# Bibliothèque de prompts Triskell

12 demandes prêtes à copier dans ChatGPT. Remplacez ce qui est [entre crochets], joignez vos documents, envoyez.

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
