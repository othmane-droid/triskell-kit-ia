# Exemple travaillé (FICTIF)

> Ticket et base de réponses inventés. Les comportements du produit décrits ici sont fictifs et ne reflètent pas la documentation Triskell.

## Entrées
**Base de tickets résolus (extrait)**
- R-21 · Un nouveau chef de projet ne voit pas son projet → son profil n'avait pas les droits sur l'entité du projet ; l'administrateur ajoute l'entité au profil.
- R-34 · Un utilisateur ne voit plus aucun projet après un changement de service → profil modifié par l'annuaire ; l'administrateur vérifie le profil.

**Nouveau ticket R-52** : « Depuis ce matin, aucun membre de mon équipe (8 personnes) ne voit les projets du programme Phénix. Le comité est jeudi. »

## Sorties attendues (extrait)

**Fiche de qualification**
R-52 · Paramétrage et droits · Priorité proposée : P2 élevée (une équipe bloquée, échéance métier sous 5 jours) · Ton : urgence métier · Réponses existantes : R-21 (droits sur l'entité : même symptôme, mais un seul utilisateur), R-34 (changement de profil) · Confiance : moyenne · Escalade : N2 si l'administrateur ne trouve pas de changement de droits.

**Réponse au client**
> Bonjour Madame,
> Nous avons bien noté votre comité de jeudi.
> Quand toute une équipe perd l'accès aux projets d'un même programme, la cause la plus fréquente est un changement de droits sur l'entité du programme. Pouvez-vous demander à votre administrateur de vérifier que le profil de votre équipe a toujours accès à l'entité du programme Phénix [libellé exact à vérifier dans la doc Triskell] ?
> Si les droits n'ont pas changé, merci de nous indiquer l'heure à laquelle le problème est apparu et le nom d'un utilisateur concerné : nous reprendrons l'analyse en priorité.
> Bien cordialement,

**Note interne** : 8 utilisateurs d'une même équipe, depuis ce matin, sur un seul programme → hypothèse H1 changement de droits sur l'entité (R-21), H2 synchronisation d'annuaire qui a modifié le profil (R-34). Si H1 et H2 sont écartées : escalade N2, instance de production, heure d'apparition à obtenir.

**Article d'aide** : non proposé (deux tickets proches, mais la cause n'est pas confirmée).

## Pourquoi c'est juste
- Le ticket R-21 concernait un seul utilisateur : la réponse le présente comme une cause fréquente, pas comme le diagnostic.
- Aucune promesse de délai malgré le comité de jeudi ; l'échéance est reconnue et la priorité relevée.
- Le client sait exactement quoi demander à son administrateur.
