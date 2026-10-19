# Les 26 composants du moteur

Chaque slide du plan est un objet JSON avec un `type`. Champs communs facultatifs : `subtitle` (chapeau d'une ligne sous le titre), `notes` (notes orateur), `source` (affichée en bas à gauche). Toute valeur `null` ou vide devient « [à compléter] » et part dans le rapport. Dans tout texte, `**mot**` met le mot en orange gras : un seul par slide. Exemple complet utilisant les 26 types : `references/exemple-plan.json`.

## Matrice de choix
| Je veux… | Composant |
|---|---|
| Ouvrir | `cover` |
| Résumer pour un décideur (3 messages + décision) | `summary` |
| Annoncer le plan, avec durées | `agenda` |
| Changer de partie | `section` |
| Poser une affirmation forte | `statement` |
| Mettre en avant 2 à 4 chiffres | `kpis` |
| Montrer une tendance, une comparaison, une répartition | `chart` |
| Comparer la situation actuelle et la cible | `before_after` |
| Présenter 2 à 4 options, enjeux, engagements | `cards` |
| Prioriser (valeur / effort, risques) | `matrix` |
| Montrer la solution avec une photo | `image_text` |
| Dérouler des points en 1 à 4 blocs | `bullets` |
| Remplir une fiche (identité, licences, contrat) | `fields` |
| Montrer une démarche | `steps` |
| Montrer des phases et leurs livrables | `phases` |
| Montrer des jalons datés | `timeline` |
| Montrer une feuille de route par chantier | `roadmap` |
| Présenter l'équipe | `team` |
| Lister des participants par rôle | `people` |
| Présenter des formules chiffrées | `offer` |
| Montrer des données en lignes et colonnes | `table` |
| Vérifier avant une décision (GO / NO GO) | `checklist` |
| Dire qui fait quoi pour quand | `actions` |
| Citer un client ou un dirigeant | `quote` |
| Demander une décision, fixer le prochain rendez-vous | `cta` |
| Conclure | `closing` |

## Spécifications

**cover** — `{"type":"cover","kicker":"Proposition d'accompagnement","title":"…","date_version":"Octobre 2026 – Version 1.0","client_name":"Client Alpha","client_logo":"logo.png","confidential":true}`
`client_logo` uniquement s'il est fourni ; sinon « Pour <client> » en vert. Mention « Document confidentiel » par défaut (`confidential:false` pour la retirer).

**summary** — `{"type":"summary","title":"L'essentiel en une page","messages":[{"title":"…","text":"…"}×3],"decision":{"label":"Décision attendue","text":"…","options":["…"],"color":"vert"}}` — `color` : `vert` (défaut), `orange` (sous réserve), `rouge` (NO GO).

**agenda** — `{"type":"agenda","items":["…"] ou [{"label":"…","time":"10 min"}],"current":2,"qa":true}` — 8 points maximum ; `current` met en avant la partie en cours.

**section** — `{"type":"section","number":1,"title":"…","teaser":"une phrase d'accroche facultative"}`

**statement** — `{"type":"statement","title":"Le constat","text":"Vos comités arbitrent **180 projets** avec…","support":"…","source":"…"}`

**kpis** — `{"type":"kpis","title":"…","kpis":[{"value":"180","label":"projets actifs","note":"…","highlight":false}],"takeaway":"la phrase à retenir","source":"…"}` — 2 à 4 chiffres, `source` obligatoire.

**chart** — `{"type":"chart","title":"…","chart":"column|bar|stacked|line|donut","categories":["2023","2024"],"series":[{"name":"…","values":[6,8]}],"highlight_category":"2024","key_figure":"×2","takeaway":"…","takeaway_detail":"…","number_format":"# ##0","labels":true,"source":"…"}`
Graphique natif PowerPoint, modifiable par l'utilisateur. Avec `takeaway`, un panneau « à retenir » s'affiche à droite. `highlight_category` colore une barre en orange (une seule série).

**before_after** — `{"type":"before_after","title":"…","before":{"label":"Aujourd'hui","title":"…","items":["…"]},"after":{"label":"Avec Triskell","title":"…","items":["…"]}}`

**cards** — `{"type":"cards","title":"…","cards":[{"kicker":"Engagement 1","title":"…","text":"…","items":["…"],"highlight":true,"badge":"Votre priorité","icon_text":"1"}],"card_height":11}` — 2 à 4 cartes, une seule `highlight`.

**matrix** — `{"type":"matrix","title":"…","x_label":"Effort","y_label":"Valeur","quadrants":["haut-gauche","haut-droit","bas-gauche","bas-droit"],"highlight_quadrant":0,"items":[{"label":"…","x":0.3,"y":0.85,"highlight":true}],"reading":["lecture 1","lecture 2"],"reading_title":"Lecture"}` — `x` et `y` entre 0 et 1.

**image_text** — `{"type":"image_text","title":"…","image":"reunion-equipe|couverture-ppm|chemin.jpg","side":"left|right","kicker":"…","heading":"…","text":"…","items":["…"]}` — photos du modèle dans `assets/photos/`, recadrées automatiquement.

**bullets** — `{"type":"bullets","title":"…","groups":[{"heading":"…","items":["…"],"accent":"orange|vert"}],"plain":false,"compact":false}` — 1 groupe sans intertitre = texte libre ; 2 à 4 groupes = panneaux.

**fields** — `{"type":"fields","title":"…","columns":[{"heading":"Identité","inline":false,"fields":[{"label":"Secteur","value":"…"},{"label":"Chiffres-clés","value":["…","…"]}]}]}` — 1 à 3 colonnes ; `inline:true` = « Libellé : valeur » sur une ligne.

**steps** — `{"type":"steps","title":"…","steps":[{"title":"Cadrer","text":"…","duration":"3 semaines","highlight":false}]}` — 3 à 6 étapes.

**phases** — `{"type":"phases","title":"…","phases":[{"name":"Cadrage","dates":"Novembre","items":["…"],"deliverable":"…","current":true}]}` — 3 à 6 phases.

**timeline** — `{"type":"timeline","title":"…","milestones":[{"date":"05/11","label":"Kick-off","detail":"…","done":true,"current":false}]}` — 3 à 8 jalons ; la frise se remplit en vert jusqu'au dernier jalon `done`.

**roadmap** — `{"type":"roadmap","title":"…","periods":["Nov.","Déc."],"today":0,"lanes":[{"name":"Conception","bars":[{"start":0,"end":1.5,"label":"Ateliers","highlight":false}]}],"milestones":[{"at":5,"label":"Ouverture"}]}` — `start`, `end`, `at` en nombre de périodes depuis le début (décimales permises).

**team** — `{"type":"team","title":"…","members":[{"name":"…","role":"…","text":"…","lead":true}]}` — 1 à 8 personnes, initiales calculées.

**people** — `{"type":"people","title":"Participants","groups":[{"heading":"…","people":[{"role":"DC","name":null}]}]}`

**offer** — `{"type":"offer","title":"…","offers":[{"name":"Adapt","price":"25 k€","period":"implémentation HT","pitch":"…","items":["…"],"recommended":true,"badge":"Recommandé"}],"footnote":"…"}` — 2 à 4 formules, une seule recommandée.

**table** — `{"type":"table","title":"…","columns":["Poste","Année 1"],"rows":[["…","…"]],"col_widths":[3,1],"numeric_columns":[1],"header_color":"orange_tableau|vert","highlight_row":0,"total_row":true,"source":"…"}` — 12 lignes maximum ; colonnes chiffrées alignées à droite.

**checklist** — `{"type":"checklist","title":"…","items":[{"question":"…","status":"oui|non|null","owner":"DC","comment":"…","critical":true}],"verdict":true}` — verdict GO / GO sous réserve / NO GO calculé (une ligne `critical` pas à « oui » = NO GO).

**actions** — `{"type":"actions","title":"…","teams":[{"team":"Client","actions":[{"action":"…","owner":"…","due":"25/10"}]}]}`

**quote** — `{"type":"quote","text":"…","author":"…","role":"…"}` — uniquement un propos validé par écrit.

**cta** — `{"type":"cta","title":"Ce que nous vous proposons de décider","asks":[{"what":"…","who":"…","when":"…"}],"next_label":"Prochain rendez-vous","next":"Kick-off le 5 novembre","contact":"…"}`

**closing** — `{"type":"closing","contact":"…","details":["…"]}`

## Limites connues
- La police Montserrat doit être installée sur le poste qui ouvre le fichier, sinon PowerPoint la remplace ; la mise en page reste juste.
- Le surlignage d'une barre de graphique (`highlight_category`) s'affiche dans PowerPoint ; Keynote peut l'ignorer.
- Captures GEPIL / HubSpot : à insérer à la main, jamais à reconstituer.
