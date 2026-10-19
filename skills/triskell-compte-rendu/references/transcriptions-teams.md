# Lire une transcription Teams sans se tromper

> Une transcription n'est pas un compte rendu : elle contient des hésitations, des phrases coupées, des erreurs de reconnaissance vocale et des accords implicites. Ce guide liste les pièges et la conduite à tenir.

## 1. Les formats que tu vas recevoir
| Format | Reconnaître | Lire |
|---|---|---|
| Export Word de Teams (.docx) | Nom du locuteur, puis horodatage `0:41` ou `00:00:41`, puis le texte | Une intervention = nom + heure + paragraphe |
| Fichier .vtt | Lignes `00:00:41.000 --> 00:00:47.500` et balises `<v Prénom Nom>` | Ignore les numéros de bloc et les heures de fin ; regroupe les blocs consécutifs du même locuteur |
| Texte collé | `[00:41] Prénom Nom : texte` ou `Prénom Nom 0:41` | Idem |
| Résumé Copilot ou « notes de réunion » Teams | Puces déjà rédigées, « Tâches de suivi » | Source secondaire : vérifie chaque décision et chaque tâche dans la transcription si elle est fournie. Sans transcription, écris en tête du CR « Rédigé à partir du résumé automatique, non vérifié » |
| Notes manuscrites ou prises à la volée | Mots-clés, abréviations | Ne complète pas les phrases au-delà de ce que les notes permettent ; « à préciser » sinon |

## 2. Les locuteurs
- **Rattache chaque nom à sa société et à son rôle** à partir de l'en-tête, de l'invitation ou de l'adresse mail. Un participant sans rôle connu reste « (fonction à préciser) ».
- **« Utilisateur inconnu », « Invité », un numéro de téléphone, « Salle de réunion 3 »** : ne devine pas qui parle. Si le contenu permet d'identifier la personne sans ambiguïté (« moi, en tant que DSI… »), indique-le ; sinon garde « un participant [société si connue] » et ajoute une question dans « À vérifier avant envoi ».
- Une salle de réunion partagée par plusieurs personnes produit un seul locuteur pour plusieurs voix : ne prête pas une décision à une personne précise sur cette base.
- Le prénom seul (« Julien ») renvoie à la liste des participants ; deux personnes du même prénom : signale-le.

## 3. Horodatage
- Sers-t'en pour prouver une décision ou une action (dans ta grille de travail ou dans le CR interne), pas dans le CR client.
- Un trou de plusieurs minutes, une transcription qui commence après 0:00 ou qui s'arrête net : la réunion n'est peut-être pas entière. Écris-le dans « À vérifier avant envoi ».
- Dernier horodatage très inférieur à la durée annoncée (ex. 06:24 pour 32 min) : la transcription est peut-être incomplète ou l'enregistrement a été coupé. Signale-le dans « À vérifier avant envoi », ne recalcule pas la durée.

## 4. Paroles qui se chevauchent et accords implicites
- « Oui », « d'accord », « ça marche », « parfait » : cherche **à quelle proposition** la personne répond (l'intervention juste avant, en général). Si deux propositions se suivent, l'accord porte sur la dernière.
- **Un accord ne vaut décision que s'il vient de quelqu'un qui peut décider** (sponsor, DSI, responsable PMO pour son périmètre). Le « oui » d'un participant sans autorité sur le sujet reste un avis.
- Un accord sous condition (« ça me va, mais il faut que ce soit validé avant le 30 ») : la condition fait partie de la décision.
- Phrases coupées, reprises, « euh », bruits : ignore-les. Ne reconstruis jamais une phrase coupée en lui donnant un sens.
- Deux personnes parlent en même temps et la transcription mélange : garde l'information seulement si elle est confirmée plus loin.

## 5. Mots mal transcrits
- Noms propres, sigles et noms de produits sont les plus touchés. Exemples possibles : un nom d'outil interne transcrit phonétiquement, un sigle épelé (« d. s. c. »), un nom de client déformé.
- **Ne corrige pas au hasard.** Si le contexte rend la correction certaine (le mot figure correctement ailleurs dans la transcription ou dans un document joint), corrige. Sinon, garde le mot entre guillemets et liste-le dans « À vérifier avant envoi ».
- Chiffres : « vingt » et « trente » se confondent rarement, mais « 15 » et « 50 » si. Un chiffre qui change une décision se vérifie.

## 6. Dates relatives
Convertis à partir de la date de la réunion et garde la trace :
- « lundi dernier » le jeudi 08/10 → lundi 05/10 ;
- « la semaine prochaine » → semaine du lundi suivant ;
- « d'ici la fin de semaine » → le vendredi de la même semaine ;
- « avant le COPIL » → la date du COPIL si elle est connue, sinon « avant le prochain COPIL (date à fixer) ».
Si la date de la réunion est inconnue, ne convertis pas : garde l'expression entre guillemets et demande la date.

## 7. Langue et registre
- Les participants se tutoient parfois en réunion : le CR client vouvoie toujours.
- Un échange en anglais se résume en français, sauf les termes que le client emploie lui-même.
- Garde les mots du client pour ses besoins et ses irritants (« la consolidation prend plus de vingt minutes »), sans les adoucir ni les dramatiser.
