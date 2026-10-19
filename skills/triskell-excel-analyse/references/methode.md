# Méthode d'analyse d'un classeur

## 1. Comprendre le fichier (avant tout calcul)
| Question | Où regarder |
|---|---|
| Quelles feuilles comptent ? Y en a-t-il de masquées ? | Profil, ligne de chaque feuille |
| Que représente **une ligne** ? (une saisie, un projet, un mois, un collaborateur) | En-têtes + 5 premières lignes |
| Où commence le tableau ? (titre au-dessus, lignes vides, en-tête sur 2 lignes) | `ligne_entete` du profil ; vérifier à l'œil |
| Quelle période ? | Dates min / max |
| Y a-t-il des formules, des totaux intermédiaires, des cellules fusionnées ? | Profil : formules, fusions ; une ligne « Total » dans les données fausse toutes les sommes |
| Clés de jointure entre feuilles (ex. nom de projet) : sont-elles écrites pareil ? | Variantes d'écriture du profil |
| Les colonnes à peu de valeurs (statut, Oui / Non, type) contiennent-elles des variantes de **sens** (« O » pour « Oui ») ? | Lire la liste des valeurs distinctes du profil : un script ne voit que les variantes d'écriture |

## 2. Typologie des anomalies
| Anomalie | Exemple | Décision par défaut |
|---|---|---|
| Date stockée en texte | « 04/09/2026 » aligné à gauche | **Corriger** (conversion, format JJ/MM/AAAA) |
| Nombre stocké en texte | « 7,5 » | **Corriger** (conversion) |
| Espaces parasites, casse | « Alpha - Déploiement␣ », « alpha - déploiement » | **Corriger** vers l'écriture de la table de référence |
| Variantes d'une même valeur | Oui / oui / O | **Corriger** si le sens est sûr ; sinon « à confirmer » |
| Doublon exact (toutes colonnes) | deux lignes identiques | **Retirer**, en le journalisant ; si un doublon peut être légitime (deux saisies de 4 h le même jour), **signaler** au lieu de retirer |
| Valeur manquante | projet vide | **Signaler** ; ne jamais deviner (même si le client permet de le déduire) |
| Valeur négative | -4 h | **Signaler** (correction de saisie ? avoir ?) |
| Valeur aberrante | 75 h sur une journée | **Signaler**, chiffrer l'impact |
| Date future dans des données de réalisé | saisie au 26/10 alors qu'on est le 19/10 | **Signaler** (prévisionnel ?), calculer avec et sans |
| Ligne de total dans les données | « Total » en bas | **Exclure** des calculs, journaliser |
| Unité mélangée | heures et jours dans la même colonne | **Signaler**, demander |

## 3. Écrire une décision de nettoyage
Une décision = un identifiant (D1, D2…), une colonne, une action, un motif. Elle est montrée à l'utilisateur **avant** de produire la copie quand elle touche plus de 5 % des lignes ou une colonne utilisée dans la réponse ; sinon elle est appliquée et journalisée.

Actions possibles dans le script : `supprimer_espaces`, `remplacer` (table de correspondance), `texte_en_nombre`, `texte_en_date`, `supprimer_doublons_exacts`, `signaler` (conditions : `<x`, `>x`, `<=x`, `>=x`, `==x`, `!=x`, `vide`, `futur`, `passé`).

## 4. Calculer proprement
- Calculer sur les données nettoyées, **hors lignes signalées**, puis donner le résultat **avec** elles quand l'écart change la conclusion.
- Contrôle croisé : somme des groupes = total ; nombre de lignes avant / après nettoyage expliqué par le journal.
- Arrondir à l'affichage seulement (2 décimales pour les jours, 0 pour les pourcentages) ; garder les valeurs exactes dans les calculs.
- Pourcentages : toujours dire « de quoi » (« 103 % des jours vendus »).

## 5. Choisir le graphique (natif Excel)
| Message | Graphique |
|---|---|
| Comparer des catégories (projets, équipes) | Barres (horizontales si les libellés sont longs) |
| Prévu vs réalisé | Barres groupées (2 séries) |
| Évolution dans le temps | Lignes |
| Répartition d'un total (5 parts maximum) | Camembert ; au-delà, barres |
Un graphique = un message ; le titre du graphique dit ce message quand c'est possible.

## 6. Ce qu'il ne faut jamais faire
- Trier ou filtrer les feuilles d'origine.
- Remplacer une formule par sa valeur dans les feuilles d'origine.
- Supprimer une colonne « inutile ».
- Compléter un vide par la moyenne.
- Annoncer un total sans dire ce qu'il exclut.
