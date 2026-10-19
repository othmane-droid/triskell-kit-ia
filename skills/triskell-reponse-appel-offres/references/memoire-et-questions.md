# Mémoire technique et questions à l'acheteur

## 1. Plan du mémoire technique
Principe : **le plan suit les critères de notation**, pas l'organisation interne de Triskell. Le nombre de pages de chaque partie est proportionnel au poids du critère qu'elle sert (le prix est traité dans la proposition financière, pas dans le mémoire).

Budget de pages : pages disponibles (limite du règlement − 2 pour la page de garde et le sommaire) réparties au prorata des critères non financiers. Exemple : 30 pages, valeur technique 50 %, accompagnement 15 % → 28 pages × 50/65 ≈ 21 pages pour la valeur technique, 28 × 15/65 ≈ 7 pages pour l'accompagnement.

Plan type (à adapter aux sections du CDC) :
1. **Synthèse de notre réponse** (1 page) : la compréhension du besoin en 3 phrases, les 3 engagements principaux (sourcés), la couverture des exigences.
2. **Notre compréhension de votre besoin** : contexte, enjeux et calendrier du client, avec ses mots ; volumétrie.
3. **Réponse fonctionnelle** : une sous-partie par section du CDC, dans l'ordre du CDC, en rappelant les n° d'exigence couverts (« EX-01, EX-02, EX-04 »).
4. **Architecture, sécurité, conformité** : hébergement, SSO, droits, RGPD, certifications, disponibilité, API.
5. **Démarche de déploiement** : phases, pilote, reprise de données, planning (modèle validé par la DSC), gouvernance projet.
6. **Accompagnement** : formation (publics, langues, format), support (horaires, langues), conduite du changement, interlocuteur unique.
7. **Références** : uniquement validées, avec accord des clients.
8. **Annexes** : matrice de conformité, certificats, DPA, CV (vérifier si les annexes comptent dans la limite de pages : sinon, question à l'acheteur).

Pour chaque partie, indique : critère servi, n° d'exigences couverts, pages allouées, sources Triskell disponibles, responsable de la rédaction, « [à compléter] » restants.

Si une soutenance est prévue : le design system Triskell (`triskell-design-system`, recette `proposition-commerciale`) produit le support à partir du mémoire.

## 2. Questions à l'acheteur
Règles :
- Respecter le canal et la **date limite** fixés par le règlement (souvent par écrit uniquement, réponses partagées avec tous les candidats).
- Une question = un sujet, rattachée à un n° d'exigence ou à un article du règlement.
- Ne jamais révéler une faiblesse (« nous ne savons pas faire X ») : demander une précision (« l'exigence X couvre-t-elle aussi… ? »).
- Ne pas poser une question dont la réponse est dans le dossier.
- 5 à 10 questions, classées par impact sur l'offre.

Sujets qui reviennent :
| Sujet | Pourquoi poser la question |
|---|---|
| Volumétrie par profil d'utilisateur | Base du chiffrage des licences |
| Périmètre du pilote | Planning et charge de mise en œuvre |
| Reprise de données (volume, format, qualité) | Premier risque de planning |
| Intégrations (système, sens des flux, fréquence, technologie) | Charge d'intégration |
| Niveaux de service (exclusions, mode de calcul, pénalités) | Écart possible avec les engagements standard |
| Langues (formation, support, interface) | Capacité et coût |
| Sous-critères de notation, soutenance | Répartition du mémoire, préparation |
| Annexes comptées ou non dans la limite de pages | Forme, risque d'élimination |
| Durée du marché, reconduction, révision des prix | Proposition financière |

Format de sortie : tableau `N° | Exigence | Question (telle qu'elle sera envoyée) | Pourquoi`, suivi de la date limite d'envoi et du canal.
