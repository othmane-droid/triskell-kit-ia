# Matrice de conformité

## Colonnes
| Colonne | Contenu | Règle |
|---|---|---|
| N° | Identifiant de l'exigence dans le CDC | Inchangé ; si le CDC ne numérote pas, créer `CDC-p4-01` (page + rang) et le dire |
| Niveau | Obligatoire / Souhaité / Optionnel / Non précisé | Tel qu'écrit dans le CDC |
| Catégorie | Fonctionnel, Finance, Reporting, Technique & sécurité, Déploiement, Accompagnement, Modalités de réponse | Selon la section du CDC |
| Exigence | Texte exact du CDC | Copier-coller, sans résumé |
| Emplacement | Page ou section du CDC | `p. 5` ou `§ 3.2` |
| Réponse proposée | Texte de réponse | Uniquement à partir d'une source Triskell jointe ; sinon `[à compléter]` |
| Statut | Couvert / Partiel / Non couvert / À vérifier | Voir règles ci-dessous |
| Source Triskell | Document + section | Obligatoire si la réponse est rédigée |
| Pièce / preuve | Certificat, DPA, fiche référence, capture | À joindre au dossier |
| Responsable | Qui valide la réponse | Avant-vente, RSSI, DSC, DC, juridique |
| Commentaire interne | Écart, risque, question en cours | **À retirer avant envoi** |

## Règles de statut
| Statut | Quand | Exemple |
|---|---|---|
| **Couvert** | Un document Triskell joint couvre **toute** l'exigence, explicitement | AO : SSO Entra ID ; base : « SAML 2.0, compatible Microsoft Entra ID » |
| **Partiel** | Le document couvre une partie, ou ajoute une condition absente de l'AO | AO : 99,5 % par mois ; base : 99,5 % « hors maintenances planifiées » |
| **Non couvert** | Un document Triskell dit explicitement que ce n'est pas proposé | Base : « nous ne disposons pas de rapport SOC 2 » face à une exigence SOC 2 |
| **À vérifier** | Aucune source jointe, ou source ambiguë | Toute exigence fonctionnelle sans base de réponses fonctionnelles |

« Non couvert » ne se déduit jamais d'une absence d'information : l'absence donne « À vérifier ».
Pour les exigences de **modalités** (mémoire, matrice, bordereau), statut « À vérifier » et réponse « Pièce à produire : … » jusqu'à ce que la pièce existe.

## Rédiger une réponse
- Première phrase = réponse directe à l'exigence (« Oui. », « Oui, avec la réserve suivante : … »).
- Reprendre les termes de la source sans les embellir ; adapter seulement la syntaxe.
- Vouvoiement, présent de l'indicatif, pas de superlatif (« leader », « unique », « le meilleur »).
- 80 mots maximum par exigence dans la matrice ; le détail va dans le mémoire technique.
- Partiel : dire ce qui est couvert, puis l'écart, sans le cacher ; proposer une question à l'acheteur si l'écart vient d'une ambiguïté du CDC.
- Les produits ou noms d'éditeurs des documents joints sont repris tels quels (ne pas les remplacer par « Triskell » s'ils ne le disent pas).

## Format JSON du script `matrice_xlsx.py`
```json
{
  "ao": {"acheteur": "", "reference": "", "objet": "", "date_limite": "", "date_questions": "",
         "criteres": [{"critere": "Valeur technique", "poids": 50}],
         "documents_triskell": ["Base de réponses sécurité v. 15/06/2026"], "date_analyse": "", "avertissement": ""},
  "exigences": [{"id": "EX-16", "niveau": "Obligatoire", "categorie": "Technique & sécurité",
                 "exigence": "Authentification unique (SSO) avec Microsoft Entra ID.", "emplacement": "p. 5",
                 "reponse": "…", "statut": "Couvert", "source": "Base de réponses sécurité, § 6",
                 "piece": "", "responsable": "RSSI", "commentaire_interne": ""}],
  "questions": [{"exigence": "EX-20", "question": "…", "pourquoi": "…"}],
  "go_no_go": {"criteres": [{"critere": "…", "poids": 3, "note": null, "justification": "…"}],
               "eliminatoires": [{"critere": "…", "statut": "Levé | À vérifier | Non levé", "commentaire": "…"}]}
}
```
Exemple complet : `exemple-analyse.json`. Le script refuse un statut hors des 4 valeurs.

## Version client de la matrice
Avant envoi : supprimer la colonne « Commentaire interne », vérifier qu'aucun « [à compléter] » ne reste, et que chaque « Partiel » est formulé de façon honnête et positive (ce qui est couvert d'abord).
