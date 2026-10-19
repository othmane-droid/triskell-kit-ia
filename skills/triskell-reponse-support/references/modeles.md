# Modèles de sortie du support

> Les crochets `[…]` sont à remplacer. Un nom d'interface absent des sources s'écrit « [à vérifier dans la doc Triskell] ». Si Triskell joint ses propres modèles de réponse, ils remplacent ceux-ci.

## 1. Fiche de qualification
```
Ticket [référence] · [Type] · Priorité proposée : [P1 à P4] ([raison en quelques mots])
Problème : [une phrase : qui, quoi, depuis quand, impact, échéance]
Ton : [ligne de la grille de ton]
Réponses existantes : [T-xxx : correspond / diffère sur…] · [doc : page]
Confiance : [élevée / moyenne / faible]
Escalade : [non / N2 / équipe technique / produit / ADV / CSM] · [condition]
```

## 2. Réponse au client, selon le type

**Objet** : `RE: [objet du client]` (on garde le fil) ; si nouveau message : `[Sujet] : [ce qu'on apporte]`.

**Solution connue (question d'usage, paramétrage)**
```
Bonjour [Madame / Monsieur / Prénom],

[Une phrase qui montre qu'on a compris la demande.]

Pour [résultat voulu] :
1. [Étape, avec le nom exact de l'option tel qu'il figure dans la source]
2. [Étape]
3. [Étape]

[Si besoin : ce que l'administrateur doit faire, et pourquoi.]

Pouvez-vous nous confirmer que [résultat attendu] ?

Bien cordialement,
[Signature support]
```

**Plusieurs causes possibles (incident)**
```
Bonjour [ ],

Merci pour votre message[, nous avons bien noté votre échéance du JJ/MM].

[Une phrase : ce symptôme correspond le plus souvent à deux causes que vous pouvez vérifier tout de suite.]

1. [Cause la plus probable] : [comment la vérifier] → [comment la contourner]
2. [Cause suivante] : [vérification] → [contournement]

Si le problème persiste, pouvez-vous nous indiquer :
- [information 1]
- [information 2]
Nous reprendrons alors l'analyse en priorité.

Bien cordialement,
```

**Bug supposé (escaladé)**
```
Bonjour [ ],

Merci pour ces précisions. Nous avons transmis le comportement que vous décrivez à notre équipe technique pour analyse.
[Si un contournement est connu : En attendant, vous pouvez … ]
Nous revenons vers vous dès que nous avons son retour.
```
Interdit : « c'est un bug connu », « ce sera corrigé dans la prochaine version », toute date.

**Demande d'évolution**
```
Merci pour cette suggestion : [reformulation du besoin en une phrase].
Nous l'avons transmise à notre équipe produit[, avec le contexte de votre usage].
[Si une solution existe aujourd'hui dans la documentation : En attendant, … ]
```
Interdit : « c'est prévu », « c'est dans la roadmap », sauf document produit joint qui le dit et accord du CSM.

**Facturation et contrat**
```
Merci pour votre message. Je le transmets à [notre administration des ventes / votre responsable de compte], qui reviendra vers vous directement.
```

## 3. Note interne d'escalade
```
NOTE INTERNE · [Ticket] · [Client ou instance] · [date]
Type : [ ] · Priorité proposée : [ ] · Escalade vers : [N2 / technique / produit / ADV / CSM]
Résumé : [2 lignes]

Contexte technique
- Instance : [production / bac à sable / à demander au client]
- Version : [ / à demander]
- Utilisateur : profil [ ], droits [ ] (pas de nom si inutile)
- Volume : [lignes, projets, période]

Reproduire
1. [étape]
2. [étape]
Résultat attendu : [ ]
Résultat obtenu : [ ]
Fréquence : [ ] · Depuis : [ ] · Changement récent : [ ]

Hypothèses (à vérifier)
- [H1] · fondée sur [T-xxx / doc] · comment la confirmer
- [H2] · …

Déjà fait / répondu au client : [ ]
Informations manquantes : [ ] (à demander au client)
Échéance métier du client : [date, ex. clôture vendredi]
Signal produit : [récurrence, demande d'évolution associée, ou rien]
```

## 4. Article d'aide proposé
```
Titre : [Verbe d'action + résultat, ex. « Obtenir un export des temps complet sur une longue période »]
Pour qui : [utilisateur / administrateur]
Résumé : [2 lignes : le symptôme et la solution]

Symptôme
[Ce que l'utilisateur voit, avec ses mots.]

Causes et solutions
| Si… | Alors… |
|---|---|
| [cause 1] | [solution 1] |

À savoir : [limite ou règle par défaut, avec sa source]
Tickets à l'origine : [T-xxx, T-yyy] (à retirer avant publication)
Statut : brouillon à valider par [support / produit] avant publication
```
Règles : aucune donnée client, aucun nom de personne ou de société, chaque comportement décrit vient d'une source citée ; ce qui n'en a pas reste « [à vérifier dans la doc Triskell] ».
