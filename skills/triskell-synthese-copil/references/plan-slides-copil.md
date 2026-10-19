# Plan de slides du COPIL : remplir la recette `copil` du design system

> Le fichier .pptx se fabrique **uniquement** avec le skill `triskell-design-system` (modèle officiel, contrôle de charte). Ce skill-ci prépare le contenu : un plan JSON au format de `recettes/copil.json`, que l'utilisateur transmet avec la phrase « Génère le deck avec le skill design system à partir de ce plan ». Spécification de chaque type de slide : `references/composants.md` du design system.

## Correspondance sortie → slide

| N° | Type | Contenu tiré de la synthèse | Règle |
|---|---|---|---|
| 1 | `cover` | kicker « Comité de pilotage », titre = le message du comité, `date_version`, `client_name` | Titre-message, pas « COPIL n°3 » |
| 2 | `summary` | 3 messages : où en est le projet · ce qui va bien · ce qui bloque ; `decision` = la décision principale | `decision.color` : `vert`, `orange` ou `rouge` selon la météo projet |
| 3 | `agenda` | Les points de l'ordre du jour, avec `time` | Mêmes durées que l'invitation |
| 4 | `section` | 1. Avancement | |
| 5 | `kpis` | 2 à 4 chiffres **présents dans les sources**, chacun avec `note` et `source` | Chiffre inconnu = `null`, jamais estimé |
| 6 | `timeline` | Jalons : comité précédent, livraisons, comité, échéances | `done` pour le passé tenu, `current` pour le comité |
| 7 | `table` (facultatif) | Suivi des engagements : Engagement / Porteur / Statut | `header_color: "vert"` |
| 8 | `section` | 2. Points d'attention | |
| 9 | `table` | Risques : Risque / Impact / Probabilité / Action / Porteur | Version **client** des risques uniquement |
| 10 | `section` | 3. Décisions | |
| 11 | `cards` | Une carte par décision attendue, ou les options d'une décision ; `highlight` sur la recommandation | Une seule carte `highlight` |
| 12 | `actions` | Actions par équipe (Client, Triskell) avec porteur et échéance | Échéance inconnue = `null` |
| 13 | `cta` (facultatif) | Décisions demandées, qui, quand ; prochain comité | Avant `closing` |
| 14 | `closing` | `contact` = la personne qui anime | |

## Règles d'écriture (rappel du design system)
- Un titre = un message, 70 caractères maximum : « Le correctif de performance arrive le 20/10, après ce comité » plutôt que « Performance ».
- 3 à 5 puces par bloc, sans point final ; un seul accent orange (`**mot**`) par slide.
- Chaque chiffre a une `source` ; un montant précise HT ou TTC.
- Ce qui ne tient pas sur la slide va dans `notes`.
- Une valeur inconnue reste `null` : le moteur affichera « [à compléter] » et la listera.

## Ce qui n'entre jamais dans le deck client
Le contenu du brief interne : risque compte, nom de concurrent, citation d'un mail qui menace de partir, opportunité commerciale non encore proposée, données GEPIL ou HubSpot, marge, TJM. Ce qui sert à l'orateur sans être montré va dans `notes`, et seulement si ce n'est pas sensible : les notes de l'orateur restent dans le fichier envoyé.

## Squelette JSON minimal
```json
{
  "recette": "copil",
  "title": "Triskell - COPIL <Client> - <AAMMJJ>",
  "author": "Triskell Software France",
  "slides": [
    {"type": "cover", "kicker": "Comité de pilotage", "title": "<message du comité>", "date_version": "<Mois AAAA – Version 1.0>", "client_name": "<Client>"},
    {"type": "summary", "title": "La météo du projet", "messages": [{"title": "…", "text": "…"}, {"title": "…", "text": "…"}, {"title": "…", "text": "…"}], "decision": {"label": "Décisions attendues", "text": "…", "options": [], "color": "orange"}},
    {"type": "agenda", "items": [{"label": "…", "time": "10 min"}]},
    {"type": "section", "number": 1, "title": "Avancement"},
    {"type": "kpis", "title": "…", "kpis": [{"value": null, "label": "…", "note": "…"}], "source": "…"},
    {"type": "closing", "contact": null}
  ]
}
```
Le plan complet se construit en partant de `recettes/copil.json` du design system : remplace chaque « À ÉCRIRE : » et chaque `null` connu, retire les slides sans matière plutôt que de les laisser vides.
