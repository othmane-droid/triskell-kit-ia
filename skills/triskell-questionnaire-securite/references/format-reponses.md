# Format de `reponses.json` et des livrables

## reponses.json (entrée de `scripts/remplir.py`)

```json
{
  "meta": {
    "questionnaire": "nom du fichier reçu",
    "base": "nom de la base + date de validation + valideur",
    "prepare_le": "JJ/MM/AAAA"
  },
  "reponses": [
    {
      "feuille": "Questionnaire sécurité",
      "ligne": 7,
      "statut": "Validé",
      "confiance": "Haute",
      "source": "B2 Certifications",
      "reponse": "Texte repris de la base",
      "justificatif": "Certificat ISO 27001 (à joindre)",
      "oui_non": "Oui",
      "a_valider_par": "RSSI",
      "note": "Ce qui manque, en une phrase"
    }
  ]
}
```

| Champ | Obligatoire | Règle |
|---|---|---|
| `feuille` | non | Nom exact de l'onglet. Absent = premier onglet |
| `ligne` | oui | Numéro de ligne Excel de la question (donné par `extraire.py questions`) |
| `statut` | oui | `Validé`, `À valider` ou `Hors base`. Le script refuse toute autre valeur |
| `confiance` | oui | `Haute`, `Moyenne`, `Basse` ou `—` |
| `source` | oui si Validé | Identifiant de l'entrée de la base (`B4 Sauvegardes`) |
| `reponse` | non si Hors base | Le script refuse un texte sur une ligne « Hors base » |
| `justificatif` | non | Écrit dans la colonne « Source / justificatif » **du prospect** si elle existe. Uniquement un document cité par la base |
| `oui_non` | non | Écrit dans la colonne Oui / Non du prospect, seulement si le statut est « Validé » |
| `a_valider_par`, `note` | si non Validé | Qui tranche, et ce qu'il manque |

Exemple complet (25 questions) : `exemples/resultats/exemple-fictif-questionnaire-securite.json` du kit.

## Colonnes ajoutées à la copie de travail
À droite de la dernière colonne du prospect, avec le style de son en-tête : **Statut (interne)** (liste déroulante, couleur : vert Validé, orange À valider, rouge Hors base) · **Confiance (interne)** · **Source dans la base (interne)** · **À valider par / note (interne)**. Plus une feuille **Synthèse interne** : compteurs et questions à faire valider.

La version à envoyer (`--client`) n'a ni ces colonnes ni cette feuille, et n'est produite que si tout est « Validé ».

## Sans exécution de code : le tableau à rendre
Un seul tableau, dans l'ordre et avec les numéros du prospect :

| N° | Question (copiée) | Réponse proposée | Statut | Confiance | Source dans la base | À valider par |
|---|---|---|---|---|---|---|

Puis, dans cet ordre : le bilan chiffré, la liste des questions pour le RSSI / DPO (section suivante), et la phrase : « Copiez la colonne Réponse dans le fichier du prospect après validation ; les colonnes Statut à Source restent internes. »

## Message de validation à envoyer au RSSI / DPO
Prêt à copier dans Teams ou Outlook, une ligne par question :

> Objet : Questionnaire sécurité [prospect] — [n] points à valider avant le [date limite]
> Bonjour [prénom],
> Le questionnaire [prospect] est prérempli à partir de la base validée du [date]. Il me manque votre réponse sur ces points :
> 1. Q[n°] — [question courte] — Ce qu'il manque : [précision]. Proposition : [texte « À valider » ou « aucune »]
> Le fichier de travail est joint (colonne « Statut » en orange et rouge). Merci de me répondre directement dans la colonne Réponse.

## Synthèse finale (dans la conversation)
5 lignes maximum :
1. « [n] questions : [x] Validé, [y] À valider, [z] Hors base. »
2. Le fichier de travail.
3. Les 3 points les plus sensibles (engagement contractuel, IA, audit, délais), avec leur valideur.
4. Les entrées de la base périmées ou ambiguës repérées, s'il y en a.
5. « Rien ne part chez le prospect avant validation des lignes orange et rouges. »
