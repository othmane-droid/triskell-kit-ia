# Résultat du skill `triskell-reponse-support` sur le fichier de test (FICTIF)

> Entrée : `exemples/fichiers-de-test/demo2-tickets-support-fictifs.docx` (document fictif : les réponses ne reflètent pas la documentation réelle du produit). Base : tickets résolus T-101 à T-110. Ticket traité : T-111.
> Demande testée : « Réponds au ticket T-111. »

---

Pas d'alerte humaine : ni perte de données, ni sécurité, ni production indisponible. L'échéance métier (vendredi) relève la priorité.

## Fiche de qualification
```
Ticket T-111 · Incident (export incomplet, non reproduit) · Priorité proposée : P2 élevée
  (bloquant pour la clôture, échéance métier « vendredi », contournement probable)
Problème : un utilisateur exporte les temps de toute l'équipe sur l'année 2026 ; le fichier
  s'ouvre mais il manque le second semestre et une partie des projets terminés ; les chiffres
  sont attendus par la finance vendredi.
Ton : urgence métier · rassurant et concret
Réponses existantes :
  - T-108 (export des temps limité à 10 000 lignes par fichier) : correspond au second semestre
    manquant sur une année complète d'équipe ; le client ne dit pas combien de lignes il a.
  - T-102 (projets archivés exclus par défaut) : correspond aux « projets terminés » manquants
    si « terminé » veut dire « archivé » [à vérifier dans la doc Triskell].
  - T-101 (filtre « Période ») : possible si la période choisie ne couvre pas toute l'année ;
    moins probable, le premier semestre étant complet.
Confiance : moyenne (deux causes connues expliquent chacune une partie du symptôme, non confirmées)
Escalade : non pour l'instant ; N2 si l'export par trimestre avec projets archivés reste incomplet.
```

## Réponse au client

**Objet** : RE: Export Excel des temps incomplet

Bonjour,

Merci pour votre message, nous avons bien noté que la finance attend vos chiffres vendredi.

Ce symptôme correspond le plus souvent à deux causes que vous pouvez vérifier tout de suite :

1. **Taille du fichier** : l'export des temps est limité à 10 000 lignes par fichier [limite à vérifier dans la doc Triskell à jour]. Sur une année complète pour toute une équipe, la limite est vite atteinte et les derniers mois n'apparaissent pas. Exportez plutôt trimestre par trimestre (ou entité par entité), puis assemblez les fichiers.
2. **Projets terminés** : par défaut, l'export n'inclut pas les projets archivés. Avant de lancer l'export, cochez l'option « Inclure les projets archivés ».

Vérifiez aussi que le filtre « Période » couvre bien du 1er janvier au 31 décembre 2026.

Si le fichier reste incomplet, pouvez-vous nous indiquer le nombre de lignes du fichier obtenu et les filtres utilisés ? Nous reprendrons alors l'analyse en priorité.

Bien cordialement,
[Signature support]

## Note interne
```
NOTE INTERNE · T-111 · [client / instance à compléter] · [date du ticket à compléter]
Type : incident · Priorité proposée : P2 · Escalade vers : aucune pour l'instant (N2 si échec)
Résumé : export des temps annuel 2026 de toute une équipe incomplet (second semestre et
une partie des projets terminés absents). Échéance finance : vendredi.

Contexte technique
- Instance : à demander (production supposée)
- Version : à demander
- Utilisateur : profil et droits à vérifier (voit-il toutes les entités de l'équipe ? cf. T-103)
- Volume : nombre de lignes du fichier à demander ; si ≈ 10 000, H1 confirmée

Reproduire
1. Export des temps, période 01/01/2026 → 31/12/2026, toute l'équipe
Résultat attendu : toutes les saisies de l'année, projets terminés compris
Résultat obtenu : second semestre absent, une partie des projets terminés absente
Fréquence / depuis / changement récent : à demander

Hypothèses (à vérifier)
- H1 · limite de 10 000 lignes (T-108) · confirmer par le nombre de lignes du fichier
- H2 · projets archivés exclus par défaut (T-102) · confirmer que les projets manquants sont archivés
- H3 · filtre de période (T-101) · peu probable, le premier semestre est complet
- H4 · droits sur certaines entités (T-103) · si des projets manquent aussi sur le premier semestre

Déjà répondu au client : contournements H1, H2, H3 ; 2 informations demandées
Échéance métier : vendredi → si pas de retour client la veille, relancer par téléphone
Signal produit : 5 tickets sur 11 concernent l'export des temps (T-101, T-102, T-105, T-108,
T-111). Suggestion à transmettre au produit via le CSM, sans engagement : avertir l'utilisateur
quand l'export atteint la limite de lignes, plutôt que de livrer un fichier tronqué sans message.
```

## Article d'aide proposé
```
Titre : Obtenir un export des temps complet sur une longue période
Pour qui : utilisateurs et administrateurs
Résumé : un export des temps vide, incomplet ou mal daté vient presque toujours d'un réglage
d'export. Quatre vérifications règlent la plupart des cas.

Symptôme
Le fichier exporté est vide, s'arrête avant la fin de la période, n'affiche pas certains projets
ou présente des dates au format américain.

Causes et solutions
| Si… | Alors… |
|---|---|
| le fichier est vide ou couvre la mauvaise période | réglez le filtre « Période » sur la période voulue, puis relancez l'export |
| des projets terminés manquent | cochez « Inclure les projets archivés » avant l'export |
| le fichier s'arrête avant la fin de la période | l'export est limité à 10 000 lignes : exportez par trimestre ou par entité |
| les dates sont au format américain | passez la langue de votre profil en français, puis relancez l'export |

À savoir : limite de 10 000 lignes par fichier [à vérifier dans la doc Triskell à jour]
Tickets à l'origine : T-101, T-102, T-105, T-108, T-111 (à retirer avant publication)
Statut : brouillon à valider par le support avant publication
```

## À vérifier avant envoi
- La limite de 10 000 lignes vient d'un ticket résolu (T-108) : vérifier qu'elle est toujours d'actualité dans la doc.
- « Projets terminés » = « projets archivés » ? À confirmer dans la doc ; sinon retirer le point 2.
- Le ticket n'est pas daté : « vendredi » ne peut pas être converti en date.
- Libellés « Période » et « Inclure les projets archivés » : repris des tickets T-101 et T-102, à vérifier dans l'interface actuelle.

À relire avant envoi.

---

## Relecture du test (contrôle du skill)
- Aucun comportement inventé : chaque option et la limite citées viennent de T-101, T-102, T-105, T-108 ; les correspondances partielles sont présentées comme des pistes.
- Aucune date ni promesse de correctif ; la suggestion produit reste interne et « sans engagement ».
- Réponse client : ce qui débloque arrive avant les questions ; 2 informations demandées (maximum 3).
- Écarts repérés pendant le test et corrigés dans le skill :
  1. une limite chiffrée tirée d'un ancien ticket peut être périmée → ajout dans `checklist-relecture.md` : « une limite ou un libellé repris d'un ticket ancien se vérifie dans la doc à jour » ;
  2. un ticket non daté empêche de convertir « vendredi » → ajout dans le SKILL.md (étape 2) : dater l'échéance métier ou l'écrire telle quelle avec « date à préciser ».
