"""Écrit les réponses dans une COPIE du questionnaire Excel du prospect.

Usage :
    python remplir.py questionnaire.xlsx reponses.json sortie.xlsx            # copie de travail (interne)
    python remplir.py questionnaire.xlsx reponses.json sortie.xlsx --client   # version à envoyer

Copie de travail : la structure du prospect est conservée (feuilles, lignes, colonnes,
mise en forme). Le script remplit la colonne réponse (et la colonne justificatif /
oui-non si elles existent), puis ajoute à droite 4 colonnes internes :
Statut · Confiance · Source dans la base · À valider par / note, et une feuille
« Synthèse interne » (compteurs + questions à envoyer au RSSI / DPO).

Version client (--client) : aucune colonne ni feuille interne. Refuse de produire le
fichier s'il reste une réponse « À valider » ou « Hors base » (option --forcer pour
passer outre, à n'utiliser qu'après arbitrage écrit du responsable).

Format de reponses.json : voir references/format-reponses.md.
"""
import argparse
import json
import sys
from copy import copy
from pathlib import Path

import openpyxl
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.worksheet.datavalidation import DataValidation

sys.path.insert(0, str(Path(__file__).resolve().parent))
from extraire import _trouver_entete  # noqa: E402

STATUTS = ("Validé", "À valider", "Hors base")
CONFIANCES = ("Haute", "Moyenne", "Basse", "—")
COULEURS = {"Validé": "E6F5F3", "À valider": "FFF3E6", "Hors base": "FDE7EA"}
COLONNES_INTERNES = (
    ("Statut (interne)", 14),
    ("Confiance (interne)", 13),
    ("Source dans la base (interne)", 30),
    ("À valider par / note (interne)", 40),
)
TEXTE_HORS_BASE = "[À compléter par {qui}]"


def charger_reponses(chemin):
    data = json.loads(Path(chemin).read_text(encoding="utf-8"))
    erreurs = []
    for i, r in enumerate(data.get("reponses", [])):
        if r.get("statut") not in STATUTS:
            erreurs.append(f"réponse {i} (ligne {r.get('ligne')}) : statut « {r.get('statut')} » invalide")
        if r.get("statut") == "Validé" and not r.get("source"):
            erreurs.append(f"ligne {r.get('ligne')} : une réponse « Validé » doit citer sa source dans la base")
        if r.get("statut") == "Hors base" and r.get("reponse"):
            erreurs.append(f"ligne {r.get('ligne')} : « Hors base » ne doit pas contenir de réponse rédigée")
    if erreurs:
        sys.exit("reponses.json refusé :\n- " + "\n- ".join(erreurs))
    return data


def _copier_style(source, cible):
    cible.font = copy(source.font)
    cible.fill = copy(source.fill)
    cible.border = copy(source.border)
    cible.alignment = copy(source.alignment)
    cible.number_format = source.number_format


def _ecrire(ws, ligne, colonne, valeur, colonne_modele):
    """Écrit une valeur en reprenant le style de la cellule « question » de la même ligne."""
    cell = ws.cell(ligne, colonne)
    cell.value = valeur
    modele = ws.cell(ligne, colonne_modele) if colonne_modele else None
    if modele is not None and modele.has_style and not cell.has_style:
        _copier_style(modele, cell)
    cell.alignment = Alignment(wrap_text=True, vertical="top")


def _ajouter_colonnes_internes(ws, ligne_entete, premiere, lignes):
    entete_modele = ws.cell(ligne_entete, premiere - 1)
    for k, (titre, largeur) in enumerate(COLONNES_INTERNES):
        col = premiere + k
        cell = ws.cell(ligne_entete, col, titre)
        _copier_style(entete_modele, cell)
        ws.column_dimensions[openpyxl.utils.get_column_letter(col)].width = largeur
    lettre = openpyxl.utils.get_column_letter(premiere)
    dv = DataValidation(type="list", formula1='"' + ",".join(STATUTS) + '"', allow_blank=True)
    ws.add_data_validation(dv)
    if lignes:
        dv.add(f"{lettre}{min(lignes)}:{lettre}{max(lignes)}")


def remplir_feuille(ws, reponses, client):
    ligne_entete, colonnes = _trouver_entete(ws)
    if not ligne_entete:
        return []
    col_rep = colonnes.get("reponse")
    if col_rep is None:  # pas de colonne réponse : on en crée une juste après la question
        col_rep = ws.max_column + 1
        _copier_style(ws.cell(ligne_entete, colonnes["question"]), ws.cell(ligne_entete, col_rep, "Réponse"))
        ws.column_dimensions[openpyxl.utils.get_column_letter(col_rep)].width = 50
    premiere_interne = ws.max_column + 1
    traitees = []
    for r in reponses:
        ligne = r["ligne"]
        if not ws.cell(ligne, colonnes["question"]).value:
            sys.exit(f"Feuille « {ws.title} », ligne {ligne} : aucune question à cette ligne. Vérifier reponses.json.")
        texte = r.get("reponse") or ""
        if r["statut"] == "Hors base":
            texte = TEXTE_HORS_BASE.format(qui=r.get("a_valider_par") or "l'équipe sécurité")
        _ecrire(ws, ligne, col_rep, texte, colonnes["question"])
        if "source" in colonnes and r.get("justificatif"):
            _ecrire(ws, ligne, colonnes["source"], r["justificatif"], colonnes["question"])
        if "oui_non" in colonnes and r.get("oui_non") and r["statut"] == "Validé":
            _ecrire(ws, ligne, colonnes["oui_non"], r["oui_non"], colonnes["question"])
        if not client:
            valeurs = (r["statut"], r.get("confiance", "—"), r.get("source", ""),
                       " · ".join(x for x in (r.get("a_valider_par"), r.get("note")) if x))
            for k, v in enumerate(valeurs):
                _ecrire(ws, ligne, premiere_interne + k, v, colonnes["question"])
            ws.cell(ligne, premiere_interne).fill = PatternFill("solid", fgColor=COULEURS[r["statut"]])
        traitees.append({**r, "feuille": ws.title, "question": str(ws.cell(ligne, colonnes["question"]).value),
                         "numero": ws.cell(ligne, colonnes["numero"]).value if "numero" in colonnes else ""})
    if not client:
        _ajouter_colonnes_internes(ws, ligne_entete, premiere_interne, [r["ligne"] for r in reponses])
    return traitees


def ajouter_synthese(wb, traitees, meta, total_questions):
    ws = wb.create_sheet("Synthèse interne")
    gras = Font(bold=True)
    ws.append(["Synthèse interne — à supprimer avant envoi au prospect"])
    ws["A1"].font = Font(bold=True, size=13)
    ws.append([f"Base utilisée : {meta.get('base', '[à préciser]')}"])
    ws.append([])
    ws.append(["Statut", "Nombre"])
    for statut in STATUTS:
        ws.append([statut, sum(1 for r in traitees if r["statut"] == statut)])
    ws.append(["Questions du fichier sans réponse préparée", total_questions - len(traitees)])
    ws.append([])
    ws.append(["Questions à envoyer pour validation", "", "", "", ""])
    ws.append(["N° (feuille / ligne)", "Question", "Statut", "À valider par", "Ce qu'il manque"])
    for row in (4, ws.max_row - 1, ws.max_row):
        for c in ws[row]:
            c.font = gras
    for r in traitees:
        if r["statut"] != "Validé":
            ws.append([f"{r.get('numero', '')} ({r['feuille']} / {r['ligne']})", r.get("question", ""),
                       r["statut"], r.get("a_valider_par", ""), r.get("note", "")])
    for lettre, largeur in zip("ABCDE", (22, 70, 12, 26, 60)):
        ws.column_dimensions[lettre].width = largeur
    for row in ws.iter_rows(min_row=10):
        for c in row:
            c.alignment = Alignment(wrap_text=True, vertical="top")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("questionnaire")
    p.add_argument("reponses")
    p.add_argument("sortie")
    p.add_argument("--client", action="store_true", help="version à envoyer, sans colonnes internes")
    p.add_argument("--forcer", action="store_true", help="avec --client : accepter des réponses non validées")
    a = p.parse_args()

    if Path(a.sortie).resolve() == Path(a.questionnaire).resolve():
        sys.exit("La sortie doit être une copie : ne jamais écraser le fichier du prospect.")
    data = charger_reponses(a.reponses)
    reponses = data["reponses"]
    if a.client and not a.forcer:
        restantes = [r for r in reponses if r["statut"] != "Validé"]
        if restantes:
            lignes = ", ".join(str(r["ligne"]) for r in restantes)
            sys.exit(f"Version client refusée : {len(restantes)} réponse(s) non validée(s) (lignes {lignes}).")

    wb = openpyxl.load_workbook(a.questionnaire)
    traitees, total = [], 0
    par_feuille = {}
    for r in reponses:
        par_feuille.setdefault(r.get("feuille") or wb.worksheets[0].title, []).append(r)
    for ws in wb.worksheets:
        ligne_entete, colonnes = _trouver_entete(ws)
        if ligne_entete:
            total += sum(1 for row in range(ligne_entete + 1, ws.max_row + 1)
                         if ws.cell(row, colonnes["question"]).value)
        if ws.title in par_feuille:
            traitees += remplir_feuille(ws, par_feuille[ws.title], a.client)
    inconnues = set(par_feuille) - {ws.title for ws in wb.worksheets}
    if inconnues:
        sys.exit(f"Feuilles absentes du questionnaire : {', '.join(sorted(inconnues))}")
    if not a.client:
        ajouter_synthese(wb, traitees, data.get("meta", {}), total)
    wb.save(a.sortie)

    compte = {s: sum(1 for r in traitees if r["statut"] == s) for s in STATUTS}
    print(json.dumps({"sortie": a.sortie, "questions": total, "preparees": len(traitees), **compte},
                     ensure_ascii=False))


if __name__ == "__main__":
    main()
