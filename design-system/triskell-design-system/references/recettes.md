# Les 7 recettes de présentation

Chaque recette est un squelette prêt à remplir dans `recettes/<nom>.json` : bon ordre des slides, bons composants, titres « À ÉCRIRE : » à remplacer par des titres-messages, valeurs `null` à compléter. Le squelette se génère tel quel (utile pour montrer la structure), mais le contrôleur bloque tant qu'il reste un « À ÉCRIRE : ».

| Recette | Quand | Durée | Public | Slides |
|---|---|---|---|---|
| `proposition-commerciale` | Soutenance ou envoi d'une proposition | 45 min | Sponsor, PMO, achats | 20 |
| `kickoff-client` | Réunion de lancement avec le client | 1 h 30 | Sponsor, équipe projet, administrateur | 16 |
| `copil` | Comité de pilotage d'un projet en cours | 1 h | Sponsor, direction | 12 |
| `business-review` | Revue trimestrielle client : valeur, adoption, suite | 1 h | Sponsor, CSM | 9 |
| `presentation-produit` | Présentation de la solution, webinar, salon | 30 min | Prospects, clients | 11 |
| `comite-direction` | Note de décision interne | 20 min | Comité de direction Triskell | 7 |
| `formation-atelier` | Formation ou atelier | 2 h | Collaborateurs, utilisateurs | 10 |

Pour le kick-off **interne** (passation DC → DSC), utiliser le skill `triskell-kickoff-dc-dsc`, qui remplit la trame officielle et calcule le verdict GO Projet.

## Les règles d'une présentation qui fait avancer
1. **Slide 2 = la synthèse** (`summary`) : 3 messages + la décision attendue. Un sponsor qui ne lit que cette slide doit savoir quoi décider.
2. **Une partie = un séparateur** (`section`), 2 à 6 slides par partie.
3. **Le constat avant la solution** : `statement` ou `kpis` d'abord, puis `before_after`, puis la proposition.
4. **Toujours une preuve chiffrée** (`kpis` ou `chart`) avec sa source.
5. **Le planning se montre** : `roadmap` pour la vue d'ensemble, `timeline` pour les jalons, `steps` pour la démarche.
6. **On finit par une demande** (`cta`) : qui décide quoi, pour quand, et le prochain rendez-vous. Puis `closing`.
7. **Un accent orange par slide**, pas plus.

## Adapter une recette
- Présentation courte (moins de 10 slides) : retirer l'agenda et les séparateurs.
- Public direction : garder `summary`, `kpis`, `chart`, `cards` (options), `cta` ; retirer le détail opérationnel.
- Public opérationnel : ajouter `phases`, `actions`, `checklist`, `table`.
- Présentation client : vouvoiement, aucun nom de concurrent, aucune donnée interne (GEPIL, marges, TJM).
