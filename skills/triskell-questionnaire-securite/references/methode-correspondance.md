# Méthode de correspondance question → base de réponses

> À lire en entier avant le premier questionnaire. Objectif : qu'une réponse « Validé » soit toujours défendable devant le RSSI, mot pour mot.

## 1. Les trois statuts

| Statut | Quand | Ce qu'on écrit dans la colonne réponse |
|---|---|---|
| **Validé** | Une entrée de la base répond à **toute** la question, sur le même périmètre. | Le texte de la base, repris tel quel ou raccourci sans rien changer au sens. On peut ajouter « Oui. » ou « Non. » en tête si la base le dit explicitement. |
| **À valider** | La base répond **en partie** (la question demande un détail absent), ou il a fallu **combiner** deux entrées, ou la réponse dépend du contrat / de l'offre du prospect, ou l'entrée de la base date de plus de 12 mois. | Ce que la base dit, puis le manque entre crochets : « [nom du fournisseur à compléter] ». |
| **Hors base** | Rien dans la base. | Rien d'autre que « [À compléter par <qui>] ». **Aucune réponse rédigée**, même « probable ». |

Confiance (colonne interne) :
- **Haute** : même sujet, même périmètre, la réponse couvre chaque partie de la question.
- **Moyenne** : reformulation nécessaire, ou réponse partielle (donc forcément « À valider »).
- **Basse** : le rapprochement est discutable (sujet voisin). Toujours « À valider ».
- **—** : hors base.

Source (colonne interne) : l'identifiant de l'entrée (`B4 Sauvegardes`), ou la section et la page du document si la base n'est pas découpée. Jamais « base de réponses » sans précision.

## 2. Découper la question avant de chercher
Beaucoup de questions en contiennent plusieurs : « Avez-vous un DPO ? Fournissez-vous un DPA ? », « fréquence **et** durée de conservation », « pays, fournisseur, région ». Liste chaque sous-question. La réponse n'est « Validé » que si **chaque** sous-question est couverte. Sinon : « À valider » et le manque nommé.

## 3. Table des correspondances (reformulations fréquentes)

| Famille | Le prospect peut écrire | Chercher dans la base | Piège |
|---|---|---|---|
| Hébergement | localisation des données, datacenter, cloud provider, région, souveraineté, SecNumCloud | hébergement, hébergeur, datacenter, région | Le nom de l'hébergeur et la certification **de l'hébergeur** ≠ certification **de l'éditeur** |
| Transferts hors UE | transfert international, accès depuis l'étranger, CLOUD Act, clauses contractuelles types | hors UE, transfert, accès support | « Stocké en France » ne dit rien sur la **consultation** (support offshore) |
| ISO 27001 | SMSI, certification sécurité, ISO/IEC 27001:2022 | certification, ISO | Exiger **périmètre + date + organisme** ; un « alignement » sur l'ISO n'est pas une certification |
| SOC 2 | SOC 2 Type I / Type II, ISAE 3402, SSAE 18 | SOC, ISAE, rapport d'audit | Type I ≠ Type II. Si la base dit « pas de SOC 2 », répondre non, ne pas proposer d'équivalent |
| HDS | hébergement de données de santé, agrément / certification HDS | HDS, santé | Seul l'hébergeur ou l'éditeur certifié HDS peut le dire. Absent = Hors base |
| RGPD / DPA | sous-traitant au sens de l'art. 28, accord de traitement, DPO / délégué à la protection des données, registre | RGPD, DPA, DPO, sous-traitance | « Conforme RGPD » n'est pas une réponse : citer les mesures de la base |
| Sous-traitants ultérieurs | sub-processors, tiers, fournisseurs ayant accès aux données | sous-traitants ultérieurs, annexe DPA | Si la base renvoie à une annexe, ne pas inventer la liste : « À valider » + annexe à joindre |
| Chiffrement | encryption at rest / in transit, TLS, HTTPS, AES, gestion des clés, KMS, BYOK | chiffrement, TLS, AES, clés | Ne pas promettre BYOK ou un HSM si la base ne le dit pas |
| Sauvegardes | backup, rétention, restauration | sauvegarde, restauration | Fréquence, rétention et test de restauration sont trois sous-questions |
| PRA / PCA | plan de reprise, continuité, DRP, BCP, RPO, RTO | continuité, reprise, RPO, RTO | « Testé » exige une date de test dans la base |
| Disponibilité | SLA, uptime, taux de service | disponibilité, SLA | Ne jamais arrondir (99,5 % ≠ 99,9 %) ni retirer l'exclusion des maintenances |
| Pentest | test d'intrusion, audit de sécurité, scan de vulnérabilités, bug bounty | intrusion, audit, vulnérabilité | Un scan automatique n'est pas un pentest. Communication du rapport = selon la base (souvent sous NDA) |
| Audit client | droit d'audit, audit sur site, visite | audit | Engagement contractuel : Hors base si absent, juridique à consulter |
| SSO / MFA | SAML, OIDC, Entra ID / Azure AD, Okta, 2FA, authentification forte | SSO, SAML, MFA, authentification | « Disponible » ≠ « imposé par défaut » |
| Accès internes | moindre privilège, PAM, bastion, revue des habilitations, départs | accès, habilitations, bastion | Un **nombre** (d'admins, de personnes) n'est jamais déduit |
| Incidents | notification de violation, délai d'alerte, CERT | incident, notification | Ne jamais raccourcir le délai de la base (48 h ne devient pas 24 h) |
| Journalisation | logs, traces, SIEM, conservation des journaux | journaux, logs | Durée exacte de la base |
| Développement | SDLC, secure coding, OWASP, revue de code, SAST / DAST | développement, code | — |
| Réversibilité | fin de contrat, export, restitution, suppression, portabilité | réversibilité, export, suppression | Formats et délai exacts de la base |
| Personnel | sensibilisation, formation sécurité, charte, phishing | sensibilisation, charte | — |
| Assurance | cyber-assurance, RC pro, montant de couverture | assurance | Montant = Direction financière, jamais estimé |
| IA | entraînement de modèles, usage des données par l'IA, LLM, sous-traitants IA | IA, intelligence artificielle, modèles | Question sensible : absent de la base = Hors base, **jamais « non » par défaut** |

## 4. Ce qu'on ne fait jamais
- Déduire une certification d'une autre (« hébergeur ISO 27001 » ne fait pas de l'éditeur un certifié).
- Transformer un « disponible » en « garanti », un « annuel » en « continu », un « sous NDA » en « fourni ».
- Répondre « Oui » ou « Non » à une question fermée quand la base ne tranche pas.
- Recopier une date périmée sans le signaler (certificat, dernier pentest, dernier test PRA de plus de 12 mois → « À valider »).
- Reprendre une réponse d'un ancien questionnaire rempli qui n'est pas dans la base validée.
- Mentionner un client, un incident ou un nom de collaborateur qui n'est pas dans la base.

## 5. Qui valide quoi (à confirmer par Triskell)
| Sujet | Valideur par défaut |
|---|---|
| Hébergement, chiffrement, accès, pentest, PRA, journaux, incidents | RSSI [nom à compléter par Triskell] |
| RGPD, DPA, sous-traitants ultérieurs, usage des données par l'IA | DPO [nom à compléter par Triskell] |
| Audit sur site, pénalités, clauses, assurance | Juridique / Direction financière [à compléter par Triskell] |
| Fonctionnalités (SSO, MFA, export) | Direction technique / produit [à compléter par Triskell] |

## 6. Questionnaire hors Excel
- **Word / PDF** : reproduire le tableau dans le même ordre, avec les mêmes numéros, et les colonnes Réponse · Statut · Confiance · Source. Si le prospect a fourni un .docx à compléter, écrire dans une copie (python-docx), sans toucher aux questions.
- **Portail en ligne** (formulaire web) : livrer un tableau « N° · question copiée · réponse à coller · statut », dans l'ordre du portail.
- **Plusieurs feuilles** : traiter chaque feuille ; le script `remplir.py` gère les feuilles via le champ `feuille`.
