# Exemple fictif : « Quels projets dépassent leur budget en jours ? »

> Fichier fictif `demo5-suivi-temps-budget-fictif.xlsx` (feuilles Lisez-moi, Temps, Budget). Date de référence : 19/10/2026.

**La réponse en 3 lignes**
Au 19/10/2026, 2 projets sur 4 dépassent leurs jours vendus : Valbourg - Formation (9,36 j consommés pour 8 vendus, 117 %) et Alpha - Déploiement (20,57 j pour 20, 103 %). Orion (50 %) et Hélianthe (36 %) restent dans leur budget. Avec les saisies déjà datées après le 19/10, Alpha atteindrait 114 % et Valbourg 123 %.

**Le fichier en bref** : feuille Temps = une saisie d'heures par ligne (75 lignes, du 02/09 au 26/10/2026) ; feuille Budget = jours vendus et TJM pour 4 projets ; clé commune : le nom du projet.

**Comment c'est calculé** : jours consommés = somme des heures du projet ÷ 7 ; consommation = jours consommés ÷ jours vendus. En Excel : `=SOMME.SI.ENS(Temps!F:F;Temps!C:C;A2;Temps!A:A;"<="&DATE(2026;10;19))/7`, puis `=C2/B2`.

**Décisions de nettoyage**
| Décision | Lignes | Avant → après |
|---|---|---|
| D1-D2 Nom de projet harmonisé | 7, 24 | « Alpha - Déploiement␣ », « alpha - déploiement » → « Alpha - Déploiement » |
| D3 Dates en texte converties | 5, 19, 42 | « 04/09/2026 » → date |
| D4 Nombre en texte converti | 32 | « 7,5 » → 7,5 |
| D5 Variantes de Oui | 14, 28 | oui, O → Oui (O = Oui : à confirmer) |
| D6 Doublon exact retiré | 63 | ligne retirée |
| D7-D10 Signalé, non corrigé, exclu du calcul | 37 (-4 h), 46 (75 h), 52 (projet vide), 66-76 (dates après le 19/10) | inchangé, colonne Contrôle |

**Hypothèses à confirmer** : 1 jour = 7 h ; le non facturable consomme le budget ; les saisies après le 19/10 sont du prévisionnel.
**Limites** : le fichier ne contient pas de reste à faire : on sait ce qui est consommé, pas ce qui reste à produire.
**Fichier** : copie avec Synthèse (3 tableaux, 3 graphiques natifs), Données nettoyées, Journal des corrections (9 modifications, 14 lignes signalées) ; feuilles d'origine intactes.

Vérifiez 2 ou 3 chiffres dans le fichier d'origine avant de diffuser.
