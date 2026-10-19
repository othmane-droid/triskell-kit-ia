# Exemple fictif — questionnaire sécurité (skill `triskell-questionnaire-securite`)

> Test du 19/10/2026 sur `demo1-questionnaire-securite-prospect.xlsx` + `demo1-base-reponses-securite.docx` (documents fictifs, aucune donnée réelle).
> Fichiers produits : `exemple-fictif-questionnaire-securite.xlsx` (copie de travail) · `exemple-fictif-questionnaire-securite.json` (les réponses préparées, entrée du script).

---

**25 questions : 19 Validé, 2 À valider, 4 Hors base.** Base utilisée : Nova Software, validée par le RSSI le 15/06/2026 (moins de 12 mois, OK).

**Fichier de travail** : `Alpha Industrie - Questionnaire sécurité - travail - 261019.xlsx` (ici `exemple-fictif-questionnaire-securite.xlsx`). Structure du prospect inchangée ; colonne « Réponse du fournisseur » remplie ; colonne « Source » du prospect remplie uniquement avec les justificatifs cités par la base (certificat ISO, synthèse pentest, DPA) ; 4 colonnes internes + feuille « Synthèse interne ».

**Les 3 points sensibles**
1. **Q24 — Usage des données pour entraîner des modèles d'IA** : absent de la base. Ne pas répondre « non » par défaut. → DPO + direction technique.
2. **Q25 — Audit sur site** : engagement contractuel absent de la base. → RSSI + juridique.
3. **Q23 — Assurance cyber et montant** : absent de la base. → Direction financière.

**Message prêt à envoyer**

> Objet : Questionnaire sécurité Groupe Alpha Industrie — 6 points à valider
> Bonjour [prénom],
> Le questionnaire Alpha Industrie est prérempli à partir de la base validée du 15/06/2026. Il me manque votre réponse sur ces points :
> 1. Q1 — Hébergement — Ce qu'il manque : le nom du fournisseur cloud. Proposition : la réponse B1 + « Fournisseur : [nom] ».
> 2. Q13 — Nombre d'administrateurs de production — absent de la base. Proposition : aucune.
> 3. Q16 — Liste des sous-traitants ultérieurs — la base renvoie à l'annexe du DPA. Proposition : joindre l'annexe à jour.
> 4. Q23 — Assurance cyber et montant — absent de la base. Proposition : aucune.
> 5. Q24 — Entraînement de modèles d'IA avec les données client — absent de la base. Proposition : aucune.
> 6. Q25 — Audit de sécurité sur site — absent de la base. Proposition : aucune.
> Le fichier de travail est joint (colonne « Statut » en orange et rouge). Merci de répondre directement dans la colonne Réponse.

**Vigilance** : Q17 (notification d'incident) reprend le délai de la base, 48 h. Si le prospect exige moins au contrat, c'est un arbitrage RSSI.

Rien ne part chez le prospect avant validation des lignes orange et rouges. La version à envoyer se produit ensuite avec `remplir.py … --client` (le script la refuse tant qu'il reste une ligne non validée : vérifié, refus sur les lignes 5, 17, 20, 27, 28, 29).
