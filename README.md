# Kit IA Triskell : design system et skills ChatGPT

Ce dépôt réunit les outils remis à Triskell Software France pendant la formation IA (octobre 2026) :

- **1 design system** qui produit des présentations PowerPoint dans le modèle officiel Triskell et contrôle qu'un support respecte la charte ;
- **13 skills** pour les tâches qui reviennent chaque semaine, choisis à partir de vos réponses au sondage (synthèses, comptes rendus, présentations, mails, Excel, veille, support, avant-vente, traduction) ;
- **une bibliothèque de 12 prompts** prêts à copier (`bibliotheque-prompts-triskell.md` et `.pdf`) ;
- **des fichiers de test fictifs** et **le résultat obtenu sur chacun**, pour savoir à quoi vous attendre avant d'utiliser vos propres documents.

Chaque skill suit le format standard `SKILL.md` : un dossier qui contient les instructions et ses ressources (modèles, grilles, scripts, exemple). Le même dossier fonctionne dans ChatGPT Business et dans Claude.

---

## Les skills, par besoin

### Présentations
| Skill | Ce qu'il fait | Test |
|---|---|---|
| `triskell-design-system` | Crée un vrai .pptx dans le modèle officiel (Montserrat, orange `#FD7F01`, vert `#00897B`) à partir d'un brief ou de documents : 26 types de slides, 7 recettes (proposition commerciale, kick-off client, COPIL, revue trimestrielle, présentation produit, comité de direction, formation). Contrôle aussi un PPT existant et le remet aux normes. | « Fais une présentation de 8 slides pour le COPIL Alpha à partir de ce compte rendu » |
| `triskell-kickoff-dc-dsc` | Kick-off interne « Transition DC → DSC » : fiche de passation, contrôles de cohérence (licences, jrsH, échéancier, GEPIL), verdict GO / NO GO, deck et registre des informations manquantes par équipe. | `references/exemple-fiche.json` |

### Réunions et projets
| Skill | Ce qu'il fait | Test |
|---|---|---|
| `triskell-compte-rendu` | Transcription Teams ou notes → CR client, interne ou d'atelier + mail de suivi. Sépare ce qui part au client de ce qui reste en interne ; ne transforme jamais un « on peut » en engagement. | `demo3` |
| `triskell-synthese-copil` | Dernier CR + mails + notes → pack COPIL : engagements tenus ou non (avec preuve), météo projet, risques, décisions attendues, ordre du jour, plan de slides prêt pour le design system. | les 3 fichiers `demo2-*-alpha` |
| `triskell-synthese-documents` | Un ou plusieurs documents → synthèse pour la direction, l'opérationnel ou le client. Chaque affirmation est sourcée, les contradictions entre documents sont signalées. | `demo2` + `demo3` |

### Mails
| Skill | Ce qu'il fait | Test |
|---|---|---|
| `triskell-emails` | Trie une boîte (à traiter, pour info, à déléguer), répond à un fil en 3 tons, prépare les relances et les mails difficiles (réclamation, refus, retard). Brouillons uniquement, aucun engagement de date ou de prix. | `demo7` |

### Excel
| Skill | Ce qu'il fait | Test |
|---|---|---|
| `triskell-excel-analyse` | Comprend un fichier, répond à la question, liste chaque correction de données, livre une copie propre avec un onglet Synthèse et des graphiques. Explique et écrit des formules (version française, séparateur `;`). Vos onglets d'origine ne sont jamais modifiés. | `demo5` |

### Avant-vente et sécurité
| Skill | Ce qu'il fait | Test |
|---|---|---|
| `triskell-reponse-appel-offres` | Analyse un appel d'offres (dates, critères, pièces, points éliminatoires), grille go / no-go, matrice de conformité exigence par exigence, questions à poser à l'acheteur, plan du mémoire technique. Ne rédige qu'à partir de vos documents joints. | `demo1-appel-offres` |
| `triskell-questionnaire-securite` | Remplit le fichier Excel du prospect à partir de votre base de réponses validées. Chaque réponse est « Validé », « À valider » ou « Hors base », avec sa source. La version client ne sort que quand tout est validé. | `demo1-questionnaire` + `demo1-base-reponses` |
| `triskell-document-modele` | Document source + modèle → nouveau document Word qui garde la mise en forme du modèle (courrier, note, procédure, adaptation à un autre client). Les manques sont surlignés. | `demo4` |

### Support, marketing, veille, traduction
| Skill | Ce qu'il fait | Test |
|---|---|---|
| `triskell-reponse-support` | Ticket → type et priorité proposés, réponse client, note d'escalade pour l'équipe technique, proposition d'article d'aide. Ne confirme pas un bug avant reproduction, ne promet ni date ni correctif. | `demo2-tickets` |
| `triskell-webinaire-contenus` | Transcription d'un replay → article de blog, 3 posts LinkedIn, newsletter, 5 extraits horodatés, FAQ. Citations mot pour mot, rien n'est publié sans l'accord écrit des intervenants. | `demo6` |
| `triskell-veille-ppm` | Veille datée et sourcée sur le marché PPM et les concurrents. Contient le texte de la tâche planifiée à coller pour la recevoir chaque lundi. | « Veille PPM de la semaine » |
| `triskell-traduction` | FR ↔ EN, ES et DE sur demande, avec un glossaire PPM. Adapte le registre (contrat, support, marketing, textes d'interface avec limite de longueur) et liste les choix faits. | un mail de `demo2-tickets` |

Les résultats obtenus sur les fichiers de test sont dans `exemples/resultats/`. La veille a été testée sur l'actualité réelle du 19/10/2026 (`exemple-reel-veille-ppm-2026-10-19.md`).

---

## Installer un skill dans ChatGPT Business

1. Téléchargez le `.zip` du skill dans le dossier `zips/`.
2. Dans ChatGPT : **Skills › Create › Upload**, puis choisissez le `.zip`. L'administrateur de l'espace peut avoir à autoriser l'import.
3. Ouvrez une nouvelle conversation et faites la demande de test du tableau, avec le fichier fictif correspondant.

**Si l'import n'est pas proposé** : ouvrez le `SKILL.md`, copiez son contenu et recréez le skill avec le skill creator de ChatGPT, en joignant les fichiers des dossiers `references/`, `scripts/` et `assets/`.

**Les skills qui fabriquent un fichier** (design system, kick-off, Excel, questionnaire sécurité, document modèle, appel d'offres) utilisent des scripts Python. Ils ont été testés hors de ChatGPT. Faites un premier essai avec le fichier de test : si ChatGPT n'exécute pas le script, le skill livre le contenu (plan, tableau, texte) et indique comment obtenir le fichier.

## Rendre un skill plus précis

Chaque `SKILL.md` se termine par une section « Pour affiner le skill » : la liste des documents Triskell à joindre au projet ChatGPT (base de réponses sécurité, SLA, signature mail, glossaire produit, modèles de CR…). Les endroits qui attendent vos informations sont marqués `[à compléter par Triskell]`.

Pour adapter un skill à un autre métier : joignez son `SKILL.md` au skill creator et demandez « Adapte ce skill à [votre tâche] ».

## Trois règles avant tout envoi

1. **Relisez les chiffres et les noms.** Les skills n'inventent rien et laissent `[à compléter]` quand une information manque, mais la relecture reste humaine.
2. **Données réelles = espace ChatGPT Business de Triskell uniquement**, jamais un compte personnel.
3. **Corrigez la demande, pas le fichier.** Pour un PowerPoint ou un Excel généré, corrigez la consigne ou le plan, puis régénérez.

## Arborescence

```
design-system/triskell-design-system/   le design system
skills/                                 les 13 skills, un dossier chacun
zips/                                   un .zip prêt à importer par skill
exemples/fichiers-de-test/              documents fictifs pour tester
exemples/resultats/                     ce que chaque skill a produit sur ces documents
```

---

Documents d'exemple : tous fictifs, créés pour la formation (l'éditeur y est parfois appelé « Nova Software »). Aucune donnée réelle de Triskell ou de ses clients.
