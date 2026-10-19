# Spec de la copie propre (`scripts/copie_propre.py`)

Commande : `python scripts/copie_propre.py source.xlsx spec.json "<Nom> - analyse <AAMMJJ>.xlsx"`

Le classeur produit contient :
1. **Synthèse** (en premier) : titre, chiffres clés, tableaux de synthèse avec graphiques natifs, hypothèses, conclusions ;
2. les **feuilles d'origine**, strictement inchangées (formules et mise en forme comprises) ;
3. **Données nettoyées** : la feuille analysée après décisions, avec « Ligne d'origine » et « Contrôle » (OK ou motif du signalement, en orange) ;
4. **Journal des corrections** : chaque cellule modifiée (décision, ligne d'origine, colonne, avant, après, motif) puis la liste des décisions.

## Clés de la spec
| Clé | Obligatoire | Contenu |
|---|---|---|
| `feuille` | oui | Nom de la feuille de données à nettoyer |
| `ligne_entete` | non (1) | Ligne des en-têtes (donnée par le profil) |
| `date_reference` | non (aujourd'hui) | `JJ/MM/AAAA`, sert à la condition `futur` / `passé` |
| `titre`, `sous_titre` | non | En-tête de la Synthèse ; dire que les feuilles d'origine sont inchangées |
| `decisions` | non | Liste ordonnée : `{id, action, colonne, motif, …}` (voir `methode.md` § 3) |
| `indicateurs` | non | `{libelle, valeur, source}` : chiffres clés calculés par toi (pandas) |
| `syntheses` | non | Tableaux : `type: "pivot"` (calcul par le script) ou `type: "tableau"` (lignes calculées par toi) |
| `hypotheses`, `conclusions` | non | Listes de phrases ; une conclusion cite ses chiffres |

### Tableau `pivot`
`{titre, type: "pivot", index, valeur, agg (somme | nombre | moyenne | max | min), libelle_valeur, exclure_signalees: true, graphique: "barres" | "lignes" | "camembert", horizontal: true|false}`

### Tableau `tableau`
`{titre, type: "tableau", colonnes: [...], lignes: [[...], ...], graphique, series: [n° de colonnes à tracer, 2 = 1re colonne de valeurs], note}`
À utiliser pour les calculs croisant plusieurs feuilles (ex. consommé vs vendu) : calcule avec pandas, puis écris les lignes.

## Exemple complet
`references/exemple-spec.json` : suivi des temps fictif, 10 décisions (6 corrections, 4 signalements), 3 tableaux, 3 graphiques.

## Contrôles après génération
- Le script affiche le nombre de lignes, de modifications et de lignes signalées : ces trois nombres doivent figurer dans ta réponse.
- Relis la Synthèse (openpyxl) : chaque indicateur a une source ; chaque conclusion correspond aux tableaux.
- Vérifie que les feuilles d'origine sont identiques à la source (comparaison cellule par cellule).
