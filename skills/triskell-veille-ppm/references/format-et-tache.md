# Format de la veille et tâche planifiée

## 1. Le format (1 page, rien de plus)

```
Veille PPM · semaine du [lundi JJ/MM] au [dimanche JJ/MM/AAAA]
Période couverte : [dates] · Recherche faite le [date] · [n] sources consultées

## Les 3 faits clés
1. [Concurrent] — [fait en une phrase] ([JJ/MM/AAAA], [Source](URL))
2. …
3. …
(moins de 3 faits dans la période : en écrire moins. Aucun : « Rien de nouveau cette semaine sur les concurrents suivis. »)

## Par concurrent
### Planisware
- [JJ/MM/AAAA] · [fait] · [Source](URL) · Fiabilité : officiel | presse | avis public
(ou : « Rien de nouveau sur la période. » + la dernière actualité connue avec sa date, en une ligne)
### Planview
### Sciforma (Planview ProjectAdvantage)
### Virage Group
### [Autres : à compléter par Triskell]

## Signaux marché
- [JJ/MM/AAAA] · [tendance, étude, classement, mouvement] · [Source](URL)

## À venir (dates annoncées officiellement)
- [JJ/MM/AAAA] · [événement] · [Source](URL)

## Et pour Triskell ?
3 questions au plus, pour la réunion d'équipe. Des questions, pas des conclusions.
- « [Concurrent] annonce [X] : est-ce que nos clients nous en parlent ? »

## Écartés
[Éléments vus mais non retenus, en une ligne chacun : hors période, source non fiable, non vérifiable.]
```

## 2. Règles de tri
- **Date + URL pour chaque élément.** Un élément sans date de publication vérifiable ne figure pas dans les faits ; s'il n'a qu'un mois (ex. « version d'octobre 2026 »), écrire le mois.
- **Période** : hebdomadaire = du lundi au dimanche précédents. Ignorer tout ce qui a plus de 30 jours, sauf demande explicite ou rubrique « À venir ». Premier passage ou demande « ce mois-ci » : 30 jours.
- **Date de l'événement ≠ date de l'article** : retenir la date de l'annonce officielle. Un article récent sur une annonce ancienne n'est pas une nouveauté.
- **Pas de rumeur** : pas de « selon nos informations », pas de comparatif d'un autre éditeur, pas de post de salarié, pas d'agrégateur de données (effectifs estimés, « nombre de clients » d'un site tiers). Une feuille de route n'est retenue que si l'éditeur l'a publiée.
- **Recopier les chiffres tels quels**, avec leur périmètre (« 51,0 M€, +13,6 % à taux de change constants, T1 2026 »).
- **Publications de routine ignorées** : nombre d'actions et droits de vote, contrat de liquidité, simples mises à jour de mentions légales.
- **Un fait = une source primaire** si elle existe : si la presse reprend un communiqué, citer le communiqué.
- **« Rien de nouveau » est une bonne réponse.** Ne jamais remplir avec du contenu ancien présenté comme nouveau.
- **Et pour Triskell ?** : jamais d'affirmation sur l'offre, les prix, les clients ou la feuille de route de Triskell. Des questions que l'équipe tranche.

## 3. Contrôle avant d'envoyer
- [ ] Chaque ligne a une date et un lien cliquable.
- [ ] Aucune date hors période (sauf « À venir » et « Écartés »).
- [ ] Les liens ouverts mènent bien à la page citée (pas à une page d'accueil).
- [ ] Chiffres identiques à la source.
- [ ] Une page maximum.

## 4. Tâche planifiée ChatGPT (chaque lundi)
Dans ChatGPT Business : ouvrir le projet « Veille » (avec `sources.md` et les documents listés), puis créer une tâche planifiée **chaque lundi à 8 h 00**, et coller ce texte :

> Utilise le skill triskell-veille-ppm. Fais la veille PPM de la semaine écoulée (du lundi au dimanche précédents) sur les concurrents suivis de Triskell : Planisware, Planview, Sciforma (désormais Planview ProjectAdvantage), Virage Group, et ceux listés dans le fichier des sources du projet. Utilise la recherche web et les sources du fichier « sources ». Règles : chaque élément a sa date de publication et son lien ; rien de plus de 30 jours, sauf la rubrique « À venir » ; pas de rumeur, pas de comparatif d'un autre éditeur, pas de chiffre d'agrégateur ; si rien de nouveau, écris-le. Format du skill : les 3 faits clés, par concurrent, signaux marché, à venir, « Et pour Triskell ? » (3 questions, pas de conclusions), écartés. Une page maximum, en français.

Conseils : la tâche planifiée s'exécute sans personne pour répondre, donc elle ne pose pas de question ; si une source est inaccessible, elle le signale dans « Écartés ». Relire le premier lundi, puis ajuster `sources.md` plutôt que le texte de la tâche.

## 5. Sans recherche web
Si la recherche web n'est pas disponible dans la conversation, ne produis aucune veille à partir de tes connaissances : dis-le en une phrase et propose de traiter les articles ou liens que l'utilisateur colle.
