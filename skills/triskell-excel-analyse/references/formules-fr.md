# Formules Excel en version française

## Règles d'écriture
- **Séparateur d'arguments : point-virgule** `;` (Excel en français). Virgule décimale : `7,5`.
- Noms de fonctions en français (tableau ci-dessous). Un utilisateur dont Excel est en anglais utilise la colonne anglaise et la virgule `,` comme séparateur.
- Texte entre guillemets droits : `"Oui"`. Critère de comparaison entre guillemets : `">"&B2`, `"<>"&""`.
- Références absolues avec `$` quand la formule est recopiée : `$B$2`.
- Dans un tableau Excel (Ctrl+L), préférer les références structurées : `=SOMME.SI.ENS(Temps[Heures];Temps[Projet];[@Projet])`.

## Correspondance des fonctions courantes
| Français | Anglais | Usage |
|---|---|---|
| SOMME | SUM | Somme |
| SOMME.SI / SOMME.SI.ENS | SUMIF / SUMIFS | Somme sous condition(s) |
| NB / NBVAL / NB.VIDE | COUNT / COUNTA / COUNTBLANK | Compter nombres / non vides / vides |
| NB.SI / NB.SI.ENS | COUNTIF / COUNTIFS | Compter sous condition(s) |
| MOYENNE / MOYENNE.SI.ENS | AVERAGE / AVERAGEIFS | Moyenne |
| SI / SI.CONDITIONS | IF / IFS | Condition |
| ET / OU / NON | AND / OR / NOT | Logique |
| SIERREUR | IFERROR | Remplacer une erreur |
| RECHERCHEX | XLOOKUP | Recherche (Excel 365 / 2021) |
| RECHERCHEV | VLOOKUP | Recherche (versions anciennes) |
| INDEX / EQUIV | INDEX / MATCH | Recherche souple (toutes versions) |
| FILTRE / TRIER / UNIQUE | FILTER / SORT / UNIQUE | Tableaux dynamiques (365) |
| SUPPRESPACE | TRIM | Retirer les espaces parasites |
| MAJUSCULE / MINUSCULE / NOMPROPRE | UPPER / LOWER / PROPER | Casse |
| CNUM / DATEVAL | VALUE / DATEVALUE | Texte → nombre / date |
| TEXTE | TEXT | Mise en forme (`TEXTE(A2;"jj/mm/aaaa")`) |
| AUJOURDHUI / MAINTENANT | TODAY / NOW | Date du jour |
| NB.JOURS.OUVRES | NETWORKDAYS | Jours ouvrés entre deux dates |
| MOIS.DECALER / FIN.MOIS | EDATE / EOMONTH | Décaler / fin de mois |
| ARRONDI / ARRONDI.SUP | ROUND / ROUNDUP | Arrondis |
| CONCAT / JOINDRE.TEXTE | CONCAT / TEXTJOIN | Assembler du texte |
| SOUS.TOTAL | SUBTOTAL | Total qui ignore les lignes filtrées |

## Exemples prêts à coller (cas Triskell)
- Heures d'un projet : `=SOMME.SI.ENS(Temps!F:F;Temps!C:C;A2)`
- Heures facturables d'un projet sur octobre 2026 : `=SOMME.SI.ENS(Temps!F:F;Temps!C:C;A2;Temps!G:G;"Oui";Temps!A:A;">="&DATE(2026;10;1);Temps!A:A;"<"&DATE(2026;11;1))`
- Jours consommés (hypothèse 7 h / jour, en C1) : `=SOMME.SI.ENS(Temps!F:F;Temps!C:C;A2)/$C$1`
- Taux de consommation : `=SIERREUR(C2/B2;"")` puis format pourcentage
- Alerte de dépassement : `=SI(C2>B2;"Dépassement";SI(C2>0,8*B2;"À surveiller";"OK"))`
- Jours vendus d'un projet depuis la feuille Budget : `=RECHERCHEX(A2;Budget!A:A;Budget!B:B;"introuvable")` · avant Excel 2021 : `=SIERREUR(INDEX(Budget!B:B;EQUIV(A2;Budget!A:A;0));"introuvable")`
- Nettoyer un nom avant recherche : `=SUPPRESPACE(A2)`
- Convertir « 7,5 » texte en nombre : `=CNUM(F2)` ; une date texte « 04/09/2026 » : `=DATEVAL(A2)`

## Expliquer une formule (format de réponse)
1. Ce qu'elle calcule, en une phrase.
2. Chaque argument, dans l'ordre, en mots simples.
3. Un exemple chiffré sur une ligne du fichier.
4. Ce qui peut la faire échouer.

## Erreurs fréquentes et cause probable
| Erreur | Cause probable | Correction |
|---|---|---|
| `#N/A` | Valeur cherchée absente : espace en trop, casse, nombre stocké en texte | `SUPPRESPACE`, `CNUM`, vérifier la table de référence |
| `#VALEUR!` | Texte dans un calcul (« 7,5 » en texte, date en texte) | `CNUM` / `DATEVAL`, ou convertir la colonne |
| `#NOM?` | Fonction en anglais dans un Excel français (ou l'inverse), guillemets typographiques | Traduire la fonction, remplacer « » par " |
| `#DIV/0!` | Division par zéro ou cellule vide | `SIERREUR(…;"")` |
| `#REF!` | Ligne ou colonne référencée supprimée | Refaire la référence |
| `#PROPAGATION!` (`#SPILL!`) | Formule dynamique bloquée par des cellules non vides | Vider la zone de sortie |
| Résultat 0 inattendu | Critère texte qui ne correspond pas (espace, casse, accent) | Comparer avec `=EXACT(A2;Budget!A2)` |
| Formule affichée au lieu du résultat | Cellule au format Texte | Format Standard, puis F2 + Entrée |
| Séparateur refusé | `,` au lieu de `;` en français | Remplacer par `;` |
