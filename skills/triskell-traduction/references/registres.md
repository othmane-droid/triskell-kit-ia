# Registres et mise en forme par type de document

## Le registre selon le document
| Type | Registre | Règles |
|---|---|---|
| **Contrat, CGV, DPA, annexe juridique** | Juridique, littéral | Phrase par phrase, aucune reformulation, mêmes numéros d'articles ; « shall » pour une obligation (anglais) ; termes définis (avec majuscule) traduits toujours pareil ; mention « traduction de travail, seule la version [langue] fait foi » ; relecture juridique obligatoire |
| **Réponse d'appel d'offres, questionnaire sécurité** | Formel, précis | Pas d'adaptation : chaque engagement garde sa portée exacte (« peut » ≠ « doit ») ; conserver la numérotation des exigences |
| **Réponse support, article d'aide** | Clair, direct, poli | Phrases courtes, impératif pour les étapes (« Click **Export** ») ; noms de menus et de boutons **identiques à l'interface de la langue cible** : s'ils ne sont pas connus, garder le libellé source entre crochets et le signaler |
| **Mail client** | Courtois, professionnel | Anglais : « Dear Ms Martin » (formel) ou « Hello Claire » si le fil est au prénom ; formules de fin : « Kind regards » ; allemand : « Sie », « Sehr geehrte Frau … » ; espagnol : « usted », « Estimada Sra. … » |
| **Marketing (site, post, newsletter, plaquette)** | Vivant, adapté | Adaptation autorisée (accroche, rythme, jeux de mots remplacés) ; aucun fait, chiffre ou promesse ajouté ; titres anglais en « sentence case » (« Prioritise your portfolio », pas « Prioritise Your Portfolio ») sauf charte contraire |
| **Présentation** | Concis | Même nombre de puces, titres-messages courts ; signaler les textes qui risquent de déborder (l'anglais est souvent plus court, l'allemand plus long de 20 à 30 %) |
| **Interface (UI), libellés, messages d'erreur** | Neutre, court | Voir ci-dessous |
| **Document interne** | Neutre | Sigles internes expliqués une fois entre parenthèses |

## Chaînes d'interface (UI)
- **Longueur** : respecter la limite donnée (caractères, espaces compris). Sans limite donnée : viser ± 20 % de la longueur source et signaler tout dépassement de plus de 30 %.
- **Variables et balises intactes** : `{0}`, `{count}`, `%s`, `%d`, `{{name}}`, `<b>…</b>`, `\n`. Leur ordre peut changer si la grammaire l'exige, jamais leur forme.
- **Cohérence** : un même bouton porte le même nom partout (Enregistrer → Save, toujours).
- **Pluriels** : signaler les chaînes qui dépendent d'un nombre (« 1 projet / 2 projets ») si la clé ne gère pas le pluriel.
- **Majuscules** : boutons et menus en majuscule initiale seule (« Export timesheets »), sauf convention de l'interface existante.
- **Abréviations** : seulement si la limite l'impose, et dans la liste « À vérifier ».
- Format de livraison : tableau `Clé | Source | Traduction | Longueur / limite | Statut`.

## Mise en forme à conserver
- Titres, niveaux de titres, listes à puces et numérotées, tableaux, gras / italique, liens (texte traduit, URL inchangée sauf version localisée connue).
- Nombres : FR `1 800,50` → EN `1,800.50` → DE `1.800,50` → ES `1.800,50`.
- Dates : FR `13/11/2026` → EN UK `13 November 2026` (ou `13/11/2026`) → EN US `November 13, 2026` (ou `11/13/2026`) → DE `13.11.2026` → ES `13/11/2026`. Écrire le mois en lettres dans les documents engageants pour éviter toute confusion jour / mois.
- Heures : FR `12h00` → EN `12:00 (noon)` / `12 pm` (US) → DE `12:00 Uhr` → ES `12:00 h`.
- Montants : la devise et le HT / TTC restent (« € excl. VAT »). Jamais de conversion de devise.
- Noms propres, sigles produits, noms d'outils internes : inchangés.

## Signaler plutôt que deviner
À mettre dans « À vérifier » : terme Triskell absent du glossaire · phrase source ambiguë (deux lectures possibles : donner les deux) · jeu de mots ou expression sans équivalent · référence culturelle ou juridique française (SYNTEC, OPCO, URSSAF, CGV) · libellé d'interface dont la traduction officielle n'est pas connue · « vous » collectif ou individuel en allemand / espagnol si le destinataire est flou.
