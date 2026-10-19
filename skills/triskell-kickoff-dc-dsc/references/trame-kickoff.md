# Trame du kick-off interne TSF : champ par champ

> Reprend exactement le modèle officiel « NOM CLIENT - Kickoff interne TSF - AAMMJJ » (35 slides, 7 parties). Colonnes : la clé dans la fiche JSON · où trouver l'information · qui la fournit · la règle de contrôle.
> Abréviations : DC Direction Commerciale · DSC Direction Succès Client · ADV Administration des Ventes · MKG Marketing · AVV avant-vente · DP directeur de projet · CSM Customer Success Manager · jrsH jours-homme · F / NF facturable / non facturable.

## 0. En-tête
| Clé | Source | Qui | Règle |
|---|---|---|---|
| `meta.client` | Proposition, BDC | DC | Raison sociale exacte, comme sur le BDC |
| `meta.offre` | Proposition | DC | Une valeur parmi : Ready, Adapt, Plateform, POC |
| `meta.date_kickoff` | Agenda | DSC | Format JJ/MM/AAAA. Sert au nom du fichier (AAMMJJ) |
| `meta.version` | — | DSC | 1.0 à la première diffusion, +0.1 à chaque mise à jour |

Préambule (fixe) : le document transmet de la DC vers la DSC, l'ADV, le Marketing et le Support les informations sur le client, son besoin et l'offre formalisée. Il est rédigé par le DC et le CSM / DP ou le consultant, stocké dans « Clients - Projets », publié dans le canal Teams du client.

## Participants
| Clé | Source | Qui | Règle |
|---|---|---|---|
| `participants.cycle_de_vente` (DC, DSC / AVV, DSC / Consultant) | HubSpot (propriétaire de l'affaire), mails | DC | Prénom + nom, une personne par rôle ou « non concerné » |
| `participants.equipe_projet` (Consultant, Intégration, DP) | Staffing DSC | DSC | Le DP est obligatoire avant le kick-off client |
| `participants.autres_invites` | Modèle (valeurs par défaut) | DSC | Valeurs du modèle à confirmer : ADV Isabelle P, Marketing Lilian & Isabelle M, CSM Richard, Architecte Arnaud, Support Myriam & Arielle |

## 1. Éléments de contexte
| Clé | Source | Qui | Règle |
|---|---|---|---|
| `client.identite` : secteur, activités / offres, chiffres-clés, localisation | Site du client, proposition (contexte), HubSpot | DC | Chiffres-clés avec leur année. Rien de non public sans source interne |
| `client.autres` : site web, enjeux stratégiques / vision, éléments contextuels, autres | Mails, CR de découverte | DC | Enjeux formulés avec les mots du client |
| `contexte.lead` : date, contexte, cahier des charges | HubSpot (date de création), premier mail | DC | Date JJ/MM/AAAA ; cahier des charges : oui (date de réception) ou non |
| `contexte.cycle_de_vente.raisons_du_choix` | CR de closing, mail de choix | DC | **Bloquant si vide** : c'est ce que l'équipe projet doit tenir |
| `…concurrence` | CR, mails | DC | Nommer les concurrents en interne est autorisé ; jamais dans un support client |
| `…dates_cles` | HubSpot, mails | DC | Démo, soutenance, choix, signature |
| `…maquette` / `demo_base_demo` / `gouvernance_presentee` | DC, AVV | DC | Maquette : si oui, l'URL d'accès |
| `contexte.objectifs_enjeux` | Proposition, CR | DC | **Bloquant si vide.** 2 à 5 puces |
| `contexte.challenges` | CR | DC | 2 à 5 puces |
| `contexte.facteurs_cles_succes` | CR, cahier des charges | DC | **Bloquant si vide** : ils deviennent les critères de réussite du projet |

## 2. Interlocuteurs-clés côté client
Rôles du modèle : Direction Client · Sponsor · Futur(e) administrateur(-trice) Solution · Équipe Projet · DAF · Facturation & Comptabilité · Achats · Juridique.
Source : signataires du BDC, destinataires des mails, HubSpot. Qui : DC.
Règle : **Sponsor et futur administrateur bloquants** ; Facturation & Comptabilité nécessaire à l'ADV avant la première facture.

## 3. Périmètre fonctionnel & technique
| Clé | Source | Qui | Règle |
|---|---|---|---|
| `perimetre.processus` | Proposition, cahier des charges, CR | DSC (AVV) | Pour chaque processus de la liste : inclus oui / non, priorité P1 à P3, précision |
| `perimetre.decommissionnement` | CR, mails | DSC | Si oui : quel outil, quelle date. C'est souvent la vraie échéance |
| `perimetre.contrainte_mise_en_production` | CR | DSC | Date imposée, période de gel, clôture budgétaire |
| `perimetre.echanges_client` : date, priorités, documents et inputs, contraintes calendaires | CR des échanges | DSC | Priorités bloquantes si vides |
| `licences` : Production (avec 1 admin), Sandbox, Avancé, Contributeur, Lecture / Demandeur, Flex, Hébergeur (OBS / AWS), POC licences | Proposition (tableau de souscription), BDC | DC | Somme Avancé + Contributeur + Lecture + Flex = nombre d'utilisateurs de la synthèse financière |
| `technique.sso` : mise en œuvre, maintenance, nombre | Proposition, CR technique | DSC (Architecte) | Si SSO, la maintenance a un porteur |
| `technique.integrations` | Proposition, cahier des charges | DSC | Une ligne par flux : source → cible, fréquence |
| `prestations` : volume jrsH, forfait / régie, formation admin, reprise de données, Pack Change, Pack Contextualisation | Proposition | DC | Le volume doit égaler la somme de la répartition des charges |
| `contractuel` : durée d'engagement, renouvellement (révision SYNTEC), contrat signé, commande reçue | Contrat, BDC | DC | Contrat signé et commande reçue sont des lignes critiques du GO |

**Liste des processus de pilotage** (à reprendre telle quelle) : gestion de portefeuille · gestion de la demande · gestion de projet / programme / récurrent (méthodologie : cycle en V, Phase & Gate, Agile) · gestion de ressources · gestion financière / budgétaire (cycles budgétaires) · saisie des temps · indicateurs, reportings & tableaux de bord · comitologies et décisions · gestion des risques.

## 4. Démarrage du projet
| Clé | Source | Qui | Règle |
|---|---|---|---|
| `demarrage.reunion_lancement` | Agenda, mails | DSC | Bloquant si vide |
| `demarrage.duree_projet` | Proposition | DC | En mois |
| `demarrage.ouverture_service` | Proposition, CR | DSC | Bloquant si vide ; doit être postérieure au lancement |
| `demarrage.gouvernance` | Proposition | DSC | COPIL, COPROJ, fréquence |
| `demarrage.points_attention` | CR, ressenti DC | DC | Ce que le DC sait et que la DSC doit savoir : disponibilité du sponsor, tensions internes, historique d'échec |
| `repartition_charges` | Proposition, GEPIL (onglet Tableau des ressources) | DSC | Toutes les charges, F et NF. Somme = volume vendu |
Slides du modèle à compléter à la main : cadencement de l'implémentation (démarche de l'offre), planning prévisionnel GEPIL (3 vues, jalons-clés en évidence).

## 5. Éléments financiers
| Clé | Source | Qui | Règle |
|---|---|---|---|
| `financier.licences_users`, `financier.synthese` (6 mois, année 1 post 6 mois, années 2 et 3) | Proposition (synthèse financière) | DC | Montants HT, recopiés sans arrondi |
| `financier.budget_implementation_ht` | Proposition (chiffrage implémentation) | DC | HT |
| `financier.reference_proposition` | Proposition | DC | Format 202x-xxx |
| `facturation.licences_a_compter_du`, `paiement` | Contrat | ADV | Par défaut du modèle : paiement par année à échoir |
| `facturation.echeancier_implementation` | Proposition, contrat | DC | **Somme des pourcentages = 100 %**. Montant calculé automatiquement |
| `facturation.lignes_gepil` | Répartition des charges | ADV | Une ligne F avec libellé, jrsH et TJM ; une ligne NF avec libellé et jrsH. Totaux = répartition |
| `facturation.termes_paiement` | Contrat | ADV | Ex. 30 jours fin de mois |
| `facturation.sous_traitance` | Proposition | DC | Si oui : périmètre et jrsH du partenaire |
| `facturation.bdc_recu_le` | BDC | ADV | **Critique** : sans BDC, pas de démarrage |

## 6. Marketing & Communication
`marketing.contact_reference` : nom du contact pour la référence, **qui doit exister dans GEPIL**.
`marketing.consentements` : oui / non / inconnu pour chacun des 10 usages du modèle : logo dans la liste clients du site · citation de l'interlocuteur principal (nom, fonction, photo) · news signature sur le blog avec relais LinkedIn · logo dans les supports commerciaux · citation dans les supports commerciaux · communiqué de presse (uniquement grand compte et gros projet) · fiche témoignage après la mise en production · témoignage 1to1 auprès de prospects · témoignage lors d'un événement clients · témoignage lors d'un événement prospects (physique ou webinar).
Règle : un seul « oui » impose un contact de référence nommé. Un consentement non écrit reste « inconnu ».

## 7. Actions & Check-list « GO Projet »
Actions fixes du modèle (le pipeline les ajoute ; les échéances se fixent en séance) :
- **Support** : créer les instances client (sandbox et production) · donner les accès à SKORAN et au Teams Triskell Club Utilisateurs · envoyer le mail de bienvenue (copie ADV et CSM / DP). Rappel : ne pas toper en « Comm. Incident » tant que la production n'est pas ouverte.
- **DC & CSM dans HubSpot** : DC bascule les contacts en clients · CSM crée, rattache et actualise les contacts de la solution client.
- **CSM / DP & DC** : formaliser l'échéancier de facturation et le transmettre à l'ADV.
- **ADV** : créer la souscription et les lignes F et NF dans GEPIL.
- **Marketing** : initier la fiche référence client.

Check-list GO (9 lignes, `go_projet`) : équipe projet synchronisée, dont avec l'avant-vente · périmètre défini et priorisé (critique) · planning prévisionnel créé dans GEPIL · plan de charge renseigné dans GEPIL · contacts clients créés dans HubSpot par le commercial · répertoire client créé dans « Clients Actifs » avec l'offre · contrat signé (critique) · bon de commande reçu (critique) · toutes les informations nécessaires connues et à disposition.

## Contrôles automatiques du pipeline
| Contrôle | Gravité |
|---|---|
| Somme de l'échéancier ≠ 100 % | bloquant |
| Ouverture du service ≤ réunion de lancement | bloquant |
| Contrat non signé | bloquant |
| Aucun BDC reçu | bloquant |
| Utilisateurs licenciés (configuration) ≠ synthèse financière | important |
| jrsH vendus ≠ somme de la répartition des charges | important |
| jrsH facturables des lignes GEPIL ≠ répartition | important |
| Ligne GEPIL facturable sans TJM | important |
| Consentement marketing sans contact de référence | important |
| Décommissionnement annoncé sans précision | important |
| SSO sans porteur de maintenance | conseil |
| Processus inclus sans priorité | conseil |
