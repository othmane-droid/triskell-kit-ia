# Bibliothèque de prompts Triskell

12 demandes prêtes à copier dans ChatGPT. Remplacez ce qui est [entre crochets], joignez vos documents, envoyez.
Chaque prompt est suivi d'un cas d'usage à essayer avec les fichiers fictifs du dossier `exemples/fichiers-de-test/`. Dans ces fichiers fictifs, l'éditeur s'appelle « Nova Software » : il joue le rôle de Triskell.

## La recette d'un bon prompt

1. **Qui je suis** : Votre rôle et le contexte : « Je suis chef de projet chez Triskell, éditeur de logiciels PPM. »
2. **Ce que je joins** : Les documents. ChatGPT ne sait que ce que vous lui donnez, ou ce qu'il trouve sur le web.
3. **Ce que je veux** : La tâche, en un verbe : synthétiser, rédiger, comparer, classer.
4. **Pour qui, sous quelle forme** : Le lecteur, la longueur, le format : tableau, 3 lignes, mail de 150 mots.
5. **Les règles** : Ce qu'il ne doit pas faire : inventer, promettre une date, changer le fond.

## 01. Synthétiser un document

*Synthèses · Fondamentaux*

**Quand :** Un contrat, un appel d'offres, un rapport ou un long fil de mails à comprendre vite.  
**À joindre :** Le ou les documents.

```text
Je suis [votre rôle, ex. chef de projet chez Triskell Software, éditeur de logiciels PPM].
Je te joins [le document : compte rendu, contrat, rapport, cahier des charges].
Fais-en une synthèse pour [le lecteur : ma direction / l'équipe projet / le client].

Format :
1. L'essentiel en 3 lignes.
2. Les points clés (5 maximum), chacun avec la section ou la page d'où il vient.
3. Ce qui demande une décision ou une action : quoi, qui, quand (si c'est écrit).
4. Ce qui manque ou n'est pas clair.

Règles : n'ajoute rien qui ne soit pas dans le document. Si une information manque, écris « non précisé ». Sépare ce que dit le document de ton interprétation.
```

**Et ensuite :** « Refais-la en 5 lignes pour un dirigeant qui a 30 secondes. »

### Cas d'usage 01

**La situation :** Vous reprenez le compte Groupe Alpha Industrie. Votre direction veut savoir en 5 minutes où en est le client.

**Fichiers :** demo2-cr-copil-alpha-2026-09-12.docx, demo2-echanges-mail-alpha.docx, demo2-note-interne-alpha.docx

```text
Je suis CSM chez Nova Software, éditeur de logiciels PPM.
Je te joins 3 documents sur le compte Groupe Alpha Industrie : le compte rendu du COPIL du 12/09, les échanges de mails de septembre et une note interne.
Fais-en une synthèse pour ma direction.

Format :
1. L'essentiel en 3 lignes.
2. Les points clés (5 maximum), chacun avec le document d'où il vient.
3. Ce qui demande une décision ou une action : quoi, qui, quand (si c'est écrit).
4. Ce qui manque ou n'est pas clair.

Règles : n'ajoute rien qui ne soit pas dans les documents. Si une information manque, écris « non précisé ». Sépare ce que disent les documents de ton interprétation.
```

**Ce que vous devez retrouver :**

- Le contrat arrive à échéance le 31/12/2026.
- Le responsable PMO a évoqué la concurrence par écrit le 22/09.
- Le correctif des lenteurs (v8.4) est prévu le 20/10, après le COPIL du 15/10 : une bonne synthèse le relève.
- L'adoption est à 60 % des chefs de projet pour un objectif de 80 %.

## 02. Compte rendu d'une réunion Teams + mail de suivi

*Comptes rendus · Fondamentaux*

**Quand :** Juste après une réunion client ou interne enregistrée.  
**À joindre :** La transcription Teams (ou vos notes).

```text
Voici la transcription de notre réunion [type : COPIL client / atelier / point interne] du [date].
Participants : [noms et rôles].

Rédige le compte rendu :
- Objet (1 ligne)
- Décisions prises
- Actions, en tableau : Action | Responsable | Échéance
- Points ouverts et risques
- Prochaine réunion

Règles : uniquement ce qui a été dit. Responsable ou date non dits = « à préciser ». Ne transforme pas une proposition (« on pourrait ») en décision. Mets à part, sous « À garder en interne », ce qui ne doit pas partir chez le client.

Ensuite, propose le mail de suivi au client : vouvoiement, 150 mots maximum, 2 objets au choix.
```

**Et ensuite :** « Pour chaque action du compte rendu, cite le passage de la transcription qui la justifie. »

### Cas d'usage 02

**La situation :** Vous sortez d'un point de suivi Teams avec le client Alpha. Le compte rendu doit partir ce soir.

**Fichiers :** demo3-transcription-teams-alpha-2026-10-08.docx

```text
Voici la transcription de notre point de suivi client du 8 octobre 2026.
Participants : Claire Martin (DSI, Groupe Alpha Industrie), Julien Roche (responsable PMO, Alpha), Sarah Benali (CSM, Nova Software), Marc Dupuis (consultant, Nova Software).

Rédige le compte rendu :
- Objet (1 ligne)
- Décisions prises
- Actions, en tableau : Action | Responsable | Échéance
- Points ouverts et risques
- Prochaine réunion

Règles : uniquement ce qui a été dit. Responsable ou date non dits = « à préciser ». Ne transforme pas une proposition (« on pourrait ») en décision. Mets à part, sous « À garder en interne », ce qui ne doit pas partir chez le client.

Ensuite, propose le mail de suivi au client : vouvoiement, 150 mots maximum, 2 objets au choix.
```

**Ce que vous devez retrouver :**

- La validation est attendue avant la clôture trimestrielle du client, le 30/10.
- La mise en production du 22/10 est conditionnée à la validation de Julien Roche : ce n'est pas une date ferme.
- Le gain « divisé par trois ou quatre » est une estimation prudente, pas un engagement : il ne doit pas apparaître comme une promesse dans le mail.
- La réunion a duré 32 minutes mais la transcription s'arrête avant : la réponse devrait le signaler.

## 03. Répondre à un mail (même difficile)

*Mails · Fondamentaux*

**Quand :** Une réponse à écrire, une réclamation, un refus, un retard à annoncer.  
**À joindre :** Le mail et le fil précédent (copiés-collés).

```text
Voici un mail reçu de [client / prospect / collègue], avec le fil précédent :
[coller le fil]

Ce que je veux répondre, en quelques mots : [ex. « on accepte, mais pas avant novembre »].

Propose 3 versions : courte (60 mots), standard (150 mots), ferme mais courtoise.
Vouvoiement pour un client. Propose 2 objets.

Règles : ne promets aucune date, aucun prix, aucune fonctionnalité que je n'ai pas indiqués. Si une information me manque, écris [à compléter].
```

**Et ensuite :** « Prends la version standard et rends-la plus chaleureuse, sans la rallonger. »

### Cas d'usage 03

**La situation :** Le client vous écrit dimanche soir qu'il refuse la mise en production de jeudi sans recette. Vous devez répondre lundi matin.

**Fichiers :** demo7-boite-mail-fictive.docx

```text
Voici un mail reçu de Julien Roche, client (Groupe Alpha Industrie) : c'est le mail M1 du document joint.

Ce que je veux répondre, en quelques mots : « vous avez raison, pas de mise en production sans recette ; on décale, nouvelle date à caler avec notre consultant ».

Propose 3 versions : courte (60 mots), standard (150 mots), ferme mais courtoise.
Vouvoiement. Propose 2 objets.

Règles : ne promets aucune date, aucun prix, aucune fonctionnalité que je n'ai pas indiqués. Si une information me manque, écris [à compléter].
```

**Ce que vous devez retrouver :**

- La réponse commence par reconnaître l'inquiétude du client, avant toute explication.
- Aucune nouvelle date n'est inventée : elle est en [à compléter].
- La version « ferme » reste courtoise et ne remet pas la faute sur le client.

## 04. Trier sa boîte et préparer sa journée

*Mails · Fondamentaux*

**Quand :** Le matin, ou au retour d'une absence.  
**À joindre :** Vos mails copiés-collés, ou le connecteur Outlook s'il est activé dans votre espace.

```text
Voici mes derniers mails [coller, ou : regarde ma boîte Outlook des dernières 24 heures].

Classe-les dans un tableau : Mail | De qui | Catégorie | Ce qu'on attend de moi (1 ligne)
Catégories : À traiter aujourd'hui · Peut attendre · À déléguer (à qui) · Pour info.

Termine par les 3 priorités de ma journée, dans l'ordre.

Règles : ne réponds à aucun mail, ne supprime et ne déplace rien.
```

**Et ensuite :** « Rédige un brouillon de réponse pour les 3 mails « À traiter aujourd'hui ». »

### Cas d'usage 04

**La situation :** Lundi 19 octobre, 8 h 30 : 9 mails vous attendent. Par quoi commencer ?

**Fichiers :** demo7-boite-mail-fictive.docx

```text
Voici mes derniers mails (document joint). Nous sommes le lundi 19 octobre 2026, je suis CSM.

Classe-les dans un tableau : Mail | De qui | Catégorie | Ce qu'on attend de moi (1 ligne)
Catégories : À traiter aujourd'hui · Peut attendre · À déléguer (à qui) · Pour info.

Termine par les 3 priorités de ma journée, dans l'ordre.

Règles : ne réponds à aucun mail, ne supprime et ne déplace rien.
```

**Ce que vous devez retrouver :**

- M1 (recette refusée par le client) est dans les priorités du jour.
- M2 (prix du renouvellement) est à traiter, mais sans donner de prix : la fourchette se demande en interne.
- M4 (newsletter) est « pour info », pas une priorité.
- Un mail rendu obsolète par un mail plus récent du même client est repéré.

## 05. Préparer une présentation

*Présentations · Fondamentaux*

**Quand :** Un COPIL, une soutenance, un point direction, une formation.  
**À joindre :** La matière : compte rendu, chiffres, documents.

```text
Je dois présenter [sujet] à [public] le [date], en [durée] minutes.
Objectif : [la décision ou le message attendu].
Matière jointe : [documents].

Étape 1 seulement : propose le déroulé en [8] slides.
Pour chaque slide : un titre qui dit la conclusion (pas « Contexte », mais « Le projet a 3 semaines de retard à cause des données »), 3 puces maximum, et la source de chaque chiffre.

Attends ma validation avant de rédiger le contenu complet.
```

**Et ensuite :** « C'est validé : génère le PowerPoint avec le skill « Design system Triskell ». »

### Cas d'usage 05

**La situation :** Vous préparez le point d'avancement à présenter au client Alpha lors du prochain COPIL.

**Fichiers :** demo2-cr-copil-alpha-2026-09-12.docx, demo3-transcription-teams-alpha-2026-10-08.docx

```text
Je dois présenter le point d'avancement du projet à Claire Martin (DSI) et Julien Roche (responsable PMO) de Groupe Alpha Industrie, lors du prochain COPIL, en 30 minutes.
Objectif : faire valider le plan d'action sur les lenteurs du reporting et sur l'adoption.
Matière jointe : le compte rendu du COPIL du 12/09 et la transcription du point du 08/10.

Étape 1 seulement : propose le déroulé en 8 slides.
Pour chaque slide : un titre qui dit la conclusion (pas « Contexte », mais « Le reporting prend encore plus de 20 minutes le lundi »), 3 puces maximum, et la source de chaque chiffre.

Attends ma validation avant de rédiger le contenu complet.
```

**Ce que vous devez retrouver :**

- Chaque titre est une phrase qui dit quelque chose, pas un thème (« Performance », « Adoption »).
- Les chiffres (60 % d'adoption, plus de 20 minutes) ont leur source.
- ChatGPT s'arrête au déroulé et attend votre validation.
- Nous n'avons volontairement pas joint la note interne : rien sur le risque de renouvellement ne doit apparaître.

## 06. Analyser un fichier Excel

*Excel · Fondamentaux*

**Quand :** Un export de temps, un suivi budgétaire, un tableau de licences à comprendre.  
**À joindre :** Le fichier Excel.

```text
Je te joins [le fichier]. Avant de répondre :
1. Décris le fichier : onglets, colonnes, nombre de lignes, et les anomalies (cases vides, doublons, formats incohérents).
2. Réponds ensuite à ma question : [ex. « quels projets dépassent leurs jours vendus ? »]
3. Montre le calcul et les hypothèses.
4. Propose un graphique utile.

Ne modifie pas mes données sans me le dire : liste chaque correction que tu fais.
```

**Et ensuite :** « Écris-moi la formule Excel en français (séparateur ;) pour refaire ce calcul moi-même, et explique-la en une phrase. »

### Cas d'usage 06

**La situation :** Le suivi des temps de septembre-octobre est arrivé. Quels projets ont déjà consommé plus que les jours vendus ?

**Fichiers :** demo5-suivi-temps-budget-fictif.xlsx

```text
Je te joins le suivi des temps et budgets (onglets Temps et Budget). Avant de répondre :
1. Décris le fichier : onglets, colonnes, nombre de lignes, et les anomalies (cases vides, doublons, formats incohérents).
2. Réponds ensuite à ma question : au 19/10/2026, quels projets dépassent leurs jours vendus ? Compte 1 jour = 7 heures, toutes les heures (facturables ou non), et seulement les saisies datées jusqu'au 19/10.
3. Montre le calcul et les hypothèses.
4. Propose un graphique utile.

Ne modifie pas mes données sans me le dire : liste chaque correction que tu fais.
```

**Ce que vous devez retrouver :**

- Il repère des anomalies : dates écrites en texte, un nom de projet écrit de plusieurs façons, un doublon, des saisies datées après le 19/10.
- Avec ces hypothèses, 2 projets sur 4 dépassent : Valbourg - Formation (environ 117 %) et Alpha - Déploiement (environ 103 %).
- Il dit quelles corrections il a faites, au lieu de nettoyer en silence.

## 07. Faire une veille concurrentielle

*Veille · Avancé*

**Quand :** Chaque semaine, ou avant un rendez-vous où un concurrent est en lice.  
**À joindre :** Rien : activez la recherche web (bouton « + »).

```text
Fais une veille sur [concurrents, ex. Planisware, Planview] sur les [30] derniers jours : nouveaux produits, annonces, partenariats, nominations, clients annoncés.

Pour chaque information : la date, la source avec le lien, et en une ligne pourquoi c'est important pour un éditeur de logiciels PPM.

Règles : uniquement des sources datées et vérifiables. Pas de rumeur. Si tu ne trouves rien de récent, dis-le simplement.
```

**Et ensuite :** « Transforme cette demande en tâche planifiée chaque lundi à 8 h. »

### Cas d'usage 07

**La situation :** Lundi matin, vous voulez savoir ce qui a bougé chez les concurrents ce mois-ci. Activez la recherche web.

**Fichiers :** aucun, tout est dans le prompt

```text
Fais une veille sur Planisware, Planview et Sciforma sur les 30 derniers jours : nouveaux produits, annonces, partenariats, nominations, clients annoncés.

Pour chaque information : la date, la source avec le lien, et en une ligne pourquoi c'est important pour un éditeur de logiciels PPM.

Règles : uniquement des sources datées et vérifiables. Pas de rumeur. Si tu ne trouves rien de récent, dis-le simplement.
```

**Ce que vous devez retrouver :**

- Chaque information a une date et un lien qui fonctionne : cliquez-en deux au hasard.
- Sciforma : le site renvoie vers Planview, qui l'a racheté, et le produit s'appelle désormais « Planview ProjectAdvantage » (vérifié le 19/10/2026).
- « Rien de nouveau » est une bonne réponse pour un concurrent calme. Une liste pleine sans liens ne l'est pas.

## 08. Répondre à un ticket support

*Support client · Fondamentaux*

**Quand :** Un ticket ou une question d'utilisateur à traiter.  
**À joindre :** Le ticket, et si possible la documentation ou des réponses passées.

```text
Voici un ticket client : [coller le ticket]

1. Classe-le : question d'usage, incident, bug supposé, demande d'évolution, facturation. Propose une priorité.
2. Rédige la réponse au client : vouvoiement, ton empathique, étapes numérotées s'il s'agit d'une manipulation.
3. Si besoin, rédige une note interne pour l'équipe technique : ce qu'on sait, comment reproduire, l'environnement concerné.

Règles : ne confirme pas un bug, ne promets ni date ni correctif. Toute information produit absente des documents joints = [à vérifier].
```

**Et ensuite :** « Ce ticket revient souvent : rédige un article d'aide court sur ce sujet. »

### Cas d'usage 08

**La situation :** Un client doit transmettre ses temps à la finance vendredi, et son export est incomplet.

**Fichiers :** demo2-tickets-support-fictifs.docx

```text
Voici un ticket client : c'est le ticket T-111 du document joint. Le même document contient nos tickets déjà résolus (T-101 à T-110) : sers-t'en comme base.

1. Classe-le : question d'usage, incident, bug supposé, demande d'évolution, facturation. Propose une priorité.
2. Rédige la réponse au client : vouvoiement, ton empathique, étapes numérotées s'il s'agit d'une manipulation.
3. Si besoin, rédige une note interne pour l'équipe technique : ce qu'on sait, comment reproduire, l'environnement concerné.

Règles : ne confirme pas un bug, ne promets ni date ni correctif. Toute information produit absente des documents joints = [à vérifier].
```

**Ce que vous devez retrouver :**

- Il rapproche le ticket de deux cas connus : la limite de lignes de l'export (T-108) et les projets archivés exclus par défaut (T-102).
- Ce sont des pistes à vérifier avec le client, pas un diagnostic certain.
- L'échéance du client (vendredi) remonte la priorité, sans promesse de délai.

## 09. Analyser un appel d'offres avant de décider d'y aller

*Avant-vente · Avancé*

**Quand :** Un appel d'offres ou un cahier des charges vient d'arriver.  
**À joindre :** Le dossier de consultation (règlement, cahier des charges).

```text
Je te joins un appel d'offres. Fais-moi une fiche d'analyse :
- Acheteur, objet, dates clés (questions, remise), format de réponse attendu
- Critères de notation et leur poids
- Pièces à fournir
- Exigences éliminatoires
- Tableau des exigences : Exigence | Obligatoire ? | Page | Question à poser
- Les 5 questions à poser à l'acheteur

Ne rédige aucune réponse à ce stade : je veux d'abord décider si on y va. Indique la page de chaque information.
```

**Et ensuite :** « Pour chaque exigence, indique si nos documents joints y répondent : couvert, partiel, non couvert ou à vérifier. »

### Cas d'usage 09

**La situation :** Le Groupe Hélianthe Industrie publie une consultation PPM. Faut-il y aller ?

**Fichiers :** demo1-appel-offres-fictif.docx

```text
Je te joins un appel d'offres (consultation HI-2026-014, Groupe Hélianthe Industrie). Fais-moi une fiche d'analyse :
- Acheteur, objet, dates clés (questions, remise), format de réponse attendu
- Critères de notation et leur poids
- Pièces à fournir
- Exigences éliminatoires
- Tableau des exigences : Exigence | Obligatoire ? | Page | Question à poser
- Les 5 questions à poser à l'acheteur

Ne rédige aucune réponse à ce stade : je veux d'abord décider si on y va. Indique la page de chaque information.
```

**Ce que vous devez retrouver :**

- Remise des offres : vendredi 13 novembre 2026, 12 h. Questions écrites possibles jusqu'au 30/10.
- Critères : valeur technique 50 %, prix 35 %, accompagnement 15 %.
- 30 exigences, dont 21 obligatoires. Mémoire technique de 30 pages maximum.
- Point d'attention : la formation en espagnol est obligatoire, et un site pilote est demandé au plus tard le 01/02/2027.

## 10. Créer un document à partir d'un modèle

*Documents · Fondamentaux*

**Quand :** Un courrier, une note ou un mode opératoire à produire « comme d'habitude ».  
**À joindre :** Le modèle à suivre et le document source.

```text
Je te joins deux documents :
- le MODÈLE : la structure et le ton à respecter ;
- la SOURCE : les informations à utiliser.

Rédige un nouveau [courrier / note / mode opératoire] qui suit exactement la structure du modèle, avec uniquement les informations de la source.
Ce qui manque : écris [à préciser].

À la fin, liste ce que tu as repris tel quel, ce que tu as reformulé et ce qui reste à compléter.
```

**Et ensuite :** « Vérifie qu'aucun nom, chiffre ou date du modèle d'origine n'est resté dans le nouveau document. »

### Cas d'usage 10

**La situation :** L'acheteuse d'Hélianthe demande des précisions avant le 20/10. Vous avez les informations internes et votre modèle de courrier.

**Fichiers :** demo4-courrier-helianthe-et-modele.docx

```text
Le document joint contient 3 parties :
1. le courrier reçu d'Hélianthe (la demande) ;
2. nos informations internes (la SOURCE) ;
3. notre modèle de courrier (le MODÈLE : structure et ton à respecter).

Rédige la réponse à Isabelle Moreau en suivant exactement la structure du modèle, avec uniquement les informations de la source.
Ce qui manque : écris [à préciser].

À la fin, liste ce que tu as repris tel quel, ce que tu as reformulé et ce qui reste à compléter.
```

**Ce que vous devez retrouver :**

- Les 3 questions reçoivent une réponse, dans l'ordre du courrier.
- Les chiffres sont identiques à la source : 10 à 12 semaines (pilote de 4 semaines), 3 sessions de 2 heures par profil, export Excel et CSV sous 30 jours.
- Le lieu, la date ou le signataire manquants sont en [à préciser], pas inventés.

## 11. Traduire un texte professionnel

*Traduction · Fondamentaux*

**Quand :** Une réponse à un client étranger, une page produit, un extrait d'appel d'offres.  
**À joindre :** Le texte, et votre glossaire s'il existe.

```text
Traduis ce texte en [anglais / espagnol / allemand] pour [un client / le support / le site web / un contrat].

Garde la mise en forme. Garde tels quels les noms propres et ces termes : [liste].
Utilise le vocabulaire usuel de la gestion de projets et de portefeuille (portfolio, resource capacity, timesheet…).

À la fin, liste en 3 puces maximum les choix de traduction discutables.

[coller le texte]
```

**Et ensuite :** « Relis ta traduction comme un client natif : qu'est-ce qui sonne traduit ? »

### Cas d'usage 11

**La situation :** Une cliente britannique a le même problème d'export. Vous avez la réponse en français, il faut l'envoyer en anglais.

**Fichiers :** aucun, tout est dans le prompt

```text
Traduis ce texte en anglais britannique pour une cliente (réponse du support).

Garde la mise en forme. Garde tels quels les noms de menus : Temps, Export, Période, Inclure les projets archivés.
Utilise le vocabulaire usuel de la gestion de projets et de portefeuille (portfolio, resource capacity, timesheet…).

À la fin, liste en 3 puces maximum les choix de traduction discutables.

Bonjour Madame Durand,
Merci pour votre message. L'export des temps est limité à 10 000 lignes par fichier : au-delà, le fichier s'arrête, ce qui explique l'absence du second semestre.
Pour obtenir l'année complète :
1. Dans le menu Temps, ouvrez Export.
2. Réglez le filtre Période sur le premier trimestre, puis lancez l'export.
3. Répétez l'opération pour chaque trimestre.
Si des projets terminés manquent encore, cochez Inclure les projets archivés avant l'export.
Bien cordialement,
L'équipe support
```

**Ce que vous devez retrouver :**

- Les noms de menus restent en français, comme demandé.
- « 10 000 » devient « 10,000 » et « Madame Durand » devient « Ms Durand ».
- « Export des temps » est traduit avec le vocabulaire du métier (timesheet), pas mot à mot.

## 12. Relire et clarifier un texte

*Documents · Fondamentaux*

**Quand :** Avant d'envoyer un mail important, une proposition, une note.  
**À joindre :** Le texte.

```text
Relis ce texte destiné à [destinataire].
Corrige l'orthographe et la grammaire, puis rends-le plus clair et plus court, sans changer le fond.

Donne-moi la version corrigée, puis en 3 puces ce que tu as changé.
N'ajoute aucune information.

[coller le texte]
```

**Et ensuite :** « Quelle phrase risque d'être mal comprise par le destinataire ? Propose une alternative. »

### Cas d'usage 12

**La situation :** Votre mail à une cliente part dans 5 minutes. Un dernier coup d'œil.

**Fichiers :** aucun, tout est dans le prompt

```text
Relis ce texte destiné à une cliente, Claire Martin (DSI).
Corrige l'orthographe et la grammaire, puis rends-le plus clair et plus court, sans changer le fond.

Donne-moi la version corrigée, puis en 3 puces ce que tu as changé.
N'ajoute aucune information.

Bonjour Claire,
Suite a notre échange de mardi, je vous confirme que nous avons bien prit en compte votre demande concernant la formation des chef de projets. Nous revenons vers vous dés que possible avec une proposition, sachant que on doit d'abord valider en interne le périmètre exacte et les modalités, ce qui peut prendre un peu de temps compte tenu du contexte actuel.
N'hésitez pas à revenir vers moi si besoin.
Cordialement,
Sarah
```

**Ce que vous devez retrouver :**

- Les fautes sont corrigées : « à », « pris », « chefs de projet », « dès », « qu'on », « exact ».
- « Dès que possible » ne devient pas une date (« sous 48 heures ») : aucune information ajoutée.
- Le mail est plus court et garde le vouvoiement.

## 5 relances qui améliorent n'importe quelle réponse

1. « Avant de commencer, pose-moi les questions dont tu as besoin. »
2. « Qu'est-ce qui, dans ta réponse, ne vient pas de mes documents ? »
3. « Plus court : 5 lignes, pour quelqu'un qui a 30 secondes. »
4. « Donne-moi 3 options vraiment différentes. »
5. « Transforme ce que tu viens de faire en consignes réutilisables (pour un projet ou un skill). »

## 3 règles

- **Relecture humaine** : Tout ce qui part chez un client est relu par une personne. Chiffres et noms en premier.
- **Le bon espace** : Les documents réels de Triskell vont dans l'espace ChatGPT Business de Triskell, jamais dans un compte personnel.
- **Les crochets** : Remplacez tout ce qui est [entre crochets] avant d'envoyer le prompt.
