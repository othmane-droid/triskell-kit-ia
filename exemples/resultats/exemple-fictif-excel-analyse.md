# Test du skill `triskell-excel-analyse` (données fictives)

> DOCUMENT FICTIF : résultat produit en appliquant le skill au fichier de test. Aucune donnée réelle.
> Fichier : `exemples/fichiers-de-test/demo5-suivi-temps-budget-fictif.xlsx` (créé pour ce test, avec 10 anomalies volontaires).
> Demande testée : « Quels projets risquent de dépasser leur budget en jours ? Fais-moi une synthèse pour le COPIL. »
> Fichier produit : `exemple-fictif-excel-analyse.xlsx` (feuilles Synthèse, Lisez-moi, Temps, Budget, Données nettoyées, Journal des corrections).

## Étape 1 · Profil (`scripts/profil_excel.py`)
Anomalies détectées par le script, sans rien modifier : 3 dates en texte (lignes 5, 19, 42) · 1 projet vide (52) · 3 variantes du nom « Alpha - Déploiement » dont une avec espace final (7) · 1 nombre en texte « 7,5 » (32) · 1 valeur négative (37) · 1 valeur > 5 × la médiane, 75 h (46) · Oui / oui · 1 doublon exact (63) · 11 dates postérieures au 19/10 (66 à 76).
Non détecté automatiquement : « O » pour « Oui » (variante de sens, pas d'écriture) ; repéré à la lecture des valeurs distinctes de la colonne.

## Étape 2 · Question reformulée et hypothèses
Consommation = (heures saisies jusqu'au 19/10 ÷ 7) ÷ jours vendus. Hypothèses posées, marquées « à confirmer » : 1 jour = 7 h ; le non facturable compte ; les saisies datées après le 19/10 sont du prévisionnel.

## Étape 3 · Réponse livrée (extrait)
Au 19/10/2026, **2 projets sur 4 dépassent leurs jours vendus** : Valbourg - Formation (117 %) et Alpha - Déploiement (103 %). Avec les saisies datées après le 19/10 : Alpha 114 %, Valbourg 123 %. Orion 50 %, Hélianthe 36 % (41 % si la ligne de 75 h valait 7,5 h).

| Projet | Jours vendus | Jours consommés au 19/10 | Consommation |
|---|---|---|---|
| Valbourg - Formation | 8 | 9,36 | 117 % |
| Alpha - Déploiement | 20 | 20,57 | 103 % |
| Orion - Paramétrage | 15 | 7,50 | 50 % |
| Hélianthe - Pilote | 25 | 9,07 | 36 % |

Contrôle croisé : 144 + 65,5 + 63,5 + 52,5 = 325,5 h = total des heures retenues ; 75 lignes − 1 doublon = 74 lignes nettoyées, dont 14 signalées (3 anomalies + 11 dates futures) et 60 retenues.

## Étape 4 · Copie propre (`scripts/copie_propre.py` + `references/exemple-spec.json`)
Sortie du script : « 74 lignes nettoyées · 9 modification(s) journalisée(s) · 14 ligne(s) signalée(s) ».
Vérification automatique après génération : feuilles Lisez-moi, Temps et Budget **identiques à la source** cellule par cellule ; 3 graphiques natifs dans la Synthèse (barres vendus vs consommés, barres horizontales par projet, camembert par activité).

## Test du mode Aide formule
Demande : « Écris-moi la formule qui affiche "Dépassement" si un projet a consommé plus que ses jours vendus, "À surveiller" au-delà de 80 %. »
Réponse : `=SI(C2>B2;"Dépassement";SI(C2>0,8*B2;"À surveiller";"OK"))` (B2 = jours vendus, C2 = jours consommés). Lecture : si le consommé dépasse le vendu → « Dépassement » ; sinon, s'il dépasse 80 % du vendu → « À surveiller » ; sinon « OK ». Exemple ligne Orion : 7,5 > 0,8 × 15 = 12 ? non → « OK ». Excel en anglais : `=IF(C2>B2,"Dépassement",IF(C2>0.8*B2,"À surveiller","OK"))`.

## Ce que le test a révélé (corrigé dans le skill)
- Les **dates futures** dans un fichier de réalisé n'étaient pas détectées : ajout de la détection au profil (uniquement pour les colonnes qui mélangent passé et futur, pour ne pas signaler une colonne d'échéances) et de la condition `futur` au script de copie.
- Un doublon exact peut être légitime (deux saisies identiques le même jour) : la méthode dit maintenant de le signaler au lieu de le retirer quand c'est plausible (`methode.md` § 2).
- La variante « O » n'est pas détectable par un script : la méthode impose de lire les valeurs distinctes des colonnes à faible cardinalité.
- Une feuille « Lisez-moi » d'une seule colonne était lue comme un tableau : le profil la traite désormais comme une feuille de texte.
