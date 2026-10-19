# Exemple fictif : 5 lignes de matrice et leur raisonnement

> AO fictif « Groupe Hélianthe Industrie, HI-2026-014 » ; seul document éditeur joint : une base de réponses sécurité fictive (éditeur « Nova Software »). Analyse complète au format du script : `exemple-analyse.json`.

| N° | Niveau | Exigence (texte du CDC) | Réponse proposée | Statut | Source | Pourquoi ce statut |
|---|---|---|---|---|---|---|
| EX-16 | Obligatoire | Authentification unique (SSO) avec Microsoft Entra ID. | L'authentification unique est assurée via SAML 2.0, compatible Microsoft Entra ID, Okta et Google Workspace. L'authentification multifacteur est disponible et peut être imposée par l'administrateur client. | Couvert | Base sécurité, § 6 | La source cite explicitement Entra ID |
| EX-20 | Obligatoire | Disponibilité de la solution d'au moins 99,5 % par mois. | Engagement contractuel de disponibilité de 99,5 % par mois, hors maintenances planifiées annoncées 5 jours ouvrés à l'avance. | Partiel | Base sécurité, § 5 | La source ajoute une exclusion absente du CDC : on ne la retire pas, on pose la question à l'acheteur |
| EX-10 | Obligatoire | Export des données financières au format Excel. | [à compléter] La base jointe ne mentionne qu'un export complet en CSV et JSON (réversibilité). | À vérifier | Base sécurité, § 13 (partiel) | CSV ≠ « format Excel » : source ambiguë |
| EX-17 | Obligatoire | Gestion fine des droits d'accès par profil, par projet et par entité. | [à compléter] | À vérifier | — | Le § 7 de la base parle des accès internes de l'éditeur, pas des droits des utilisateurs clients |
| EX-02 | Obligatoire | La solution doit permettre de prioriser les projets selon des critères pondérés définis par le client. | [à compléter] | À vérifier | — | Aucune base fonctionnelle jointe : aucune réponse rédigée, même si la fonction semble « standard » |

**Question à l'acheteur issue de EX-20** : « Le taux de disponibilité de 99,5 % par mois s'entend-il hors maintenances planifiées annoncées à l'avance ? »

**Ce qu'il ne faut pas faire** : écrire pour EX-02 « Oui, la solution propose une priorisation multicritère paramétrable » parce que c'est probable pour un logiciel PPM. Sans document joint, c'est une invention qui engage l'entreprise.
