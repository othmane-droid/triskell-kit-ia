# Test du skill `triskell-synthese-documents` (données fictives)

> DOCUMENT FICTIF : résultat produit en appliquant le skill aux fichiers de test. Aucune donnée réelle.
> Demande testée : « Voici les 4 documents sur le compte Alpha. Fais-moi une synthèse pour ma direction, puis une version pour l'équipe projet. »
> Fichiers joints : `demo2-cr-copil-alpha-2026-09-12.docx`, `demo2-echanges-mail-alpha.docx`, `demo2-note-interne-alpha.docx`, `demo3-transcription-teams-alpha-2026-10-08.docx`.
> Les documents de test n'ont pas de numéros de page : les ancres utilisent les sections, les dates de mail et les minutes de la transcription.

Sources (noms courts) : `[CR-12/09]` compte rendu du COPIL du 12/09/2026 · `[Mails]` échanges du 22/09 au 29/09/2026 · `[Note interne]` note CSM du 01/10/2026 · `[Transcription]` point de suivi Teams du 08/10/2026.

---

## 1. Mode Direction

**Synthèse direction · Compte Groupe Alpha Industrie · 19/10/2026**
Lecteur : direction · Sources : CR-12/09, Mails, Note interne, Transcription

**L'essentiel en 5 lignes**
1. Le contrat arrive à échéance le 31/12/2026, et la sponsor veut présenter le renouvellement à son comité de direction début novembre [CR-12/09, § Points abordés ; Mails, 29/09].
2. La consolidation du reporting prend encore plus de 20 minutes le lundi, et deux chefs de projet sont repassés sur Excel [Transcription, 00:41].
3. Le responsable PMO a écrit qu'il regarderait d'autres solutions au renouvellement si la situation ne s'améliore pas [Mails, 22/09].
4. Correctif annoncé : mise en production le 22/10 si le client valide la recette du 20 ou 21/10, avant sa clôture trimestrielle du 30/10 [Transcription, 02:05-02:51].
5. 60 % des chefs de projet saisissent chaque semaine, pour un objectif de 80 % [CR-12/09 ; Transcription, 03:10].

**Ce que j'en conclus**
- Le renouvellement dépend du correctif : s'il n'est pas en production avant le 30/10, le PMO arrivera au comité client avec un argument contre nous (lignes 2 à 4).
- La sponsor demandera un gain chiffré (« la direction financière va me demander des chiffres sur le gain réel » [Transcription, 05:10]) : le bilan avant / après doit être prêt avant le COPIL.

**Points d'attention**
- Recette client le 20 ou 21/10, mise en production le 22/10 : aucune marge avant le 30/10.
- Deux explications différentes de la lenteur circulent (voir les contradictions) : à clarifier avant d'annoncer un résultat.
- Date du COPIL : le 15/10 prévu en septembre a glissé vers la semaine du 16/11.

**Décision attendue** : aucune décision de la direction à ce stade. À suivre : la mise en production du 22/10.

---

## 2. Mode Opérationnel

**Synthèse opérationnelle · Compte Groupe Alpha Industrie · 19/10/2026**
Lecteur : équipe projet (CSM, consultant) · Sources : CR-12/09, Mails, Note interne, Transcription

**1. Ce que disent les documents**
- *Contrat* : échéance au 31/12/2026 ; la sponsor (Claire Martin) veut une proposition de renouvellement [CR-12/09, § Points abordés], avec une option de formation pour les chefs de projet qui utilisent peu l'outil [Mails, 29/09].
- *Performance* : lenteurs du reporting depuis juillet, surtout le lundi matin [CR-12/09] ; consolidation de plus de 20 min « ce lundi » [Mails, 22/09] et encore « lundi dernier » [Transcription, 00:41].
- *Cause et correctif* : version 8.4 prévue le 20/10 (calcul de consolidation non optimisé au-delà de 300 projets) [Mails, 24/09] ; paramétrage limitant le recalcul des 3 tableaux de bord aux deux dernières années, test « la semaine prochaine », production le 22/10 si Julien valide [Transcription, 01:20-02:30]. Gain estimé « par trois ou quatre », non testé [Transcription, 01:20].
- *Adoption* : 60 % d'utilisateurs hebdomadaires ; objectif 80 % à fin décembre [Transcription, 03:10]. Les nouveaux arrivants n'ont jamais été formés [Transcription, 03:40].
- *Évolution* : demande d'un connecteur ERP pour remonter les coûts réels ; chiffrage à faire [CR-12/09, § Prochaines étapes].

**2. Actions et échéances**
| Action | Responsable | Échéance | Source |
|---|---|---|---|
| Paramétrage sur l'environnement de test | Marc Dupuis | « la semaine prochaine » (dit le 08/10) | Transcription, 02:30 |
| Recette avec deux chefs de projet | Julien Roche | 20 ou 21/10 | Transcription, 02:51 |
| Mise en production | à préciser | 22/10, si recette validée | Transcription, 02:30 |
| Proposer 2 dates de session de prise en main (1 h, à distance) | Sarah Benali | « d'ici la fin de semaine » (dit le 08/10) | Transcription, 04:02 |
| Envoyer la liste des champs obligatoires | Julien Roche | à préciser | Transcription, 04:52 |
| Rédiger le mode opératoire d'une page | Marc Dupuis | à préciser | Transcription, 04:40 |
| Bilan d'usage avec temps de consolidation avant / après | à préciser (« on ») | avant le COPIL | Transcription, 05:35 |
| Sondage de dates pour le COPIL | Sarah Benali | à préciser | Transcription, 06:05 |
| Chiffrage du connecteur ERP | Nova (personne à préciser) | à préciser | CR-12/09 |
| Proposition de renouvellement (avec option formation) | à préciser | avant le comité de direction client début novembre | Mails, 29/09 |

**3. Ce que j'en conclus**
- Risque **élevé** sur le renouvellement : menace écrite du PMO [Mails, 22/09] et note interne « moyen à élevé » [Note interne, § Niveau de risque].
- Risque **moyen** sur le planning : la recette tient sur deux personnes et un ou deux jours ; aucun plan B n'est écrit.
- Ce que je ferais en premier : faire confirmer par l'équipe technique laquelle des deux corrections part le 22/10, puis caler le bilan avant / après sur cette correction.

**4. Questions ouvertes**
- Équipe technique : la version 8.4 et le paramétrage des tableaux de bord sont-ils deux corrections distinctes ou la même ?
- Sarah Benali : le COPIL du 15/10 a-t-il eu lieu ? Aucun document ne le dit.
- Direction commerciale : qui porte la proposition de renouvellement, et pour quelle date exacte ?

---

## 3. Contradictions et écarts entre documents

| Sujet | Source A dit | Source B dit | Fait foi (et pourquoi) | Qui tranche |
|---|---|---|---|---|
| Cause de la lenteur | Calcul de consolidation non optimisé au-delà de 300 projets [Mails, 24/09] | 3 tableaux de bord recalculent l'historique depuis 2021 [Transcription, 01:20] | Aucune : un écrit plus ancien contre un oral plus récent. Les deux causes peuvent coexister | Équipe technique |
| Correctif et date | Version 8.4 le 20/10 [Mails, 24/09] | Paramétrage, production le 22/10 si recette validée [Transcription, 02:30] | À clarifier : deux objets différents ou un seul | Équipe technique, puis CSM vers le client |
| Date du prochain COPIL | 15/10/2026 [CR-12/09 ; Note interne, § Actions] | Semaine du 16/11, sondage à envoyer [Transcription, 06:05] | Transcription (plus récente), mais la date n'est pas fixée | CSM avec la sponsor |
| Objectif d'adoption | 80 %, « fixé en janvier », sans échéance [CR-12/09] | 80 % à fin décembre, « objectif du COPIL de septembre » [Transcription, 03:10] | CR-12/09 (écrit), à compléter par l'échéance donnée à l'oral | CSM |
| Délai de la proposition de renouvellement | « avant le prochain comité » [CR-12/09], « avant le comité du 15/10 » [Note interne] | Présentation au comité de direction client « début novembre » [Mails, 29/09] | Mail de la sponsor (plus récent, écrit par la décisionnaire) | Direction commerciale |

## 4. À préciser
1. Qui porte la mise en production du 22/10 (Marc Dupuis ou l'équipe technique) ? (DSC)
2. Date exacte du comité de direction client de novembre. (Sarah Benali, auprès de Claire Martin)
3. Le chiffrage du connecteur ERP a-t-il été fait ? (avant-vente)

---

## Version Client (extrait du test du mode Client)

**Point d'étape · Groupe Alpha Industrie · 19/10/2026**

Bonjour Madame Martin,
Voici ce que nous retenons de notre point du 8 octobre et de nos échanges de septembre.

**Ce que nous retenons**
- La consolidation du reporting reste trop longue le lundi ; un paramétrage des tableaux de bord est prévu (référence : point du 8 octobre).
- La recette est prévue le 20 ou le 21 octobre avec deux chefs de projet, pour une mise en production le 22 octobre si elle est validée.
- Une session de prise en main d'une heure, à distance, est proposée aux nouveaux arrivants, avec un mode opératoire d'une page.

**Prochaines étapes**
| Étape | Qui | Quand |
|---|---|---|
| Liste des champs obligatoires | Julien Roche | à confirmer |
| Bilan d'usage (temps de consolidation avant / après) | Nova | avant le COPIL |
| Sondage de dates pour le COPIL | Sarah Benali | semaine du 16 novembre visée |

**Points à confirmer ensemble** : la date de votre comité de direction de novembre.

**À garder en interne (non repris dans la version client)** : niveau de risque sur le renouvellement et menace concurrentielle [Note interne ; Mails, 22/09] ; opportunité « module de gestion des ressources » [Note interne, § Opportunité] ; écart entre les deux explications de la lenteur (à clarifier avant d'en parler au client).

---

Synthèse à relire avant diffusion : vérifiez les chiffres et les noms dans les sources citées.

## Ce que le test a révélé (corrigé dans le skill)
- Les fichiers Word n'ont pas de pages : la convention d'ancre accepte maintenant section, date de mail et minute (`gabarits.md`).
- La date « mail 22/09 » parle de « ce lundi » : le skill doit dater les faits relatifs (« lundi dernier ») par rapport au document, sans inventer de date. Règle ajoutée dans `controle-qualite.md` (§ 5).
- Une action de la transcription avait une échéance relative (« d'ici la fin de semaine ») : elle est restituée telle quelle, avec la semaine du document entre parenthèses.
