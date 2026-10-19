# Résultat du skill `triskell-synthese-copil` sur les fichiers de test (FICTIF)

> Entrées : `demo2-cr-copil-alpha-2026-09-12.docx`, `demo2-echanges-mail-alpha.docx`, `demo2-note-interne-alpha.docx` (documents fictifs, aucune donnée réelle). Dans ce jeu de test, l'éditeur s'appelle « Nova Software » : il joue le rôle de Triskell.
> Demande testée : « Prépare le COPIL du 15/10 », puis « Donne-moi le plan de slides ».

---

## Pack COPIL

**Préparation du COPIL · Groupe Alpha Industrie · 15/10/2026**
Sources : CR du COPIL du 12/09 · mails du 22/09, 24/09 et 29/09 · note interne CSM du 01/10

**Météo projet : ORANGE** · les lenteurs du reporting persistent (signalées par écrit le 22/09) jusqu'au correctif annoncé pour le 20/10, et l'adoption reste à 60 % pour un objectif de 80 % ; des actions sont en place sur les deux sujets.

### 1. Suivi des engagements du dernier comité (12/09)
| Engagement | Porteur | Statut | Preuve |
|---|---|---|---|
| Diagnostic des lenteurs du reporting, retour sous 15 jours (soit le 27/09) | Nova | Tenu | mail du 24/09 : cause identifiée, correctif annoncé |
| Chiffrage du connecteur ERP | Nova | Sans trace | aucune source postérieure ; cité comme « levier » dans la note du 01/10, donc a priori non remis |
| Proposition de renouvellement avant le prochain comité | Nova | En cours | prévue « avant le comité du 15/10 » dans la note du 01/10 ; aucun envoi tracé |
| Prochain comité le 15/10 | — | Confirmé | CR du 12/09, note du 01/10 |

### 2. Faits nouveaux depuis le dernier comité
- Les lenteurs persistent : consolidation de plus de 20 minutes le lundi, des chefs de projet reviennent à Excel (mail de Julien Roche, 22/09).
- Cause identifiée : calcul de consolidation non optimisé sur les portefeuilles de plus de 300 projets ; correctif annoncé dans la version 8.4, prévue le 20/10, avec une démonstration proposée dès la mise en recette (mail du 24/09).
- La sponsor demande d'inclure dans le renouvellement une option de formation pour les chefs de projet qui utilisent peu l'outil, et veut présenter la proposition à son comité de direction début novembre (mail du 29/09).

### 3. Risques et points d'attention
| Risque | Impact | Probabilité | Niveau | Action proposée | Porteur |
|---|---|---|---|---|---|
| Lenteurs du reporting jusqu'à la livraison de la version 8.4 | fort | forte | élevé | Démonstration du correctif à l'équipe PMO dès la recette ; mesurer le temps de consolidation avant et après | Nova (Sarah Benali) |
| Adoption en dessous de l'objectif (60 % / 80 %) | moyen | forte | élevé | Plan d'adoption ; option de formation demandée le 29/09 | Nova et Alpha, porteur Alpha à désigner |
| Calendrier serré du renouvellement (échéance 31/12, comité de direction client début novembre) | fort | moyenne | élevé | Envoyer la proposition avant le comité, avec l'option de formation | Nova (Sarah Benali) |
| Chiffrage du connecteur ERP non présenté | moyen | moyenne | moyen | Confirmer l'état du chiffrage avant le comité | Nova, porteur à désigner |

### 4. Décisions attendues
| Décision | Options | Recommandation | Pour quand |
|---|---|---|---|
| Validez-vous le périmètre de la proposition de renouvellement, dont l'option de formation ? | Avec / sans option de formation | à arbitrer en séance (prix et contenu de l'option : à compléter par Nova) | avant le comité de direction client de début novembre |
| Quelle échéance fixez-vous à l'objectif de 80 % d'utilisateurs actifs ? | à proposer en séance | à arbitrer en séance | 15/10 |
| Quand organisons-nous la démonstration du correctif avec l'équipe PMO ? | dès la mise en recette (date à confirmer) | démonstration dédiée au responsable PMO | 15/10 |

### 5. Ordre du jour (1 h)
1. Météo et suivi des engagements · 10 min · Sarah Benali
2. Performance du reporting : cause, correctif, démonstration · 15 min · Nova
3. Adoption : état et plan · 10 min · Sarah Benali et Julien Roche
4. Décisions : renouvellement, objectif d'adoption, démonstration · 15 min · Claire Martin
5. Actions et prochain comité · 10 min · Sarah Benali

### 6. Contradictions entre sources et questions à l'équipe
- Pas de contradiction de date entre les trois sources.
- Le correctif est annoncé le 20/10, **après** le comité du 15/10 : la date est à reconfirmer avec l'équipe produit avant la séance, et rien ne pourra être montré en production le 15/10.
- Questions à poser à l'équipe : le chiffrage ERP est-il prêt ? la proposition de renouvellement est-elle partie ? quelle est la date de mise en recette de la version 8.4 ? le temps de consolidation « avant » est-il mesuré ? l'objectif de 80 % a-t-il une échéance écrite ?

### 7. Brief interne (ne pas transmettre)
**Risque compte : ÉLEVÉ** selon la grille (mention écrite d'une alternative le 22/09 + échéance du contrat dans moins de 6 mois). La note CSM du 01/10 dit « moyen à élevé ».
- **Ce que le client a en tête** : le responsable PMO a écrit le 22/09 qu'il faudrait « regarder d'autres solutions au moment du renouvellement » ; la sponsor reste positive et salue la réactivité (29/09).
- **Ce qu'on ne dit pas en séance** : la menace de concurrence (ne pas la citer, y répondre par la preuve : démonstration et mesure avant / après) ; le niveau de risque du compte.
- **Positions à tenir** : ne donner aucun chiffre de gain avant mesure ; la date du 20/10 se présente comme « annoncée », pas comme garantie, tant que l'équipe produit ne l'a pas reconfirmée.
- **Opportunité (à valider avec le DC avant d'en parler)** : le module de gestion des ressources intéresse l'équipe PMO, à proposer en option dans le renouvellement (note du 01/10). Ne pas l'aborder en COPIL si la proposition ne l'inclut pas encore.
- **Avant le comité** : démonstration du correctif à Julien Roche dès la recette ; proposition de renouvellement envoyée ; plan d'adoption 60 % → 80 % prêt (actions de la note du 01/10).

Voulez-vous le plan de slides pour le skill design system ?

À relire avant le COPIL.

---

## Plan de slides (recette `copil`)

Plan transmis au skill `triskell-design-system` (« Génère le deck avec le skill design system à partir de ce plan »). Les statuts « sans trace » et les échéances inconnues restent à `null` : le moteur affiche « [à compléter] » et les liste.

```json
{
  "recette": "copil",
  "title": "Nova - COPIL Groupe Alpha Industrie - 261015",
  "author": "Nova Software (fictif)",
  "slides": [
    {"type": "cover", "kicker": "Comité de pilotage", "title": "Sécuriser la performance et l'adoption avant le 31/12", "date_version": "15 octobre 2026 – Version 1.0", "client_name": "Groupe Alpha Industrie"},
    {"type": "summary", "title": "La météo du projet : orange", "messages": [
      {"title": "La cause des lenteurs est identifiée", "text": "Correctif annoncé dans la version 8.4, le 20/10, à reconfirmer"},
      {"title": "Le diagnostic a été rendu dans les délais", "text": "Retour le 24/09, engagement « sous 15 jours » tenu"},
      {"title": "L'adoption reste à 60 %", "text": "Objectif fixé en janvier : 80 % des chefs de projet"}],
      "decision": {"label": "Décisions attendues", "text": "Valider le plan d'adoption et le périmètre du renouvellement", "options": [], "color": "orange"}},
    {"type": "agenda", "items": [
      {"label": "Météo et suivi des engagements", "time": "10 min"},
      {"label": "Performance du reporting", "time": "15 min"},
      {"label": "Adoption", "time": "10 min"},
      {"label": "Décisions", "time": "15 min"},
      {"label": "Actions et prochain comité", "time": "10 min"}]},
    {"type": "section", "number": 1, "title": "Avancement"},
    {"type": "kpis", "title": "L'adoption plafonne à 60 % pour un objectif de 80 %", "kpis": [
      {"value": "60 %", "label": "chefs de projet actifs chaque semaine", "note": "CR du COPIL du 12/09", "highlight": true},
      {"value": "80 %", "label": "objectif d'adoption", "note": "fixé en janvier, échéance à préciser"},
      {"value": "> 20 min", "label": "consolidation du reporting le lundi", "note": "mail du 22/09"}],
      "source": "CR du COPIL du 12/09, mail du 22/09"},
    {"type": "timeline", "title": "Le correctif arrive le 20/10, après ce comité", "milestones": [
      {"date": "12/09", "label": "COPIL", "done": true},
      {"date": "24/09", "label": "Cause des lenteurs identifiée", "done": true},
      {"date": "15/10", "label": "COPIL", "current": true},
      {"date": "20/10", "label": "Version 8.4 annoncée", "detail": "à reconfirmer"},
      {"date": "31/12", "label": "Échéance du contrat"}]},
    {"type": "table", "title": "Un engagement tenu, deux à confirmer en séance", "columns": ["Engagement du 12/09", "Porteur", "Statut"], "rows": [
      ["Diagnostic des lenteurs sous 15 jours", "Nova", "Tenu (24/09)"],
      ["Chiffrage du connecteur ERP", "Nova", null],
      ["Proposition de renouvellement avant le comité", "Nova", null]],
      "col_widths": [6, 2, 3], "header_color": "vert"},
    {"type": "section", "number": 2, "title": "Points d'attention"},
    {"type": "table", "title": "Trois risques élevés, chacun avec une action en place", "columns": ["Risque", "Impact", "Probabilité", "Action", "Porteur"], "rows": [
      ["Lenteurs du reporting jusqu'à la version 8.4", "fort", "forte", "Démonstration du correctif dès la recette", "Nova"],
      ["Adoption en dessous de l'objectif", "moyen", "forte", "Plan d'adoption, option de formation", "Nova et Alpha"],
      ["Calendrier serré du renouvellement", "fort", "moyenne", "Proposition avant votre comité de direction", "Nova"],
      ["Chiffrage du connecteur ERP non présenté", "moyen", "moyenne", "Présenter l'état du chiffrage", "Nova"]],
      "col_widths": [4, 1.4, 1.4, 4, 1.6]},
    {"type": "section", "number": 3, "title": "Décisions"},
    {"type": "cards", "title": "Trois décisions pour tenir l'échéance du 31/12", "cards": [
      {"kicker": "Décision 1", "title": "Plan d'adoption", "text": "Fixer l'échéance de l'objectif de 80 % et valider le plan pour l'atteindre"},
      {"kicker": "Décision 2", "title": "Renouvellement", "text": "Valider le périmètre de la proposition, dont l'option de formation demandée le 29/09", "highlight": true, "badge": "Prioritaire"},
      {"kicker": "Décision 3", "title": "Démonstration du correctif", "text": "Fixer la date de démonstration avec l'équipe PMO dès la mise en recette"}]},
    {"type": "actions", "title": "Actions décidées", "teams": [
      {"team": "Groupe Alpha Industrie", "actions": [{"action": "Fixer l'échéance de l'objectif d'adoption", "owner": "Claire Martin", "due": null}]},
      {"team": "Nova Software", "actions": [
        {"action": "Démonstration du correctif à l'équipe PMO", "owner": "Sarah Benali", "due": null},
        {"action": "Plan d'adoption 60 % → 80 %", "owner": "Sarah Benali", "due": null}]}]},
    {"type": "closing", "contact": "Sarah Benali, CSM"}
  ]
}
```

**Test de génération** : ce plan a été passé au moteur du design system (`build_deck.py`) : 13 slides, aucun avertissement de mise en page, contrôle de charte vide, 5 champs « [à compléter] » (2 statuts d'engagement, 3 échéances d'action), tous attendus. Une première version avait un badge trop long sur la carte de décision : le moteur l'a signalé, le badge a été raccourci.

---

## Variante : si l'on ajoute le CR du point de suivi du 08/10 (`demo3-transcription-teams-alpha`)

Le skill signale deux contradictions sans les trancher :
- **Date du COPIL** : 15/10 (CR du 12/09, note du 01/10) / semaine du 16/11 (point de suivi du 08/10, sondage en cours) · qui tranche : la CSM.
- **Remède aux lenteurs** : correctif produit dans la version 8.4 le 20/10 (mail du 24/09) / limitation du calcul des tableaux de bord aux deux dernières années, mise en production le 22/10 (point du 08/10) · à clarifier avec l'équipe technique : deux actions complémentaires ou un changement de solution ?

---

## Relecture du test (contrôle du skill)
- Échéance relative « sous 15 jours » convertie (27/09) pour juger le statut « tenu » : conforme à `grilles.md` §1.
- Chiffrage ERP classé « sans trace », pas « en retard » : aucune échéance n'avait été fixée et aucune source n'en parle.
- La concurrence, le niveau de risque du compte et l'opportunité « gestion des ressources » n'apparaissent ni dans la synthèse, ni dans l'ordre du jour, ni dans le plan de slides.
- Aucun prix ni contenu d'option de formation inventé : « à compléter par Nova ».
- Écart repéré pendant le test et corrigé dans le skill : une livraison annoncée **après** la date du comité change ce qu'on peut montrer en séance. Ajout de ce cas dans l'étape 4 du SKILL.md (repérer aussi les chronologies impossibles, pas seulement les contradictions).
