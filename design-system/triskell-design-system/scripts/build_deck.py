#!/usr/bin/env python3
"""Génère une présentation Triskell dans le modèle officiel à partir d'un plan JSON.

Usage :
    python build_deck.py plan.json sortie.pptx [--report rapport.json] [--no-check] [--preview dossier/]

Enchaîne automatiquement : génération → contrôle charte (check_deck.py) → rapport.
--preview : si LibreOffice est disponible, exporte aussi un PDF et des aperçus PNG pour se relire.

Garanties du moteur :
- uniquement les couleurs et polices de tokens/tokens.json, dans les dispositions du modèle officiel ;
- toute valeur vide devient « [à compléter] » en orange italique et figure dans le rapport ;
- le texte se réduit s'il dépasse sa zone, sinon un avertissement est émis ;
- **mot** dans un texte = mot mis en avant en orange ;
- aucune consigne du modèle (« A MODIFIER », « Insérer… ») n'est jamais recopiée.
Types de slides : voir references/composants.md (26 composants).
"""
import json
import os
import shutil
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pptx import Presentation  # noqa: E402

import deck_slides_base  # noqa: E402
import deck_slides_data  # noqa: E402
from deck_core import STATE, asset  # noqa: E402

TYPES = {**deck_slides_base.TYPES, **deck_slides_data.TYPES}
NO_TITLE = ("cover", "agenda", "section", "closing", "statement", "quote")


def validate(plan):
    errors = []
    if not isinstance(plan.get("slides"), list) or not plan["slides"]:
        errors.append("le plan doit contenir une liste « slides » non vide")
    for n, s in enumerate(plan.get("slides", []), 1):
        t = s.get("type")
        if t not in TYPES:
            errors.append(f"slide {n} : type inconnu « {t} ». Types : {', '.join(sorted(TYPES))}")
        elif t not in NO_TITLE and not s.get("title"):
            errors.append(f"slide {n} ({t}) : titre manquant")
    if errors:
        raise SystemExit("Plan invalide :\n- " + "\n- ".join(errors))


def sequence_warnings(plan):
    types = [s["type"] for s in plan["slides"]]
    out = []
    if types[0] != "cover":
        out.append("la présentation ne commence pas par une couverture")
    if "closing" not in types and not plan.get("sans_fin"):
        out.append("pas de slide de fin (type closing)")
    run = 0
    for i, t in enumerate(types, 1):
        run = 0 if t in ("cover", "section", "agenda") else run + 1
        if run == 7:
            out.append(f"slide {i} : plus de 6 slides de contenu sans séparateur de section")
    if len(types) >= 8 and "agenda" not in types:
        out.append("présentation de 8 slides ou plus sans agenda")
    return out


def build(plan, out):
    validate(plan)
    STATE["warnings"].clear()
    STATE["missing"].clear()
    prs = Presentation(asset("template-triskell.pptx"))
    for n, s in enumerate(plan["slides"], 1):
        STATE.update(n=n, title=s.get("title", s["type"]))
        TYPES[s["type"]](prs, s)
    prs.core_properties.title = plan.get("title", "")
    prs.core_properties.author = plan.get("author", "Triskell Software France")
    prs.save(out)
    return {"fichier": out, "slides": len(plan["slides"]),
            "avertissements": STATE["warnings"] + sequence_warnings(plan),
            "champs_a_completer": list(STATE["missing"]), "nb_champs_a_completer": len(STATE["missing"])}


def preview(pptx, folder):
    soffice = shutil.which("soffice") or shutil.which("libreoffice")
    if not soffice:
        return "aperçu impossible : LibreOffice absent de cet environnement"
    os.makedirs(folder, exist_ok=True)
    subprocess.run([soffice, "--headless", "--convert-to", "pdf", "--outdir", folder, pptx], check=False, capture_output=True)
    pdf = os.path.join(folder, os.path.splitext(os.path.basename(pptx))[0] + ".pdf")
    if shutil.which("pdftoppm") and os.path.exists(pdf):
        subprocess.run(["pdftoppm", "-png", "-r", "50", pdf, os.path.join(folder, "slide")], check=False)
    return pdf if os.path.exists(pdf) else "conversion PDF échouée"


if __name__ == "__main__":
    if len(sys.argv) < 3:
        raise SystemExit(__doc__)
    plan = json.load(open(sys.argv[1], encoding="utf-8"))
    report = build(plan, sys.argv[2])
    if "--no-check" not in sys.argv:
        import check_deck
        report["controle_charte"] = [{"gravite": g, "slide": n, "message": m} for g, n, m in check_deck.check(sys.argv[2])
                                     if not m.startswith("champ encore")]
    if "--preview" in sys.argv:
        report["apercu"] = preview(sys.argv[2], sys.argv[sys.argv.index("--preview") + 1])
    if "--report" in sys.argv:
        json.dump(report, open(sys.argv[sys.argv.index("--report") + 1], "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(json.dumps(report, ensure_ascii=False, indent=2))
