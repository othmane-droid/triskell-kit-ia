# Charte des présentations Triskell Software France

> Relevée dans le modèle officiel « Kickoff interne TSF » (thème Office, masque et 9 dispositions), octobre 2026. Les valeurs exactes sont dans `tokens/tokens.json`. En cas de doute, le fichier `assets/template-triskell.pptx` fait foi.

## 1. L'ADN en une phrase
Un fond clair et aéré, un titre sobre souligné d'un **trait de pinceau orange**, une **trame de points gris** en coin, des séparateurs de section en **photo sous voile vert canard** avec le symbole Triskell en blanc. L'orange signale, le vert structure, le gris laisse respirer.

## 2. Format et grille
- 16:9, 33,87 × 19,05 cm.
- Titre de slide : en haut à gauche (0,79 cm ; 0,59 cm), 24 pt gras, couleur texte `#3F3F3F`.
- Trait de pinceau orange `#FF7200` sous le titre (1,23 cm ; 2,38 cm), 3,15 × 0,30 cm : il est dans la disposition, ne pas le redessiner.
- Zone de contenu : x 0,95 → 30,55 cm ; y 3,3 → 17,5 cm. À droite de 30,55 cm, la trame de points du masque occupe le haut de la slide ; sous 17,5 cm, le logo Triskell occupe le coin bas droit (29,8 cm ; 17,8 cm).
- Marges intérieures des blocs : 0,5 cm. Écart entre colonnes : 0,8 à 1,2 cm.

## 3. Les 9 dispositions du masque
| N° | Nom dans PowerPoint | Usage | Type du moteur |
|---|---|---|---|
| 0 | 2_Disposition personnalisée | Couverture : sur-titre vert, titre bleu nuit 44 pt, date et version, photo à droite, logo couleur en bas à droite | `cover` |
| 1 | Contenu hierarchie | Slide de contenu standard (trame de points, titre, trait orange, logo) | presque tous |
| 2 | Contenu Simple | Variante de contenu | — |
| 3 | 1_Blank (titre seul) | Contenu sans trame de points | — |
| 6 | 1_Blank (points + logo) | Agenda : « Agenda » 66 pt orange ExtraBold, liste numérotée 20 pt gras, « Q&A » | `agenda` |
| 7 | 1_Blank (MERCI !) | Fin : « MERCI ! » 72 pt vert | `closing` |
| 8 | Transition-vert | Séparateur : photo + voile vert 88 %, symbole blanc, titre blanc ~50 pt | `section` |

## 4. Couleurs et rôles
| Jeton | Hex | Rôle |
|---|---|---|
| orange | `#FD7F01` | Intertitres de bloc (niveau 1 du masque), UN chiffre ou mot d'attention par slide, « [à compléter] » |
| orange_pinceau | `#FF7200` | Trait sous les titres (déjà dans le masque) |
| orange_tableau | `#FC8B00` | En-tête des tableaux financiers et de données |
| vert | `#00897B` | Voile des séparateurs, sous-titre de couverture, rôles et porteurs, en-tête des tableaux d'actions |
| vert_clair | `#4DB6AC` | Deuxième série, phases secondaires |
| fond_doux | `#E6F5F3` | Fond des cartes |
| fond_orange | `#FFF3E6` | Fond de la carte mise en avant (une seule) |
| texte_titre | `#1A2832` | Titre de couverture, grands chiffres |
| texte | `#3F3F3F` | Titres et texte courant |
| texte_secondaire | `#5F6B73` | Valeurs, descriptions |
| texte_attenue | `#9AA3A9` | En-têtes de colonnes discrets, sources, éléments d'agenda non actifs |
| gris_fond | `#F2F2F2` | Lignes alternées |
| rouge | `#E04E5F` | Statut « Non », verdict « NO GO ». Rien d'autre. |
| jaune | `#FFC127` | Graphiques uniquement, 3ᵉ série |

Ordre des séries dans un graphique : vert, orange, vert clair, jaune, gris atténué.

## 5. Typographie
- **Montserrat** (texte), **Montserrat SemiBold** (titres, police « majeure » du thème), **Montserrat ExtraBold** (agenda, grands chiffres). Repli : Arial.
- Échelle : couverture 44 / 24 · titre de slide 24 · intertitre 18 gras orange · texte 14 à 17 · dense 12 · source 10 · chiffre clé 48.
- Jamais de texte sous 10 pt. Jamais de capitales sur plus de 4 mots (sauf sur-titres de carte en 12 pt).

## 6. Les éléments signature
1. **Trait de pinceau orange** sous chaque titre de contenu (masque).
2. **Trame de points gris** en coin (masque).
3. **Séparateur vert** : numéroté (« 1. Éléments de contexte ») pour rythmer ; au plus 6 slides de contenu entre deux séparateurs.
4. **Pastilles Oui / Non** (vert coche, rouge croix) : `assets/icone-oui.png`, `assets/icone-non.png`. C'est le langage des check-lists Triskell (« GO Projet », consentements marketing).
5. **Valeur à compléter** : « [à compléter] » en orange italique. C'est la convention Triskell pour un champ attendu ; le moteur l'applique à toute valeur vide.

## 6 bis. La grammaire des slides de contenu
- **Panneau** : fond `panneau` (#F6F7F8) à coins arrondis, liseré d'accent de 2,2 cm en haut à gauche, intertitre 17 pt dans la couleur d'accent. C'est la brique de base : elle structure sans alourdir.
- **Disque numéroté** (vert, orange pour l'élément en cours ou mis en avant) : étapes, messages de synthèse, agenda, demandes.
- **Bloc vert plein** (texte blanc) : réservé à la décision attendue (`summary`) et au prochain rendez-vous (`cta`). Un seul par slide.
- **Fond orange doux** (#FFF3E6) : la carte, l'offre ou le chiffre mis en avant. Un seul par slide.
- **Accent dans le texte** : `**mot**` met un mot en orange gras. Un seul par slide.

## 7. Écriture
- **Un titre = un message.** « Le périmètre couvre 3 processus sur 5 » plutôt que « Périmètre fonctionnel ». Exception admise : les slides de fiche (kick-off, participants) gardent un titre descriptif, c'est l'usage du modèle.
- Vocabulaire maison à respecter tel quel : DC (Direction Commerciale), DSC (Direction Succès Client), ADV (Administration des Ventes), CSM, DP (directeur de projet), AVV (avant-vente), MKG ; jrsH (jours-homme), F / NF (facturable / non facturable) ; GEPIL, SKORAN, HubSpot ; PPM.
- Phrases courtes, sans point final dans les puces, vouvoiement pour tout support client.
- Chaque chiffre a sa source. Un montant porte HT ou TTC.

## 8. Interdits
- Toute couleur ou police hors charte.
- Dégradés, ombres portées, clipart, emojis, images générées de personnes réelles ou de logos clients.
- Les consignes du modèle oubliées : « A MODIFIER », « Insérer le planning… », « LOGO CLIENT A INSERER », « NOM CLIENT », « xxx », « Version x.x », « 202x-xxx ».
- Plus d'un élément orange d'attention par slide.
- Une capture d'outil interne inventée ou « reconstituée ».

## 9. Logos
- `assets/logo-triskell-couleur.png` : fonds clairs (déjà présent sur les dispositions de contenu, de couverture et de fin).
- `assets/logo-triskell-blanc.png` et `assets/symbole-triskell-blanc.png` : fonds verts ou photo. Ne jamais déformer ni recolorer.
- Logo client : uniquement s'il est fourni par l'utilisateur ; sinon le nom du client en vert sur la couverture.
