# Test du skill `triskell-emails` (données fictives)

> DOCUMENT FICTIF : résultat produit en appliquant le skill aux fichiers de test. Aucune donnée réelle.
> Fichiers : `demo7-boite-mail-fictive.docx` (9 mails, sans connecteur Outlook : mode « mails collés ») ; contexte du fil : `demo2-echanges-mail-alpha.docx`, `demo3-transcription-teams-alpha-2026-10-08.docx`.
> Utilisatrice simulée : Sarah Benali, CSM. Date du test : lundi 19/10/2026.

---

## Test 1 · Mode Trier : « Trie ma boîte, qu'est-ce qui est urgent ? »

**Tri du 19/10/2026 · 9 mails**

| # | De | Objet | Catégorie | Urgence | Action proposée | Échéance écrite |
|---|---|---|---|---|---|---|
| M1 | Julien Roche (client Alpha) | Recette du correctif : on n'est pas prêts | À traiter | Urgent | Répondre aujourd'hui ; caler la décision sur la mise en production avec le consultant | Mise en production « jeudi 22 » |
| M7 | Support (interne) | [T-111] Export des temps incomplet | À déléguer (support) + à traiter | Urgent | Répondre au support : oui pour être en copie ; le support répond au client | Chiffres du client à transmettre « vendredi » |
| M2 | Claire Martin (client Alpha) | Renouvellement : prix ? | À traiter + à déléguer (direction commerciale pour le prix) | Urgent (renouvellement) | Accuser réception sans prix ; demander la fourchette à la direction commerciale | Comité de direction client « début novembre » |
| M5 | Marc Dupuis (interne) | Mode opératoire nouveaux arrivants | À traiter | Cette semaine | Relancer Julien Roche pour la liste des champs obligatoires | aucune |
| M3 | Isabelle P. (ADV) | Facture Alpha septembre : bon de commande ? | À traiter | Cette semaine | Répondre à l'ADV (numéro de BDC ou accord pour relancer la compta client) | aucune |
| M6 | Isabelle Moreau (achats Hélianthe) | Report de la soutenance | Pour info | Quand possible | Aucune ; la direction commerciale est en copie | Soutenance du 22/10 reportée, nouvelle date non donnée |
| M8 | RH | Rappel : entretiens annuels | Pour info | Quand possible | Planifier ses entretiens | 30/11 |
| M9 | Julien Roche | Démo du correctif | À archiver | — | Dépassé par M1 | aucune |
| M4 | Newsletter PPM Hebdo | Les 5 tendances PPM de l'automne | À archiver | — | — | aucune |

**Les 3 à traiter en premier**
1. **M1** : mise en production dans 3 jours sans recette possible, client déjà irrité (fil de septembre).
2. **M7** : un client doit transmettre ses chiffres vendredi.
3. **M2** : la sponsor prépare son comité ; une absence de réponse serait mal lue, mais le prix ne peut pas venir de nous seuls.

**Fils liés** : M1, M5 et M9 (compte Alpha, correctif et adoption) ; M2 (renouvellement Alpha).

---

## Test 2 · Mode Difficile : réponse à M1

**Le fil en 2 lignes** : Julien Roche refuse une mise en production le 22/10 sans recette, faute de testeur cette semaine. Il a été dit le 08/10 que la production du 22/10 se ferait « si Julien valide » [transcription, 02:30], et la sponsor veut la correction avant le 30/10 [transcription, 02:05].

**Analyse (non incluse dans le mail)**
1. Ce qu'il veut : ne pas porter seul le risque d'une mise en production ratée ; être écouté.
2. Ce qu'on peut dire : la mise en production était conditionnée à sa recette (déjà dit) ; on peut proposer d'organiser la recette autrement.
3. Ce qu'on ne doit pas dire : une nouvelle date de production ou une date de recette non validée par le consultant ; une garantie de résultat.

**À compléter avant envoi**
- `[à compléter : créneaux de recette possibles]` : Marc Dupuis.
- `[à compléter : nouvelle date de mise en production]` : à décider avec Marc Dupuis, compatible avec la clôture du client le 30/10.

**Objets proposés** : 1. « RE: Recette du correctif : on n'est pas prêts » · 2. « Alpha · Recette du correctif · nouveaux créneaux » · 3. « Alpha · Mise en production décalée après votre recette »

**Variante courte**
> Bonjour Julien,
> Vous avez raison : pas de mise en production sans votre recette, comme convenu le 8 octobre. Je vous propose de nouveaux créneaux d'ici [à compléter : date] et je vous appelle aujourd'hui pour en parler.
> Bien cordialement,
> Sarah Benali

**Variante standard**
> Bonjour Julien,
> Merci de nous avoir prévenus. Nous ne passerons pas en production sans votre recette : c'était la condition fixée lors de notre point du 8 octobre, et elle reste valable.
> Pour tenir votre clôture du 30 octobre, je vous propose deux pistes :
> - une recette avec un seul chef de projet, accompagné par Marc Dupuis, sur l'un de ces créneaux : [à compléter : créneaux] ;
> - une mise en production décalée au [à compléter : date], après votre recette.
> Pouvez-vous me dire laquelle vous convient ? Je peux aussi vous appeler aujourd'hui si c'est plus simple.
> Bien cordialement,
> Sarah Benali, Customer Success Manager

**Variante ferme**
> Bonjour Julien,
> Nous ne passerons pas en production sans votre recette : c'est la condition convenue le 8 octobre.
> En revanche, décaler la recette au-delà du [à compléter : date limite] ne permettrait plus de tenir votre clôture du 30 octobre. Pour garder cette échéance, nous avons besoin d'un testeur de votre côté sur l'un de ces créneaux : [à compléter : créneaux]. Marc Dupuis l'accompagnera pour limiter le temps à y consacrer.
> Merci de me confirmer un créneau d'ici [à compléter : date].
> Bien cordialement,
> Sarah Benali, Customer Success Manager

Brouillon à relire : rien n'a été envoyé.

---

## Test 3 · Mode Répondre : M2 (demande de prix)

**Le fil en 2 lignes** : Claire Martin demande une idée du prix du renouvellement avec l'option formation, même une fourchette, pour son comité de direction de début novembre. Aucun prix n'a été communiqué par écrit dans le fil.

**À compléter avant envoi** : `[à compléter : date d'envoi de la proposition]` (direction commerciale). **Aucun prix ni aucune fourchette dans le brouillon** : le skill ne s'engage pas sur un prix non fourni.

**Objets proposés** : 1. « RE: Renouvellement : prix ? » · 2. « Alpha · Proposition de renouvellement avant votre comité »

**Variante standard**
> Bonjour Claire,
> Merci pour votre message. Je préfère vous transmettre des éléments chiffrés justes plutôt qu'une fourchette approximative : la proposition de renouvellement, avec l'option de formation pour les chefs de projet, vous parviendra le [à compléter : date], avant votre comité de début novembre.
> Pour l'ajuster au mieux, pouvez-vous me confirmer la date de ce comité ?
> Bien cordialement,
> Sarah Benali

(Variantes courte et ferme produites sur le même modèle ; non reproduites ici.)

Brouillon à relire : rien n'a été envoyé.

---

## Test 4 · Mode Relancer : liste des champs obligatoires (suite de M5)

**Le fil en 2 lignes** : le 08/10, Julien Roche a dit « Je te l'envoie » pour la liste des champs obligatoires [transcription, 04:52] ; Marc Dupuis ne l'a toujours pas le 16/10.

**Objets proposés** : 1. « Alpha · Mode opératoire nouveaux arrivants · liste des champs » · 2. « Liste des champs obligatoires pour le mode opératoire »

**Relance n°1 (à envoyer aujourd'hui, de préférence après la réponse à M1, ou à intégrer dans celle-ci)**
> Bonjour Julien,
> Je reviens vers vous au sujet du mode opératoire d'une page pour les nouveaux arrivants, évoqué lors de notre point du 8 octobre. Pour le finaliser, Marc Dupuis a besoin de la liste de vos champs obligatoires. Pourriez-vous nous l'adresser quand vous le pourrez ?
> Bien cordialement,
> Sarah Benali

**Relance n°2** (5 jours ouvrés plus tard sans réponse) : une seule question fermée : « Pouvez-vous nous transmettre la liste des champs obligatoires d'ici [à compléter : date] ? Sans elle, le mode opératoire ne pourra pas être remis aux nouveaux arrivants. »

---

## Ce que le test a révélé (corrigé dans le skill)
- Un mail récent peut rendre un autre mail obsolète (M9 dépassé par M1) : ajout de la consigne « fils liés » et du cas « dépassé » dans `tri-boite.md`.
- La relance de M5 tombe le même jour qu'une réponse délicate au même client : le skill doit proposer de **regrouper** plutôt que d'envoyer deux mails le même jour à un client irrité. Règle ajoutée dans `redaction.md`.
- La demande de prix (M2) a confirmé la règle : aucune fourchette, même « indicative ».
