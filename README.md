# Kit IA Triskell : design system et skills ChatGPT

Ce dépôt réunit les outils remis à Triskell Software France pendant la formation IA (octobre 2026) :

- **1 design system** qui produit des présentations PowerPoint dans le modèle officiel Triskell et contrôle qu'un support respecte la charte ;
- **7 skills** prêts à l'emploi pour les tâches qui reviennent chaque semaine ;
- **des fichiers de test fictifs** pour essayer chaque skill sans toucher à une donnée réelle.

Chaque skill suit le format standard `SKILL.md` : un dossier qui contient les instructions et, si besoin, des ressources (modèle, scripts, références). Le même dossier fonctionne dans ChatGPT Business et dans Claude.

---

## Ce qu'il y a dedans

### Le design system

| Skill | Ce qu'il fait | Exemple de demande |
|---|---|---|
| `triskell-design-system` | Crée un vrai fichier .pptx dans le modèle officiel (couverture, séparateurs verts, « MERCI ! »), à partir d'un brief ou de documents. 26 types de slides, 7 recettes prêtes. Contrôle aussi un PPT existant et le remet aux normes. | « Fais-moi une présentation de 8 slides pour le COPIL du projet Alpha, à partir de ce compte rendu » |

Les 7 recettes : proposition commerciale, kick-off client, COPIL, revue trimestrielle, présentation produit, comité de direction, formation.

La charte appliquée vient du modèle « Kickoff interne TSF » : police **Montserrat**, orange `#FD7F01`, vert canard `#00897B`, texte `#3F3F3F`, format 16:9. Les valeurs exactes sont dans `design-system/triskell-design-system/tokens/tokens.json`, les règles dans `references/charte.md`.

### Les 7 skills

| Skill | Ce qu'il fait | Fichier de test |
|---|---|---|
| `triskell-kickoff-dc-dsc` | Prépare le kick-off interne « Transition DC → DSC » : remplit la fiche de passation à partir de la proposition, du bon de commande et des échanges, croise les chiffres (licences, jrsH, échéancier, GEPIL), donne un verdict GO / NO GO, produit le deck dans le modèle officiel et le registre des informations manquantes par équipe. | `skills/triskell-kickoff-dc-dsc/references/exemple-fiche.json` |
| `triskell-compte-rendu` | Transcription Teams ou notes → compte rendu au format Triskell + mail de suivi. | `demo3-transcription-teams-alpha` |
| `triskell-synthese-copil` | Dernier CR + mails + notes → état du projet, risques, décisions attendues, ordre du jour, plan de présentation. | les 3 fichiers `demo2-*-alpha` |
| `triskell-reponse-support` | Ticket client → réponse, note interne et proposition d'article d'aide. | `demo2-tickets-support-fictifs` |
| `triskell-questionnaire-securite` | Pré-remplit un questionnaire sécurité / RGPD / ISO 27001 à partir de la base de réponses validées ; marque « à valider » ce qu'il ne sait pas. | `demo1-questionnaire-securite-prospect` + `demo1-base-reponses-securite` |
| `triskell-document-modele` | Document source + modèle → nouveau document (courrier, note, procédure, mode opératoire). | `demo4-courrier-helianthe-et-modele` |
| `triskell-veille-ppm` | Veille sourcée et datée sur le marché PPM et les concurrents. Se prête bien à une tâche planifiée chaque lundi. | « Veille PPM de la semaine » |

---

## Installer un skill dans ChatGPT Business

1. Téléchargez le fichier `.zip` du skill dans le dossier `zips/`.
2. Dans ChatGPT, ouvrez la gestion des skills (menu de votre profil ou des paramètres de l'espace, selon l'affichage de votre compte) et importez le `.zip`.
3. Ouvrez une nouvelle conversation et faites la demande d'exemple du tableau ci-dessus, avec le fichier de test correspondant.

**Si l'import d'un .zip n'est pas proposé dans votre espace** : ouvrez le fichier `SKILL.md` du skill, copiez son contenu et recréez le skill avec le « skill creator » de ChatGPT. Pour le design system et le kick-off, joignez aussi les fichiers du dossier (`assets/`, `scripts/`, `references/`, `tokens/`, `recettes/`) : ce sont eux qui garantissent le modèle officiel.

**Pour le design system et le kick-off**, l'exécution de code doit être active dans la conversation : c'est elle qui fabrique le .pptx. Sans elle, le skill livre le plan de la présentation et explique comment générer le fichier.

---

## Arborescence

```
design-system/triskell-design-system/   le design system (SKILL.md, modèle, moteur, recettes, charte)
skills/                                 les 7 skills, un dossier chacun
zips/                                   un .zip prêt à importer par skill
exemples/resultats/                     ce que produisent le design system et le kick-off (données fictives)
exemples/fichiers-de-test/              documents fictifs pour tester chaque skill
```

## Adapter un skill à votre métier

Un skill est un texte : ouvrez le `SKILL.md`, changez la description (elle décide quand le skill se déclenche) et les étapes, puis réimportez-le. Le plus simple : demandez au skill creator « Adapte ce skill à [votre tâche] » en joignant le `SKILL.md`.

## Trois règles avant tout envoi

1. **Relisez les chiffres et les noms** : les skills ne doivent rien inventer et laissent « [à compléter] » quand une information manque, mais la relecture reste humaine.
2. **Données réelles = espace ChatGPT Business de Triskell uniquement**, jamais un compte personnel.
3. **Ne retouchez pas le .pptx à la main** pour corriger le fond : corrigez la demande ou le plan, puis régénérez.

---

Documents d'exemple : tous fictifs, créés pour la formation. Aucune donnée réelle de Triskell ou de ses clients.
