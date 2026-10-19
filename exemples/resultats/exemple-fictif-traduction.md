# Test du skill `triskell-traduction` (données fictives)

> DOCUMENT FICTIF : résultat produit en appliquant le skill à des textes fictifs. Aucune donnée réelle. Les noms de menus sont inventés (voir `demo2-tickets-support-fictifs.docx` : « les réponses ne reflètent pas la documentation réelle du produit »).
> 3 tests : (1) réponse support FR → EN ; (2) chaînes d'interface FR → EN et FR → DE avec limites de longueur ; (3) extrait d'appel d'offres FR → EN (`demo1-appel-offres-fictif.docx`, page 7).

---

## Test 1 · Réponse support FR → EN (registre : support, client)

**Source**
> Bonjour Madame Durand,
> Merci pour votre message. L'export des temps est limité à 10 000 lignes par fichier : au-delà, le fichier s'arrête, ce qui explique l'absence du second semestre.
> Pour obtenir l'année complète :
> 1. Dans le menu **Temps**, ouvrez **Export**.
> 2. Réglez le filtre **Période** sur le premier trimestre, puis lancez l'export.
> 3. Répétez l'opération pour chaque trimestre.
> Si des projets terminés manquent encore, cochez **Inclure les projets archivés** avant l'export.
> Bien cordialement,
> L'équipe support

**Traduction (anglais britannique)**
> Dear Ms Durand,
> Thank you for your message. Timesheet exports are limited to 10,000 rows per file: beyond that limit, the file stops, which is why the second half of the year is missing.
> To get the full year:
> 1. In the **[Temps]** menu, open **[Export]**.
> 2. Set the **[Période]** filter to the first quarter, then run the export.
> 3. Repeat for each quarter.
> If completed projects are still missing, tick **[Inclure les projets archivés]** before exporting.
> Kind regards,
> The Support team

**Choix de traduction**
| Terme source | Traduction retenue | Pourquoi | Alternative |
|---|---|---|---|
| Bonjour Madame Durand | Dear Ms Durand | Client, premier échange formel | Hello Ms Durand |
| export des temps | timesheet exports | Glossaire : feuille de temps = timesheet | time entry export |
| second semestre | second half of the year | Plus naturel que « second semester » (scolaire) | H2 |
| 10 000 | 10,000 | Format anglais | — |
| cochez | tick | Anglais britannique | check (US) |
| Bien cordialement | Kind regards | Formule standard | Best regards |

**À vérifier**
1. Libellés **Temps**, **Export**, **Période**, **Inclure les projets archivés** : la traduction officielle de l'interface anglaise n'est pas connue ; gardés en français entre crochets. À remplacer par les libellés exacts de l'interface en anglais.
2. Variante d'anglais : britannique par défaut ; à confirmer selon le client.

---

## Test 2 · Chaînes d'interface (registre : UI)

**FR → EN**
| Clé | Source | Traduction | Longueur / limite | Statut |
|---|---|---|---|---|
| export.timesheets | Exporter les feuilles de temps | Export timesheets | 17 / 24 | OK |
| export.includeArchived | Inclure les projets archivés | Include archived projects | 25 / 28 | OK |
| selection.count | {0} projets sélectionnés | {0} projects selected | 21 / 25 | OK, variable intacte ; pluriel à vérifier (« 1 projects ») |
| export.tooManyRows | La période sélectionnée dépasse 10 000 lignes. Réduisez la période. | The selected period exceeds 10,000 rows. Please shorten the period. | 67 / 80 | OK |
| rule.validate | Valider la Rule | Validate [Rule] | 15 / 16 | À vérifier : terme Triskell + sens de « valider » |

**FR → DE (sur demande)**
| Clé | Source | Traduction | Longueur / limite | Statut |
|---|---|---|---|---|
| export.timesheets | Exporter les feuilles de temps | Zeiten exportieren | 18 / 24 | OK après raccourci : « Zeitnachweise exportieren » (25) dépassait |
| export.includeArchived | Inclure les projets archivés | Inkl. archivierter Projekte | 27 / 28 | Abréviation « Inkl. » imposée par la limite : à valider |
| selection.count | {0} projets sélectionnés | {0} Projekte ausgewählt | 23 / 25 | OK ; pluriel à vérifier |
| export.tooManyRows | (idem) | Der gewählte Zeitraum überschreitet 10.000 Zeilen. Bitte Zeitraum verkürzen. | 76 / 80 | OK |
| rule.validate | Valider la Rule | [Rule] validieren | 17 / 16 | **Dépassement** : longueur finale dépend du terme officiel |

**À vérifier**
1. « Rule » : terme Triskell marqué « [à compléter par Triskell] » dans le glossaire ; non traduit.
2. « Valider » : vérifier (validate) ou approuver (approve) ? Le libellé seul ne permet pas de trancher.
3. Le nombre « 10 000 » est écrit en dur dans la chaîne : s'il est formaté par l'application, le remplacer par une variable.
4. Les chaînes `selection.count` ne gèrent pas le singulier : prévoir une clé « 1 projet sélectionné ».

---

## Test 3 · Appel d'offres FR → EN (registre : formel, engagements à portée exacte)

| Source | Traduction |
|---|---|
| EX-27 (obligatoire) : La réponse doit comporter un mémoire technique de 30 pages maximum. | EX-27 (mandatory): The response shall include a technical proposal of no more than 30 pages. |
| EX-28 (obligatoire) : La réponse doit inclure une matrice de conformité reprenant chaque exigence numérotée. | EX-28 (mandatory): The response shall include a compliance matrix covering each numbered requirement. |
| EX-29 (obligatoire) : La proposition financière doit distinguer les coûts de licence, de mise en œuvre et de maintenance sur 3 ans. | EX-29 (mandatory): The financial proposal shall itemise licence, implementation and maintenance costs separately over 3 years. |
| EX-30 (souhaité) : Deux références clients dans l'industrie, de taille comparable, sont souhaitées. | EX-30 (desirable): Two customer references from the industrial sector, of comparable size, are desirable. |
| Critères de jugement : valeur technique 50 %, prix 35 %, qualité de l'accompagnement 15 %. | Award criteria: technical merit 50%, price 35%, quality of support and guidance 15%. |
| Les questions des candidats sont recevables jusqu'au 30 octobre 2026, par écrit uniquement. | Bidders' questions will be accepted until 30 October 2026, in writing only. |

**Choix de traduction**
| Terme source | Traduction retenue | Pourquoi | Alternative |
|---|---|---|---|
| doit (obligatoire) | shall | Obligation dans un document d'achat | must |
| souhaité | desirable | Distingue clairement d'une exigence obligatoire | preferred / nice to have (trop familier) |
| mémoire technique | technical proposal | Glossaire | technical response |
| critères de jugement | award criteria | Terme des marchés | evaluation criteria |
| 30 octobre 2026 | 30 October 2026 | Mois en lettres dans un document engageant | — |

**À vérifier**
1. « Accompagnement » : support (assistance) ou conduite du changement / formation ? Traduit « support and guidance » ; à préciser auprès de l'acheteur si la réponse est rédigée en anglais.
2. Mention à ajouter si ce texte circule : « Traduction de travail, sans valeur contractuelle ; seule la version française fait foi. »

Traduction à faire relire par un locuteur natif avant publication.

---

## Ce que le test a révélé (corrigé dans le skill)
- Les libellés d'interface cités dans une réponse support n'ont pas de traduction connue : la règle « garder entre crochets et signaler » est maintenant explicite dans `registres.md` (ligne support) et dans le SKILL (règle 1).
- La limite de longueur dépend parfois d'un terme encore inconnu (`[Rule]`) : le tableau UI indique alors « dépendant du terme officiel » au lieu d'un faux OK.
- Les chaînes au pluriel sans gestion du singulier sont un défaut de la source, pas de la traduction : à signaler à part (ajouté dans `registres.md`, § UI, « Pluriels »).
