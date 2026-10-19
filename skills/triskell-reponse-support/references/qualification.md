# Qualifier un ticket : type, priorité, ton, escalade

> La grille de priorité ci-dessous est une grille **par défaut** proposée par le kit. Elle ne fixe aucun délai. Dès que Triskell joint sa grille contractuelle (SLA), celle-ci la remplace. [à compléter par Triskell : grille SLA et délais]

## 1. Les 6 types de demandes
| Type | Reconnaître | Qui traite | Réponse au client |
|---|---|---|---|
| **Question d'usage** | « comment faire », « où trouver », résultat inattendu mais explicable par une manipulation | N1 | La procédure, si une source la décrit |
| **Paramétrage et droits** | un utilisateur ne voit pas, ne peut pas modifier, n'a pas accès ; notifications ; synchronisation de comptes | N1, avec l'administrateur du client | Ce que l'administrateur doit vérifier ou faire |
| **Incident** | ça marchait, ça ne marche plus ; lenteur ; erreur ; service indisponible ; pas encore reproduit | N1 puis N2 si non résolu | Contournement si connu, informations demandées, suivi |
| **Bug supposé** | comportement contraire à la documentation, reproductible, sur plusieurs utilisateurs | N2 puis équipe technique | Accusé de réception, analyse en cours, contournement si connu. **Jamais « c'est un bug » avant reproduction** |
| **Demande d'évolution** | « il faudrait que », « est-il possible d'ajouter », besoin non couvert | Produit, via le CSM | Remerciement, transmission, pas d'engagement sur la réalisation ni sur le délai |
| **Facturation et contrat** | facture, licences, renouvellement, résiliation, remise | ADV ou CSM | Accusé de réception et transfert, pas de réponse sur le fond |

Un ticket peut mêler deux types (« l'export est incomplet et il faudrait pouvoir exporter plus de lignes ») : traite le type principal, signale l'autre dans la note interne.

## 2. Grille de priorité par défaut
Impact : **bloquant** (le client ne peut plus travailler sur un processus clé, ou une échéance métier est menacée) · **gênant** (contournement possible mais coûteux) · **mineur** (confort).
Étendue : un utilisateur · une équipe · toute l'instance.

| | Toute l'instance | Une équipe | Un utilisateur |
|---|---|---|---|
| Bloquant, sans contournement | P1 critique | P1 critique | P2 élevée |
| Bloquant avec contournement, ou échéance métier sous 5 jours ouvrés | P2 élevée | P2 élevée | P3 normale |
| Gênant | P3 normale | P3 normale | P3 normale |
| Mineur, question, évolution | P4 basse | P4 basse | P4 basse |

Règles : sécurité, perte de données ou production indisponible = P1 et alerte humaine, quel que soit le reste. La priorité est **proposée** : la personne du support la valide. L'urgence ressentie par le client se prend en compte dans le ton, pas en surclassant la priorité sans raison.

## 3. Grille de ton
| Situation | Ton | À faire | À éviter |
|---|---|---|---|
| Question simple | Direct, cordial | La réponse dès la 2ᵉ phrase | Les formules d'attente |
| Urgence métier (clôture, comité, paie) | Rassurant et concret | Reconnaître l'échéance en une phrase, donner d'abord ce qui débloque aujourd'hui | Promettre un délai, dramatiser |
| Client agacé ou ticket répété | Calme, responsable | Reconnaître la gêne sans excuse excessive, montrer ce qui est fait, proposer un appel si le fil dure | Se justifier, contredire, rejeter la faute |
| Erreur de manipulation | Neutre, pédagogique | Décrire le bon réglage comme une étape | « Vous avez mal… », « comme indiqué dans la doc » |
| Demande d'évolution | Reconnaissant | Reformuler le besoin, dire qu'il est transmis | « C'est prévu », « ce sera fait » |
| Utilisateur final non administrateur | Simple, sans jargon | Lui dire quoi demander à son administrateur | Les termes techniques internes |

## 4. Passer à un humain sans attendre
- Perte, corruption ou fuite de données ; accès d'une personne qui ne devrait pas en avoir ; soupçon de faille.
- Production indisponible pour tous.
- Menace de résiliation, mention d'un concurrent, plainte adressée à la direction.
- Troisième relance sur le même sujet.
- Question juridique (RGPD, contrat) ou demande de geste commercial.

## 5. Ce dont l'équipe technique a besoin pour reproduire
Instance concernée (production ou bac à sable [libellé exact à vérifier dans la doc Triskell]) · identifiant du client ou de l'instance · version si connue · navigateur et poste si l'interface est en cause · profil et droits de l'utilisateur · étapes exactes · résultat attendu / obtenu · fréquence (toujours, parfois, une fois) · depuis quand, et ce qui a changé · volume concerné (nombre de lignes, de projets) · message d'erreur exact · pièces (fichier exporté, capture **sans donnée personnelle**) · contournement testé et son résultat.
