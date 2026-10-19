# Modèles de sortie : compte rendu et mail de suivi

> Format exact à reproduire. Les crochets `[…]` sont à remplacer ; un champ inconnu devient « à préciser ». Si Triskell joint son propre modèle de CR, sa mise en forme remplace celle-ci, mais les règles de contenu restent.

## 1. CR client

```
Compte rendu · [Type de réunion : point de suivi, COPIL, kick-off…] · [Nom du client] · [JJ/MM/AAAA]
Rédigé par [prénom nom, fonction] · Diffusion : participants [+ autres destinataires si précisés]

Participants
- [Client] : [Prénom Nom (fonction)], [Prénom Nom (fonction)]
- Triskell : [Prénom Nom (fonction)], [Prénom Nom (fonction)]
- Excusés : [noms, ou « aucun »]

1. Objet de la réunion
[Une à deux lignes : pourquoi on s'est réunis.]

2. Ce que nous avons décidé
- [Décision formulée comme un fait, avec sa condition s'il y en a une]
- […]

3. Actions
| N° | Action | Responsable | Échéance |
|---|---|---|---|
| 1 | [Verbe à l'infinitif + objet] | [Prénom Nom (société)] | [JJ/MM ou « à préciser »] |

4. Points ouverts
- [Question ou condition à lever, et qui doit y répondre]

5. Prochaine réunion
[Type, date ou période, ou « à fixer »]
```

Règles du CR client :
- **Décisions** : 3 à 7 au maximum. Au-delà, regroupe par sujet avec un intertitre (« Performance », « Adoption »).
- **Actions** : une ligne par action, une personne par ligne. Une action à deux porteurs se découpe en deux lignes.
- **Échéance** : date au format JJ/MM ; « semaine du JJ/MM » si la réunion n'a fixé qu'une semaine ; « à préciser » sinon. Jamais « ASAP ».
- Les actions du client et celles de Triskell figurent dans le même tableau : le CR engage les deux parties.
- Pas d'horodatage dans le CR client.

## 2. CR interne

```
CR interne · [Objet] · [JJ/MM/AAAA]
Participants : [Prénom Nom (rôle : DC, DSC, CSM, DP, ADV, Support…)]

En bref (3 lignes maximum)
[La conclusion de la réunion, ce qui change.]

Décisions
- […]

Actions
| Action | Responsable | Échéance |
|---|---|---|

Risques et signaux
- [Risque] · niveau [élevé / moyen / faible] · [action proposée]

Points ouverts
- […]
```
Le CR interne peut citer l'horodatage d'un propos important (`[12:40]`), nommer les concurrents évoqués et parler du renouvellement. Il ne contient pas de jugement personnel sur un collègue ou un client.

## 3. CR d'atelier (paramétrage, conception)

```
Compte rendu d'atelier · [Thème de l'atelier] · [Nom du client] · [JJ/MM/AAAA]
Participants : [comme le CR client]

1. Objectif de l'atelier
2. Ce qui est validé
| Sujet | Règle ou choix retenu | Validé par |
|---|---|---|
3. Ce qui reste à valider
| Sujet | Options discutées | Qui tranche | Pour quand |
|---|---|---|---|
4. Données et documents attendus
| Document ou donnée | Fourni par | Pour quand |
|---|---|---|
5. Actions
| N° | Action | Responsable | Échéance |
6. Prochain atelier : [thème, date ou « à fixer »]
```
Règle propre à l'atelier : une règle de gestion ou un choix de paramétrage n'est « validé » que si le client l'a dit explicitement. Sinon il va dans « Ce qui reste à valider ». N'écris jamais comment le produit se paramètre si ce n'est pas dit dans la réunion ou dans la documentation jointe : « [à vérifier dans la doc Triskell] ».

## 4. Mail de suivi Outlook (après un CR client ou d'atelier)

```
Objet (option 1) : [Client] · CR [type de réunion] du [JJ/MM] et prochaines étapes
Objet (option 2) : [Le message principal en moins de 60 caractères, ex. « Reporting : mise en production prévue le 22/10 »]

Bonjour [Prénom ou Madame, Monsieur],

Merci pour [la réunion / vos retours] du [JJ/MM].

Vous trouverez ci-dessous [ou : en pièce jointe] le compte rendu. Les points principaux :
- [Décision 1]
- [Décision 2]
- [Décision 3, facultative]

Prochaines étapes :
- [Action] · [Responsable] · [Échéance]
- [Action] · [Responsable] · [Échéance]

[Une phrase sur la prochaine réunion.]
N'hésitez pas à me signaler toute correction d'ici le [JJ/MM].

Bien cordialement,
[Prénom Nom]
[Fonction] · Triskell Software
```
Règles du mail :
- 150 mots maximum hors CR, vouvoiement, aucun contenu de « À garder en interne ».
- Seulement les 3 décisions et les 3 à 5 actions les plus importantes ; le détail est dans le CR.
- La dernière phrase avant la formule de politesse donne au client un délai pour corriger : c'est ce qui rend le CR opposable.
- Destinataires suggérés : participants en « À », sponsor en « Cc » s'il était absent. **Ne propose jamais d'ajouter quelqu'un qui n'est pas cité dans les sources.**

## 5. Message Teams (après un CR interne)
```
CR [objet] du [JJ/MM] · [lien ou pièce jointe]
Décidé : [1 ligne]
À faire : @[Prénom] [action] pour le [JJ/MM] · @[Prénom] [action] pour le [JJ/MM]
Point ouvert : [1 ligne, ou rien]
```
