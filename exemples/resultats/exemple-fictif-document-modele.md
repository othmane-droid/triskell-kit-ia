# Exemple fictif — document à partir d'un modèle (skill `triskell-document-modele`)

> Test du 19/10/2026 sur `demo4-courrier-helianthe-et-modele.docx` (document fictif : courrier reçu + informations internes + modèle Nova Software dans un seul fichier). Mode : **courrier / réponse**.
> Fichiers produits : `exemple-fictif-document-modele.docx` (copie du modèle remplie, styles Arial 12 et gras des intertitres conservés) · `exemple-fictif-document-modele.json` (le plan donné au script).

---

**Réponse attendue avant le 20/10/2026** (courrier du 05/10, Groupe Hélianthe Industrie).

## Table de correspondance

| # | Section du modèle | Contenu | Source | Statut |
|---|---|---|---|---|
| 1 | `[Lieu], le [date]` | — | absent | Manquant |
| 2 | Objet | « Demande de précisions sur votre offre et sur les conditions de déploiement » | Courrier · ligne Objet (consigne du modèle : reprendre l'objet) | Repris |
| 3 | `Madame [Nom],` | Madame Moreau | Courrier · signature « Isabelle Moreau, Acheteuse projets » | Repris |
| 4 | Remerciement | Courrier du 5 octobre 2026, 3 points de précision | Courrier · date + 1er paragraphe | Reformulé |
| 5 | Point 1 | Déploiement 4 sites en 10 à 12 semaines, pilote possible de 4 semaines | Infos internes · « Déploiement » | Reformulé |
| 6 | Point 2 | 3 sessions de 2 h à distance par profil (administrateurs, chefs de projet, direction), support PDF, replays | Infos internes · « Formation » | Reformulé |
| 7 | Point 3 | Export complet Excel et CSV à tout moment ; en fin de contrat, sur demande sous 30 jours | Infos internes · « Réversibilité » | Reformulé |
| 8 | Formules de clôture | Recopiées du modèle | Modèle | Repris |
| 9 | Signature | — | absent | Manquant |

Contrôles : 3 demandes dans le courrier → 3 réponses, dans l'ordre. Chiffres identiques à la source (10 à 12 semaines, 4 semaines, 3 × 2 h, 30 jours). 0 champ du modèle restant, 4 « [à préciser] » surlignés.

## Manques

| Manque | Où | Qui peut le fournir |
|---|---|---|
| Lieu et date d'envoi | En-tête | Commercial en charge |
| Prénom, nom et fonction du signataire | Signature | Commercial en charge |

## Points de vigilance
- **Suppression des données en fin de contrat** : le courrier demande « les conditions de réversibilité » ; les informations internes parlent de l'export, pas de la suppression. Rien n'a été ajouté. À compléter si une règle validée existe.
- **Contradiction possible entre documents** : dans le même kit de test, la base sécurité (demo1) indique un export « CSV, JSON » et une suppression sous 30 jours, alors que les informations internes de ce courrier disent « Excel et CSV ». La réponse suit la source fournie pour ce courrier ; à faire trancher avant envoi si les deux documents sont dans le projet.
- **Supposé** : aucun.

À relire avant envoi : les passages surlignés en jaune sont à compléter.
