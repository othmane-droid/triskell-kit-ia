# Table de correspondance, liste des manques, plan JSON

## 1. Table de correspondance (à montrer avant de produire le fichier)
Une ligne par champ ou section du modèle, dans l'ordre du modèle :

| # | Section du modèle | Contenu prévu (résumé) | Source (document · passage) | Statut |
|---|---|---|---|---|
| 1 | `[Lieu], le [date]` | — | absent | Manquant |
| 2 | Objet | Objet du courrier reçu, repris tel quel | Courrier du 05/10 · « Objet : … » | Repris |
| 5 | Point 1 | Durée 10 à 12 semaines, pilote 4 semaines | Infos internes · ligne « Déploiement » | Reformulé |

Statuts :
- **Repris** : texte de la source recopié (formule, objet, nom).
- **Reformulé** : même information, mise en phrase dans le ton du modèle. Aucun chiffre ni engagement ajouté.
- **Manquant** : le modèle attend quelque chose que la source ne donne pas → « [à préciser : …] » dans le document.
- **Supposé** : choix de forme sans impact sur le fond (ex. civilité « Madame » déduite de la signature). À lister pour relecture. **Jamais pour un chiffre, une date, un nom, un engagement.**

Ajouter sous la table, s'il y en a :
- **Demandes de la source non couvertes par le modèle** (ex. le courrier pose une 4ᵉ question) et ce que tu as fait (bloc dupliqué).
- **Contenu de la source non utilisé** (et pourquoi).

## 2. Contrôles de cohérence avant de produire
- Chaque demande du document source a sa réponse (compter : 3 demandes → 3 réponses).
- Chaque chiffre du document produit existe à l'identique dans la source (unités, fourchettes : « 10 à 12 semaines » ne devient pas « environ 3 mois »).
- Si deux documents du projet disent des choses différentes sur le même sujet (ex. formats d'export « Excel et CSV » dans une note interne, « CSV, JSON » dans une base validée), **ne pas trancher** : garder la source demandée pour ce document et signaler l'écart dans les points de vigilance.
- Une date limite fixée par le destinataire est rappelée dans la livraison.
- Aucun reste de consigne du modèle : `[…]`, `XXX`, « NOM CLIENT », « A MODIFIER » (le script les liste).

## 3. Liste des manques (livrée avec le document)
Format court, une ligne par manque, avec qui peut répondre :

| Manque | Où dans le document | Qui peut le fournir |
|---|---|---|
| Signataire et fonction | Signature | Commercial en charge |
| Lieu et date d'envoi | En-tête | Commercial en charge |

Puis **Points de vigilance** (contradictions, engagements à faire valider, date limite) et la phrase : « À relire avant envoi : les passages surlignés en jaune sont à compléter. »

## 4. Plan JSON pour `scripts/remplir_modele.py`
Les numéros `paragraphe` viennent de `python scripts/analyser_modele.py modele.docx --texte` (document d'origine, avant toute modification).

```json
{
  "garder_a_partir_de": "[Lieu], le [date]",
  "garder_jusqua": null,
  "dupliquer": [{"paragraphe": 20, "remplacements": [{"cherche": "[Point 3 — titre]", "remplace": "4. …"}]}],
  "remplacements": [
    {"paragraphe": 15, "cherche": "[Nom]", "remplace": "Moreau"},
    {"cherche": "Ancien Client SA", "remplace": "Nouveau Client SAS"}
  ],
  "supprimer_paragraphes": [],
  "interdits": ["Ancien Client"]
}
```
- `garder_a_partir_de` / `garder_jusqua` : quand le modèle est noyé dans un document qui contient aussi la source (cas du fichier de test demo4) ; on garde la plage du modèle seulement. Les textes sont ceux **d'origine**.
- `paragraphe` absent : remplacement partout (corps, tableaux, en-têtes, pieds de page). À réserver aux noms propres ; pour les champs génériques répétés (`[réponse]`), toujours donner le numéro.
- Écrire « \n » pour un retour à la ligne dans le même paragraphe (comme dans le modèle).
- Écrire les manques sous la forme `[à préciser : …]` : ils sont surlignés en jaune et listés par le script.

Le script garde police, taille, gras et espacements du modèle (remplacement run par run). Si un champ est coupé entre deux runs, il regroupe le paragraphe et le signale : vérifier alors le gras de ce paragraphe.

Exemple complet : `exemples/resultats/exemple-fictif-document-modele.json` du kit.

## 5. Modèle qui n'est pas un .docx
- **PDF, image, texte collé** : relever la structure à la main ; produire un .docx neuf avec python-docx (titres, paragraphes, listes dans le même ordre, police du modèle si elle est lisible), et dire que la mise en page exacte n'a pas pu être reprise.
- **Présentation** : passer la main au skill `triskell-design-system` avec la table de correspondance comme brief.
- **Mail** : rendre le texte prêt à coller (objet + corps), sans fichier.
