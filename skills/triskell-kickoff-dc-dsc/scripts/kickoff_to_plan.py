#!/usr/bin/env python3
"""Transforme une fiche de passation DC → DSC (JSON) en présentation « Kickoff interne TSF ».

Usage :
    python kickoff_to_plan.py fiche.json dossier_sortie/

Produit dans dossier_sortie/ :
    plan.json             le plan de slides pour build_deck.py (même trame que le modèle officiel)
    registre-manques.md   chaque information manquante, avec la section, l'équipe qui doit la fournir et sa gravité
    controles.json        les contrôles de cohérence, le taux de complétude par section et le verdict GO Projet
Puis lance build_deck.py pour générer « Kickoff interne TSF - <client> - <AAMMJJ>.pptx ».
"""
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SECTIONS = ["Éléments de contexte", "Interlocuteurs-clés côté client", "Périmètre fonctionnel & technique",
            "Démarrage du projet", "Éléments financiers", "Marketing & Communication", "Actions & Check-list « GO Projet »"]

# Qui fournit quoi (convention Triskell : DC = commercial, DSC = succès client, ADV, MKG, Support)
OWNER = {"participants": "DC", "client": "DC", "contexte": "DC", "interlocuteurs_client": "DC", "perimetre": "DSC",
         "licences": "DC", "technique": "DSC", "prestations": "DC", "repartition_charges": "DSC", "contractuel": "DC",
         "demarrage": "DSC", "financier": "DC", "facturation": "ADV", "marketing": "MKG", "go_projet": "DSC"}
CRITICAL_GO = ["Contrat signé", "Bon de commande reçu", "Périmètre clairement défini et priorisé"]

MISSING, CHECKS = [], []
PRE = {"manques": 0, "bloquants": 0}


def empty(v):
    return v is None or (isinstance(v, str) and v.strip() == "") or (isinstance(v, list) and len(v) == 0)


def need(section, champ, value, bloquant=False):
    """Enregistre un manque et renvoie la valeur (None si vide)."""
    if empty(value):
        MISSING.append({"section": section, "champ": champ, "equipe": OWNER.get(section, "DC"), "bloquant": bloquant})
        return None
    return value


def yn(v):
    return {True: "Oui", False: "Non"}.get(v, v)


def eur(v):
    return None if v is None else f"{v:,.0f} € HT".replace(",", " ")


def check(ok, gravite, message):
    if not ok:
        CHECKS.append({"gravite": gravite, "message": message})


# --------------------------------------------------------------------- contrôles de cohérence
def coherence(f):
    lic = f.get("licences", {})
    users = sum(v for k, v in lic.items() if k in ("Avancé", "Contributeur", "Lecture / Demandeur", "Flex") and isinstance(v, (int, float)))
    fin_users = f.get("financier", {}).get("licences_users")
    if fin_users is not None and users:
        check(users == fin_users, "important",
              f"Licences : {users} utilisateurs dans la configuration (Avancé + Contributeur + Lecture + Flex) contre {fin_users} dans la synthèse financière.")
    vol = f.get("prestations", {}).get("volume_jrsH")
    rep = f.get("repartition_charges") or []
    tot = sum(r.get("jrsH") or 0 for r in rep)
    if vol is not None and rep:
        check(vol == tot, "important", f"Charges : {vol} jrsH vendus contre {tot} jrsH dans la répartition des charges.")
    lignes = f.get("facturation", {}).get("lignes_gepil") or []
    if lignes and rep:
        lf = sum(l.get("jrsH") or 0 for l in lignes if l.get("type") == "facturable")
        rf = sum(r.get("jrsH") or 0 for r in rep if r.get("facturable"))
        check(lf == rf, "important", f"GEPIL : {lf} jrsH en lignes facturables contre {rf} jrsH facturables dans la répartition.")
        lnf = sum(l.get("jrsH") or 0 for l in lignes if l.get("type") != "facturable")
        rnf = sum(r.get("jrsH") or 0 for r in rep if not r.get("facturable"))
        check(lnf == rnf, "conseil", f"GEPIL : {lnf} jrsH non facturables en lignes contre {rnf} dans la répartition.")
        for l in lignes:
            if l.get("type") == "facturable" and empty(l.get("tjm")):
                CHECKS.append({"gravite": "important", "message": "GEPIL : une ligne facturable n'a pas de TJM, l'ADV ne pourra pas la créer."})
    ech = f.get("facturation", {}).get("echeancier_implementation") or []
    if ech:
        pct = sum(e.get("pourcentage") or 0 for e in ech)
        check(pct == 100, "bloquant", f"Échéancier d'implémentation : la somme fait {pct} %, elle doit faire 100 %.")
        budget = f.get("financier", {}).get("budget_implementation_ht")
        if budget:
            for e in ech:
                if e.get("pourcentage"):
                    e["montant_ht"] = round(budget * e["pourcentage"] / 100)
    d = f.get("demarrage", {})

    def to_date(s):
        m = re.match(r"(\d{2})/(\d{2})/(\d{4})", s or "")
        return (int(m.group(3)), int(m.group(2)), int(m.group(1))) if m else None

    a, b = to_date(d.get("reunion_lancement")), to_date(d.get("ouverture_service"))
    if a and b:
        check(a < b, "bloquant", "Planning : la date d'ouverture du service est antérieure ou égale à la réunion de lancement.")
    per = f.get("perimetre", {})
    if (per.get("decommissionnement") or {}).get("existe") and empty(per["decommissionnement"].get("commentaire")):
        CHECKS.append({"gravite": "important", "message": "Décommissionnement annoncé sans date ni précision : à documenter, c'est souvent la vraie échéance du projet."})
    sso = f.get("technique", {}).get("sso") or {}
    if sso.get("mise_en_oeuvre") and empty(sso.get("maintenance")):
        CHECKS.append({"gravite": "conseil", "message": "SSO prévu : préciser qui assure la maintenance SSO."})
    mk = f.get("marketing", {})
    if any(v == "oui" for v in (mk.get("consentements") or {}).values()) and empty(mk.get("contact_reference")):
        CHECKS.append({"gravite": "important", "message": "Marketing : des communications sont acceptées mais aucun contact de référence n'est nommé (il doit exister dans GEPIL)."})
    con = f.get("contractuel", {})
    if con.get("contrat_signe") is False:
        CHECKS.append({"gravite": "bloquant", "message": "Le contrat n'est pas signé : pas de démarrage."})
    if empty(f.get("facturation", {}).get("bdc_recu_le")) and con.get("commande_recue") is not True:
        CHECKS.append({"gravite": "bloquant", "message": "Aucun bon de commande reçu : aucun jour ne doit être travaillé avant réception."})
    prio = [k for k, v in (per.get("processus") or {}).items() if v.get("inclus") and not v.get("priorite")]
    if prio:
        CHECKS.append({"gravite": "conseil", "message": "Processus inclus sans priorité : " + ", ".join(prio) + "."})


# --------------------------------------------------------------------- construction des slides
def fields_from(section, d, keys=None):
    out = []
    for k in (keys or d.keys()):
        v = d.get(k) if isinstance(d, dict) else None
        out.append({"label": k, "value": need(section, k, yn(v)) if not isinstance(v, list) else (need(section, k, v) or None)})
    return out


def summary_slide(f, verdict):
    lab, ko, blockers = verdict
    d, pr, fi = f.get("demarrage", {}), f.get("prestations", {}), f.get("financier", {})
    offre = f["meta"].get("offre") or "offre à préciser"
    vol = f"{pr['volume_jrsH']} jrsH" if pr.get("volume_jrsH") else "charge à préciser"
    users = f"{fi['licences_users']} utilisateurs" if fi.get("licences_users") else "licences à préciser"
    nb_m, nb_b = PRE["manques"], PRE["bloquants"]
    reasons = (blockers + [f"Check-list : « {k} » non validé" for k in ko])[:3]
    return {"type": "summary", "title": "La passation en une page", "messages": [
        {"title": f"Offre {offre} : {users}, {vol}", "text": f"Lancement {d.get('reunion_lancement') or '[à fixer]'} · ouverture visée {d.get('ouverture_service') or '[à fixer]'}"},
        {"title": f"{nb_m} informations à réunir, dont {nb_b} bloquantes", "text": "Le registre des manques liste chaque information, l'équipe qui la fournit et sa gravité."},
        {"title": f"{len(CHECKS)} contrôles de cohérence à traiter", "text": "Licences, charges, échéancier, lignes GEPIL et consentements marketing croisés automatiquement."}],
        "decision": {"label": "Verdict GO Projet", "text": lab, "color": {"GO": "vert", "NO GO": "rouge"}.get(lab, "orange"),
                     "options": reasons or ["Tous les points de contrôle sont validés"]},
        "notes": "Verdict calculé à partir de la check-list GO et des contrôles de cohérence. La réunion décide."}


def build_plan(f, verdict=None):
    m = f["meta"]
    S = []
    S.append({"type": "cover", "kicker": "Réunion kick-off interne TSF", "title": "Transition de la DC vers la DSC",
              "date_version": f"{m.get('date_kickoff') or '[date]'} – Version {m.get('version') or '1.0'}", "client_name": m["client"]})
    if verdict:
        S.append(summary_slide(f, verdict))
    S.append({"type": "bullets", "title": "Préambule", "groups": [{"heading": "Objectifs du document", "items": [
        "Transmettre de la DC vers la DSC, l'ADV, le Marketing et le Support les informations sur le client, son besoin et l'offre formalisée",
        f"Offre concernée : {need('client', 'offre (Ready, Adapt, Plateform ou POC)', m.get('offre')) or '[à compléter]'}",
        "Rédigé par le commercial (DC) et le CSM / DP ou le consultant (DSC)",
        "À stocker dans « Clients - Projets » et à publier dans le canal Teams du client"]}]})
    p = f["participants"]
    S.append({"type": "people", "title": "Participants à la réunion", "groups": [
        {"heading": "Intervenants TSF lors du cycle de vente", "people": [{"role": k, "name": need("participants", k, v)} for k, v in p["cycle_de_vente"].items()]},
        {"heading": "Équipe en charge du projet", "people": [{"role": k, "name": need("participants", k, v)} for k, v in p["equipe_projet"].items()]},
        {"heading": "Autres invités", "people": [{"role": k, "name": need("participants", k, v)} for k, v in p["autres_invites"].items()]}]})
    S.append({"type": "agenda", "items": SECTIONS})

    # 1. Contexte
    S.append({"type": "section", "number": 1, "title": SECTIONS[0]})
    c = f["client"]
    S.append({"type": "fields", "title": "Présentation du client", "columns": [
        {"heading": "Identité", "fields": fields_from("client", c["identite"])},
        {"heading": "Autres informations", "fields": fields_from("client", c["autres"])}]})
    ctx = f["contexte"]
    lead, cv = ctx["lead"], ctx["cycle_de_vente"]
    S.append({"type": "fields", "title": "Contexte (1/2) : origine du lead et cycle de vente", "columns": [
        {"heading": "Origine du lead", "fields": [
            {"label": "Date du lead", "value": need("contexte", "date du lead", lead.get("date"))},
            {"label": "Contexte du lead", "value": need("contexte", "contexte du lead", lead.get("contexte"))},
            {"label": "Cahier des charges", "value": need("contexte", "cahier des charges", yn(lead.get("cahier_des_charges")))}]},
        {"heading": "Le cycle de vente", "fields": [
            {"label": "Raisons du choix de Triskell", "value": need("contexte", "raisons du choix", cv.get("raisons_du_choix"), True)},
            {"label": "Concurrence", "value": need("contexte", "concurrence", cv.get("concurrence"))},
            {"label": "Dates clés", "value": need("contexte", "dates clés", cv.get("dates_cles"))},
            {"label": "Maquette / démo / gouvernance présentée", "value":
                f"Maquette : {yn(cv.get('maquette')) or '?'} · Démo : {yn(cv.get('demo_base_demo')) or '?'} · Gouvernance : {yn(cv.get('gouvernance_presentee')) or '?'}"}]}]})
    S.append({"type": "bullets", "title": "Contexte (2/2) : ce que le client attend", "groups": [
        {"heading": "Objectifs & enjeux du projet", "items": need("contexte", "objectifs et enjeux", ctx.get("objectifs_enjeux"), True) or [None]},
        {"heading": "Challenges du client", "items": need("contexte", "challenges du client", ctx.get("challenges")) or [None]},
        {"heading": "Facteurs-clés de succès exprimés", "items": need("contexte", "facteurs-clés de succès", ctx.get("facteurs_cles_succes"), True) or [None]}]})

    # 2. Interlocuteurs
    S.append({"type": "section", "number": 2, "title": SECTIONS[1]})
    ic = f["interlocuteurs_client"]
    rows = [[k, need("interlocuteurs_client", k, ", ".join(v) if isinstance(v, list) else v, k in ("Sponsor", "Futur(e) administrateur(-trice) Solution"))] for k, v in ic.items()]
    S.append({"type": "table", "title": "Les interlocuteurs-clés côté client", "columns": ["Rôle", "Acteur"], "rows": rows, "col_widths": [2, 3], "header_color": "vert"})

    # 3. Périmètre
    S.append({"type": "section", "number": 3, "title": SECTIONS[2]})
    per = f["perimetre"]
    prow = []
    for k, v in per["processus"].items():
        inc = v.get("inclus")
        prow.append([k, need("perimetre", f"inclus ? {k}", {True: "Oui", False: "Non"}.get(inc)), (f"P{v['priorite']}" if v.get("priorite") else ("—" if inc is False else None)), v.get("detail") or "—"])
    S.append({"type": "table", "title": "Périmètre fonctionnel (1/3) : processus de pilotage", "columns": ["Processus", "Inclus", "Priorité", "Précisions"],
              "rows": prow, "col_widths": [4, 1.2, 1.2, 4]})
    dc, mep = per["decommissionnement"], per["contrainte_mise_en_production"]
    ex = per["echanges_client"]
    S.append({"type": "fields", "title": f"Périmètre fonctionnel (2/3) : échanges client du {ex.get('date') or '[date]'}", "columns": [
        {"heading": "Priorités et inputs", "fields": [
            {"label": "Priorités", "value": need("perimetre", "priorités", ex.get("priorites"), True)},
            {"label": "Documents et inputs à prendre en compte", "value": need("perimetre", "documents et inputs", ex.get("documents_inputs"))}]},
        {"heading": "Contraintes", "fields": [
            {"label": "Contraintes calendaires", "value": need("perimetre", "contraintes calendaires", ex.get("contraintes_calendaires"))},
            {"label": "Décommissionnement d'une solution existante", "value": need("perimetre", "décommissionnement", " · ".join(x for x in [yn(dc.get("existe")), dc.get("commentaire")] if x) or None)},
            {"label": "Contrainte de mise en production", "value": need("perimetre", "contrainte de mise en production", " · ".join(x for x in [yn(mep.get("existe")), mep.get("commentaire")] if x) or None)}]}]})
    lic, tech = f["licences"], f["technique"]
    sso = tech.get("sso") or {}
    S.append({"type": "fields", "title": "Périmètre (3/3) : licences, configuration et technique", "columns": [
        {"heading": "Configuration des licences", "inline": True, "fields": [{"label": k, "value": need("licences", k, None if v is None else str(v))} for k, v in lic.items()]},
        {"heading": "Aspects techniques", "fields": [
            {"label": "SSO", "value": need("technique", "SSO", f"Mise en œuvre : {yn(sso.get('mise_en_oeuvre')) or '?'} · Maintenance : {yn(sso.get('maintenance')) or '?'} · Nombre : {sso.get('nombre') or '?'}")},
            {"label": "Intégrations ou interfaces", "value": need("technique", "intégrations", tech.get("integrations"))}]}]})
    pr, con = f["prestations"], f["contractuel"]
    S.append({"type": "fields", "title": "Implémentation, services et aspects contractuels", "columns": [
        {"heading": "Contenu des prestations", "fields": [
            {"label": "Volume projet (implémentation)", "value": need("prestations", "volume jrsH", f"{pr['volume_jrsH']} jrsH · {pr.get('mode') or 'forfait ou régie ?'}" if pr.get("volume_jrsH") else None, True)},
            {"label": "Formation admin", "value": need("prestations", "formation admin", pr.get("formation_admin"))},
            {"label": "Reprise de données", "value": need("prestations", "reprise de données", pr.get("reprise_donnees"))},
            {"label": "Pack Change", "value": need("prestations", "pack change", pr.get("pack_change"))},
            {"label": "Pack Contextualisation", "value": need("prestations", "pack contextualisation", pr.get("pack_contextualisation"))}]},
        {"heading": "Aspects contractuels", "fields": [
            {"label": "Durée d'engagement", "value": need("contractuel", "durée d'engagement", con.get("duree_engagement"), True)},
            {"label": "Conditions de renouvellement", "value": need("contractuel", "renouvellement", con.get("conditions_renouvellement"))},
            {"label": "Contrat", "value": need("contractuel", "contrat signé", yn(con.get("contrat_signe")), True)},
            {"label": "Commande", "value": need("contractuel", "commande reçue", yn(con.get("commande_recue")), True)}]}]})

    # 4. Démarrage
    S.append({"type": "section", "number": 4, "title": SECTIONS[3]})
    d = f["demarrage"]
    S.append({"type": "fields", "title": "Démarrage projet : macro-planification évoquée avec le client", "columns": [
        {"heading": "Macro-planification", "fields": [
            {"label": "Réunion de lancement", "value": need("demarrage", "réunion de lancement", d.get("reunion_lancement"), True)},
            {"label": "Durée du projet", "value": need("demarrage", "durée du projet", d.get("duree_projet"))},
            {"label": "Ouverture de service visée", "value": need("demarrage", "ouverture de service", d.get("ouverture_service"), True)},
            {"label": "Gouvernance", "value": need("demarrage", "gouvernance", d.get("gouvernance"))},
            {"label": "Ateliers", "value": "Ateliers de 1h30 à 2h à caler"}]},
        {"heading": "Points d'attention détectés", "fields": [{"label": "Lors de l'échange client", "value": need("demarrage", "points d'attention", d.get("points_attention"))}]}]})
    rep = f.get("repartition_charges") or []
    if rep:
        S.append({"type": "table", "title": f"Répartition des charges : {sum(r.get('jrsH') or 0 for r in rep)} jrsH au total",
                  "columns": ["Poste", "Charge", "Facturable"], "rows": [[r["poste"], f"{r.get('jrsH')} jrsH" if r.get("jrsH") is not None else None, "F" if r.get("facturable") else "NF"] for r in rep],
                  "col_widths": [4, 1.5, 1.5], "notes": "Reporter ici le plan de charges GEPIL (onglet Tableau des ressources) : capture à insérer à la main."})

    # 5. Financier
    S.append({"type": "section", "number": 5, "title": SECTIONS[4]})
    fi, fa = f["financier"], f["facturation"]
    syn = fi.get("synthese") or []
    if syn:
        S.append({"type": "table", "title": "Synthèse financière : licences et implémentation",
                  "columns": ["Poste"] + [s["periode"] for s in syn],
                  "rows": [[f"Licences pour {fi.get('licences_users') or '?'} utilisateurs"] + [eur(s.get("montant_ht")) for s in syn],
                           ["Implémentation"] + [eur(fi.get("budget_implementation_ht"))] + ["—"] * (len(syn) - 1)],
                  "source": "proposition commerciale " + (need("financier", "référence de la proposition validée", fi.get("reference_proposition")) or "[référence à compléter]")})
    ech = fa.get("echeancier_implementation") or []
    S.append({"type": "fields", "title": "Facturation", "columns": [
        {"heading": "Licences et implémentation", "fields": [
            {"label": "Facturation des licences", "value": need("facturation", "début de facturation des licences", f"À compter du {fa['licences_a_compter_du']} · {fa.get('paiement') or ''}".strip(" ·") if fa.get("licences_a_compter_du") else None, True)},
            {"label": "Échéancier de l'implémentation", "value": [f"{e.get('pourcentage')} % · {e.get('jalon')} · {eur(e.get('montant_ht')) or '?'} le {e.get('date') or '?'}" for e in ech] or need("facturation", "échéancier", None, True)},
            {"label": "Termes de paiement", "value": need("facturation", "termes de paiement", fa.get("termes_paiement"))}]},
        {"heading": "GEPIL et commande", "fields": [
            {"label": "Lignes à créer dans GEPIL", "value": [f"{l.get('type')} « {l.get('libelle') or '?'} » : {l.get('jrsH')} jrsH" + (f" au TJM de {l['tjm']} €" if l.get("tjm") else "") for l in fa.get("lignes_gepil") or []] or None},
            {"label": "Sous-traitance à un partenaire", "value": "Non" if not (fa.get("sous_traitance") or {}).get("existe") else (fa["sous_traitance"].get("scope") or None)},
            {"label": "Réception du BDC", "value": need("facturation", "date de réception du BDC", fa.get("bdc_recu_le"), True)}]}]})

    # 6. Marketing
    S.append({"type": "section", "number": 6, "title": SECTIONS[5]})
    mk = f["marketing"]
    S.append({"type": "checklist", "title": "MKG : le client accepte-t-il de communiquer ?",
              "subtitle": "Contact pour la référence : " + (need("marketing", "contact de référence (doit exister dans GEPIL)", mk.get("contact_reference")) or "[à compléter]"),
              "items": [{"question": k, "status": v} for k, v in (mk.get("consentements") or {}).items()], "verdict": False})

    # 7. Actions & GO
    S.append({"type": "section", "number": 7, "title": SECTIONS[6]})
    S.append({"type": "actions", "title": "Actions à mener en sortie du kick-off", "teams": [
        {"team": "Support", "actions": [{"action": "Créer les instances client (sandbox et production)", "owner": "Support"},
                                        {"action": "Donner les accès à SKORAN et au Teams Triskell Club Utilisateurs", "owner": "Support"},
                                        {"action": "Envoyer le mail de bienvenue (copie ADV et CSM / DP) avec la présentation du Club Utilisateurs", "owner": "Support"}]},
        {"team": "DC & CSM (HubSpot)", "actions": [{"action": "Basculer les contacts en clients", "owner": "DC"},
                                                   {"action": "Créer, rattacher et actualiser les contacts de la solution client", "owner": "CSM"}]},
        {"team": "CSM / DP & DC", "actions": [{"action": "Formaliser l'échéancier de facturation et le transmettre à l'ADV", "owner": "CSM / DP"}]},
        {"team": "ADV", "actions": [{"action": "Créer la souscription et les lignes F et NF dans GEPIL", "owner": "ADV"}]},
        {"team": "Marketing", "actions": [{"action": "Initier la fiche référence client", "owner": "MKG"}]}],
        "notes": "Rappel Support : ne pas toper en « Comm. Incident » tant que la production n'est pas ouverte. Les échéances sont à fixer en séance."})
    go = f["go_projet"]
    S.append({"type": "checklist", "title": "Check-list « GO Projet »", "items": [
        {"question": k, "status": v.get("statut"), "comment": v.get("commentaire"), "critical": k in CRITICAL_GO,
         "owner": "ADV" if "commande" in k.lower() else ("DC" if ("contrat" in k.lower() or "hubspot" in k.lower()) else "DSC")} for k, v in go.items()]})
    S.append({"type": "closing"})
    return {"title": f"Kickoff interne TSF - {m['client']}", "author": "Triskell Software France", "slides": S}


def completeness(f):
    out = {}
    for sec in OWNER:
        miss = sum(1 for x in MISSING if x["section"] == sec)
        out[sec] = miss
    return out


def go_verdict(f):
    go = f["go_projet"]
    crit_ko = [k for k in CRITICAL_GO if (go.get(k) or {}).get("statut") != "oui"]
    others = [k for k, v in go.items() if v.get("statut") != "oui" and k not in CRITICAL_GO]
    blockers = [c["message"] for c in CHECKS if c["gravite"] == "bloquant"]
    if crit_ko or blockers:
        return "NO GO", crit_ko, blockers
    if others:
        return "GO sous réserve", others, []
    return "GO", [], []


def write_registry(f, path, verdict):
    lab, ko, blockers = verdict
    L = [f"# Registre des manques — kick-off {f['meta']['client']}", "",
         f"**Verdict GO Projet : {lab}**", ""]
    if ko:
        L += ["Points de la check-list non validés : " + " ; ".join(ko), ""]
    if CHECKS:
        rank = {"bloquant": 0, "important": 1, "conseil": 2}
        L += ["## Contrôles de cohérence", ""] + [f"- **{c['gravite'].upper()}** — {c['message']}" for c in sorted(CHECKS, key=lambda c: rank[c["gravite"]])] + [""]
    L += ["## Informations à obtenir", "", "| Équipe | Section | Information | Bloquant |", "|---|---|---|---|"]
    for x in sorted(MISSING, key=lambda x: (not x["bloquant"], x["equipe"], x["section"])):
        L.append(f"| {x['equipe']} | {x['section']} | {x['champ']} | {'oui' if x['bloquant'] else ''} |")
    L += ["", f"Total : {len(MISSING)} informations manquantes, dont {sum(1 for x in MISSING if x['bloquant'])} bloquantes."]
    open(path, "w", encoding="utf-8").write("\n".join(L))


def find_builder():
    for cand in [os.path.join(HERE, "build_deck.py"), os.path.join(HERE, "..", "..", "triskell-design-system", "scripts", "build_deck.py")]:
        if os.path.exists(cand):
            return os.path.abspath(cand)
    return None


if __name__ == "__main__":
    if len(sys.argv) < 3:
        raise SystemExit(__doc__)
    fiche = json.load(open(sys.argv[1], encoding="utf-8"))
    out = sys.argv[2]
    os.makedirs(out, exist_ok=True)
    coherence(fiche)
    verdict = go_verdict(fiche)
    build_plan(fiche)  # premier passage : recense les manques pour la synthèse
    n_missing = len(MISSING)
    PRE.update(manques=n_missing, bloquants=sum(1 for x in MISSING if x["bloquant"]))
    del MISSING[:]
    plan = build_plan(fiche, verdict)
    assert len(MISSING) == n_missing
    json.dump(plan, open(os.path.join(out, "plan.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    write_registry(fiche, os.path.join(out, "registre-manques.md"), verdict)
    ctrl = {"verdict": verdict[0], "points_non_valides": verdict[1], "bloquants": verdict[2], "controles": CHECKS,
            "manques_par_section": completeness(fiche), "nb_manques": len(MISSING), "nb_manques_bloquants": sum(1 for x in MISSING if x["bloquant"])}
    json.dump(ctrl, open(os.path.join(out, "controles.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    builder = find_builder()
    if builder:
        d = (fiche["meta"].get("date_kickoff") or "").split("/")
        stamp = (d[2][2:] + d[1] + d[0]) if len(d) == 3 else "AAMMJJ"
        pptx = os.path.join(out, f"{fiche['meta']['client']} - Kickoff interne TSF - {stamp}.pptx")
        subprocess.run([sys.executable, builder, os.path.join(out, "plan.json"), pptx, "--report", os.path.join(out, "rapport-build.json")], check=True, stdout=subprocess.DEVNULL)
        ctrl["fichier"] = pptx
    print(json.dumps(ctrl, ensure_ascii=False, indent=2))
