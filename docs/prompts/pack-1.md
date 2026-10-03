# Pack d'images · La cuisine

**70 images, une par asset.** Chaque bloc donne le nom du fichier, le format exact en pixels, la place que l'objet doit prendre dans l'image et la taille à laquelle il sera affiché dans la scène.

## Mode d'emploi

1. Génère d'abord **le plan de travail**, puis **une première pose de chaque personnage** (`commis-goute.png` et `chef-attend.png`).
2. Pour **toutes les autres images**, joins en image de référence le plan de travail et, pour un personnage, sa première pose réussie. Ajoute cette phrase à la fin du prompt : « Keep exactly the same clay style, lighting, camera angle and character design as the reference images. »
3. **Une image = un seul objet**, fond transparent (ou blanc pur #FFFFFF si ton outil ne sait pas faire).
4. Si ton outil le permet, génère **au double** de la taille indiquée (par exemple 2048 × 2048 au lieu de 1024 × 1024) : c'est plus net.
5. Dépose les fichiers dans `sources/brut/` **avec exactement le nom indiqué**, puis lance `python outils/images/preparer_images.py` (détourage, mise à l'échelle, tailles.js).

Les formats utilisés :

| Format | Pixels | Pour quoi |
|---|---|---|
| 16:9 | 1920 × 1080 (ou 2560 × 1440) | le fond |
| 1:1 | 1024 × 1024 | les objets ronds ou compacts |
| 3:2 | 1536 × 1024 | les objets longs : planche, couteau, poêles, plateau, bacs larges |
| 2:3 | 1024 × 1536 | tout ce qui est debout : les personnages, la porte, le téléphone, la poubelle |

## Sommaire

| # | Fichier | Asset | Format | Place dans l'image | Affiché dans la scène |
|---|---|---|---|---|---|
| | **Le fond (sert à toutes les notions)** | | | | |
| 1 | `plan-de-travail.png` | Le plan de travail | 16:9 · 1920 × 1080 px (ou 2560 × 1440) | toute l’image | plein écran, 1900 × 1069 px |
| | **RAG · la tarte de la maison** | | | | |
| 2 | `cocotte.png` | La cocotte (grande préparation) | 1:1 · 1024 × 1024 px | 75 % | 250 px de large |
| 3 | `saladier.png` | Le saladier (grande préparation) | 1:1 · 1024 × 1024 px | 75 % | 210 px de large |
| 4 | `marmite.png` | La marmite (grande préparation) | 1:1 · 1024 × 1024 px | 75 % | 220 px de large |
| 5 | `pichet.png` | Le pichet (grande préparation) | 1:1 · 1024 × 1024 px | 65 % | 150 px de large |
| 6 | `bocal.png` | Le bocal étiqueté | 1:1 · 1024 × 1024 px | 70 % de la hauteur | 96 px de large |
| 7 | `ticket.png` | Le ticket de commande | 1:1 · 1024 × 1024 px | 65 % de la hauteur | 150 px de large |
| 8 | `plateau.png` | Le plateau de service | 3:2 · 1536 × 1024 px | 85 % de la largeur | 380 px de large |
| 9 | `tarte.png` | La tarte de la maison | 1:1 · 1024 × 1024 px | 75 % | 220 px de large |
| 10 | `tarte-pommes.png` | La tarte ratée (sans RAG) | 1:1 · 1024 × 1024 px | 75 % | 220 px de large |
| 11 | `commis-goute.png` | Commis · il goûte | 2:3 · 1024 × 1536 px | 88 % de la hauteur | 330 px de haut |
| 12 | `commis-ecrit.png` | Commis · il étiquette | 2:3 · 1024 × 1536 px | 88 % de la hauteur | 330 px de haut |
| 13 | `commis-range.png` | Commis · il range | 2:3 · 1024 × 1536 px | 88 % de la hauteur | 330 px de haut |
| 14 | `commis-imagine.png` | Commis · il imagine le goût | 2:3 · 1024 × 1536 px | 88 % de la hauteur | 330 px de haut |
| 15 | `chef-attend.png` | Chef · il attend | 2:3 · 1024 × 1536 px | 88 % de la hauteur | 370 px de haut |
| 16 | `chef-improvise.png` | Chef · il improvise (bluff) | 2:3 · 1024 × 1536 px | 88 % de la hauteur | 370 px de haut |
| 17 | `chef-cuisine.png` | Chef · il cuisine | 2:3 · 1024 × 1536 px | 88 % de la hauteur | 370 px de haut |
| | **Token · la planche à découper** | | | | |
| 18 | `planche.png` | La planche à découper | 3:2 · 1536 × 1024 px | 85 % de la largeur | 440 px de large |
| 19 | `couteau.png` | Le couteau de chef | 3:2 · 1536 × 1024 px | 80 % de la largeur | 220 px de large |
| 20 | `de-creme.png` | Dé vierge (creme) | 1:1 · 1024 × 1024 px | 45 % | 70 px de large |
| 21 | `de-tomate.png` | Dé vierge (tomate) | 1:1 · 1024 × 1024 px | 45 % | 70 px de large |
| 22 | `de-sarcelle.png` | Dé vierge (sarcelle) | 1:1 · 1024 × 1024 px | 45 % | 70 px de large |
| 23 | `de-moutarde.png` | Dé vierge (moutarde) | 1:1 · 1024 × 1024 px | 45 % | 70 px de large |
| 24 | `balance.png` | La balance de cuisine | 1:1 · 1024 × 1024 px | 75 % | 240 px de large |
| 25 | `carotte.png` | La carotte entière | 3:2 · 1536 × 1024 px | 75 % de la largeur | 200 px de large |
| | **Température · le feu sous la poêle** | | | | |
| 26 | `feu-eteint.png` | Le feu éteint | 1:1 · 1024 × 1024 px | 75 % | 230 px de large |
| 27 | `feu-doux.png` | Le feu doux | 1:1 · 1024 × 1024 px | 75 % | 230 px de large |
| 28 | `feu-vif.png` | Le feu vif | 1:1 · 1024 × 1024 px | 75 % | 230 px de large |
| 29 | `bouton.png` | Le bouton de gazinière | 1:1 · 1024 × 1024 px | 45 % | 90 px de large |
| 30 | `poele.png` | La poêle vide | 3:2 · 1536 × 1024 px | 85 % de la largeur | 300 px de large |
| 31 | `poele-steak.png` | La poêle, steak parfait | 3:2 · 1536 × 1024 px | 85 % de la largeur | 300 px de large |
| 32 | `poele-brule.png` | La poêle, plat brûlé | 3:2 · 1536 × 1024 px | 85 % de la largeur | 300 px de large |
| | **Fenêtre de contexte · le plan de travail qui déborde** | | | | |
| 33 | `poubelle.png` | La poubelle | 2:3 · 1024 × 1536 px | 75 % de la hauteur | 220 px de haut |
| 34 | `tomate.png` | La tomate | 1:1 · 1024 × 1024 px | 60 % | 110 px de large |
| 35 | `oignon.png` | L’oignon | 1:1 · 1024 × 1024 px | 60 % | 110 px de large |
| 36 | `citron.png` | Le citron | 1:1 · 1024 × 1024 px | 60 % | 110 px de large |
| 37 | `fromage.png` | Le fromage | 1:1 · 1024 × 1024 px | 60 % | 110 px de large |
| 38 | `oeufs.png` | Les œufs | 1:1 · 1024 × 1024 px | 60 % | 110 px de large |
| 39 | `beurre.png` | Le beurre | 1:1 · 1024 × 1024 px | 60 % | 110 px de large |
| | **Hallucination · sous la cloche** | | | | |
| 40 | `cloche-fermee.png` | La cloche fermée | 1:1 · 1024 × 1024 px | 75 % | 260 px de large |
| 41 | `cloche-ouverte.png` | La cloche ouverte, plat inventé | 1:1 · 1024 × 1024 px | 85 % | 300 px de large |
| | **Fine-tuning · le chef part en stage** | | | | |
| 42 | `livre.png` | Le gros livre de pâtisserie | 1:1 · 1024 × 1024 px | 70 % | 200 px de large |
| 43 | `gateau.png` | Le gâteau de retour de stage | 1:1 · 1024 × 1024 px | 70 % | 200 px de large |
| 44 | `chef-etudie.png` | Chef · il étudie | 2:3 · 1024 × 1536 px | 88 % de la hauteur | 370 px de haut |
| 45 | `chef-diplome.png` | Chef · de retour de stage | 2:3 · 1024 × 1536 px | 88 % de la hauteur | 370 px de haut |
| | **Appel d’outil · le chef demande, le commis va chercher** | | | | |
| 46 | `chambre-froide.png` | La porte de chambre froide | 2:3 · 1024 × 1536 px | 85 % de la hauteur | 520 px de haut |
| 47 | `telephone.png` | Le téléphone mural | 2:3 · 1024 × 1536 px | 60 % de la hauteur | 220 px de haut |
| 48 | `carnet.png` | Le carnet de bons | 1:1 · 1024 × 1024 px | 60 % | 150 px de large |
| 49 | `chef-appelle.png` | Chef · il appelle une commande | 2:3 · 1024 × 1536 px | 88 % de la hauteur | 370 px de haut |
| 50 | `commis-court.png` | Commis · il court chercher | 2:3 · 1024 × 1536 px | 88 % de la hauteur | 330 px de haut |
| 51 | `commis-telephone.png` | Commis · il téléphone | 2:3 · 1024 × 1536 px | 88 % de la hauteur | 330 px de haut |
| 52 | `commis-ecoute.png` | Commis · il écoute le chef | 2:3 · 1024 × 1536 px | 88 % de la hauteur | 330 px de haut |
| | **MCP · les bacs gastronormes** | | | | |
| 53 | `gn-1-1.png` | Bac GN 1/1 (entier) | 3:2 · 1536 × 1024 px | 85 % de la largeur | 300 px de large |
| 54 | `gn-1-2.png` | Bac GN 1/2 (demi) | 1:1 · 1024 × 1024 px | 70 % de la largeur | 180 px de large |
| 55 | `gn-1-3.png` | Bac GN 1/3 (tiers) | 3:2 · 1536 × 1024 px | 65 % de la largeur | 180 px de large |
| 56 | `gn-1-6.png` | Bac GN 1/6 (sixième) | 1:1 · 1024 × 1024 px | 55 % de la largeur | 100 px de large |
| 57 | `saladette.png` | La saladette réfrigérée | 3:2 · 1536 × 1024 px | 90 % de la largeur | 330 px de large |
| 58 | `four.png` | Le four mixte | 1:1 · 1024 × 1024 px | 80 % | 300 px de large |
| 59 | `bain-marie.png` | Le bain-marie | 3:2 · 1536 × 1024 px | 90 % de la largeur | 330 px de large |
| 60 | `boites-bricolees.png` | Les boîtes bricolées | 3:2 · 1536 × 1024 px | 85 % de la largeur | 300 px de large |
| 61 | `commis-porte-bac.png` | Commis · il porte un bac | 2:3 · 1024 × 1536 px | 88 % de la hauteur | 330 px de haut |
| | **Agent · le chef en plein coup de feu** | | | | |
| 62 | `minuteur.png` | Le minuteur | 1:1 · 1024 × 1024 px | 55 % | 110 px de large |
| 63 | `sonnette.png` | La sonnette de service | 1:1 · 1024 × 1024 px | 50 % | 110 px de large |
| 64 | `saliere.png` | La salière | 1:1 · 1024 × 1024 px | 50 % | 90 px de large |
| 65 | `chef-goute.png` | Chef · il goûte et grimace | 2:3 · 1024 × 1536 px | 88 % de la hauteur | 370 px de haut |
| 66 | `chef-sale.png` | Chef · il rectifie | 2:3 · 1024 × 1536 px | 88 % de la hauteur | 370 px de haut |
| 67 | `chef-content.png` | Chef · content | 2:3 · 1024 × 1536 px | 88 % de la hauteur | 370 px de haut |
| 68 | `chef-panique.png` | Chef · débordé | 2:3 · 1024 × 1536 px | 88 % de la hauteur | 370 px de haut |
| 69 | `commis-presente.png` | Commis · il présente l’assiette | 2:3 · 1024 × 1536 px | 88 % de la hauteur | 330 px de haut |
| 70 | `commis-coupe.png` | Commis · il coupe en dés | 2:3 · 1024 × 1536 px | 88 % de la hauteur | 330 px de haut |

---

## Le fond (sert à toutes les notions)

### 1. Le plan de travail

Fichier : `plan-de-travail.png` · Format : **16:9 · 1920 × 1080 px (ou 2560 × 1440)** · Place dans l'image : toute l’image · Affiché : plein écran, 1900 × 1069 px

```
Image format: exactly 16:9 landscape, 1920 x 1080 pixels (or 2560 x 1440 if possible). A long empty kitchen countertop seen from above at a high angle, filling the ENTIRE image edge to edge: the left two thirds are warm light wood butcher block #D9A66B, the right third is a smooth white marble slab #EDEAE3 with soft grey veins #BDB7AC. Along the very top edge only, a thin strip of cream #F6EFE2 square wall tiles with a horizontal steel ticket rail. The countertop surface takes at least 85 % of the image height. Completely empty and tidy: no object, no food, no utensil. Framing: the countertop fills the frame edge to edge, lots of free space. Camera: high angle, almost top-down, about 75 degrees. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: none, the countertop itself fills the entire image.
```

---

## RAG · la tarte de la maison

### 2. La cocotte (grande préparation)

Fichier : `cocotte.png` · Format : **1:1 · 1024 × 1024 px** · Place dans l'image : 75 % · Affiché : 250 px de large

```
Image format: exactly 1:1 square, 1024 x 1024 pixels. A big round cast-iron casserole pot in tomato red #D8432B with its lid on and a dark ink #2A2A2E knob, two small handles. Framing: the object alone, centred, fully visible, nothing cropped, filling about 75 % of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 3. Le saladier (grande préparation)

Fichier : `saladier.png` · Format : **1:1 · 1024 × 1024 px** · Place dans l'image : 75 % · Affiché : 210 px de large

```
Image format: exactly 1:1 square, 1024 x 1024 pixels. A large round ceramic mixing bowl, cream #F6EFE2 inside with a teal #2B8C83 rim, filled with a smooth cream-coloured preparation. Framing: the object alone, centred, fully visible, nothing cropped, filling about 75 % of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 4. La marmite (grande préparation)

Fichier : `marmite.png` · Format : **1:1 · 1024 × 1024 px** · Place dans l'image : 75 % · Affiché : 220 px de large

```
Image format: exactly 1:1 square, 1024 x 1024 pixels. A tall brushed steel #C9CDD1 stock pot with two handles and no lid, filled with a golden mustard #E0A21B preparation, a wooden spoon resting inside. Framing: the object alone, centred, fully visible, nothing cropped, filling about 75 % of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 5. Le pichet (grande préparation)

Fichier : `pichet.png` · Format : **1:1 · 1024 × 1024 px** · Place dans l'image : 65 % · Affiché : 150 px de large

```
Image format: exactly 1:1 square, 1024 x 1024 pixels. A teal #2B8C83 ceramic jug with a handle, filled with a deep red sauce. Framing: the object alone, centred, fully visible, nothing cropped, filling about 65 % of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 6. Le bocal étiqueté

Fichier : `bocal.png` · Format : **1:1 · 1024 × 1024 px** · Place dans l'image : 70 % de la hauteur · Affiché : 96 px de large

```
Image format: exactly 1:1 square, 1024 x 1024 pixels. One round glass kitchen jar with a tomato red #D8432B clay lid, slightly bluish transparent glass, empty, and a blank strip of white masking tape stuck horizontally across the front of the jar (the tape is empty, nothing written). Framing: the object alone, centred, fully visible, nothing cropped, filling about 70 % de la hauteur of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 7. Le ticket de commande

Fichier : `ticket.png` · Format : **1:1 · 1024 × 1024 px** · Place dans l'image : 65 % de la hauteur · Affiché : 150 px de large

```
Image format: exactly 1:1 square, 1024 x 1024 pixels. One small white paper kitchen order ticket, portrait orientation, slightly curled, with a thin tomato red #D8432B stripe at the top and nothing written on it, lying flat. Framing: the object alone, centred, fully visible, nothing cropped, filling about 65 % de la hauteur of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 8. Le plateau de service

Fichier : `plateau.png` · Format : **3:2 · 1536 × 1024 px** · Place dans l'image : 85 % de la largeur · Affiché : 380 px de large

```
Image format: exactly 3:2 landscape, 1536 x 1024 pixels. An empty rectangular serving tray in teal #2B8C83 clay with low rounded edges, lying flat. Framing: the object alone, centred, fully visible, nothing cropped, filling about 85 % de la largeur of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 9. La tarte de la maison

Fichier : `tarte.png` · Format : **1:1 · 1024 × 1024 px** · Place dans l'image : 75 % · Affiché : 220 px de large

```
Image format: exactly 1:1 square, 1024 x 1024 pixels. A round white plate with a slice of pear and almond tart: golden crust in mustard yellow #E0A21B, fanned pear slices in cream #F6EFE2, a few flaked almonds on top. Framing: the object alone, centred, fully visible, nothing cropped, filling about 75 % of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 10. La tarte ratée (sans RAG)

Fichier : `tarte-pommes.png` · Format : **1:1 · 1024 × 1024 px** · Place dans l'image : 75 % · Affiché : 220 px de large

```
Image format: exactly 1:1 square, 1024 x 1024 pixels. A round white plate with a slice of a very ordinary apple tart: pale crust, thin apple slices in a plain circle, nothing special, a bit sad-looking. Framing: the object alone, centred, fully visible, nothing cropped, filling about 75 % of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 11. Commis · il goûte

Fichier : `commis-goute.png` · Format : **2:3 · 1024 × 1536 px** · Place dans l'image : 88 % de la hauteur · Affiché : 330 px de haut

```
Image format: exactly 2:3 portrait, 1024 x 1536 pixels. The kitchen helper (commis): a small young cook made of clay, round friendly face with rosy cheeks, short dark #2A2A2E hair under a small cream #F6EFE2 paper cook cap, cream #F6EFE2 cook jacket, teal #2B8C83 apron, black trousers and shoes, rounded hands, simple black dot eyes. Exactly the same character in every image. Pose: standing, holding a small tasting spoon to his mouth, the other hand on his hip. Facial expression: eyes half closed in concentration, eyebrows slightly raised, lips pursed on the spoon, head tilted a little to the side, as if analysing a subtle taste. Framing: full body, head to feet fully visible, centred horizontally, the character's total height (including the hat) is exactly 88 % of the image height, the soles of the feet 6 % above the bottom edge, so that every pose of the series has the same size and the same ground line. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 12. Commis · il étiquette

Fichier : `commis-ecrit.png` · Format : **2:3 · 1024 × 1536 px** · Place dans l'image : 88 % de la hauteur · Affiché : 330 px de haut

```
Image format: exactly 2:3 portrait, 1024 x 1536 pixels. The kitchen helper (commis): a small young cook made of clay, round friendly face with rosy cheeks, short dark #2A2A2E hair under a small cream #F6EFE2 paper cook cap, cream #F6EFE2 cook jacket, teal #2B8C83 apron, black trousers and shoes, rounded hands, simple black dot eyes. Exactly the same character in every image. Pose: standing, leaning forward, writing with a black marker with a mustard yellow #E0A21B cap on a strip of masking tape stuck on a glass jar he holds in the other hand. Facial expression: focused, eyes looking down at the tape, tongue slightly out at the corner of the mouth, eyebrows drawn together. Framing: full body, head to feet fully visible, centred horizontally, the character's total height (including the hat) is exactly 88 % of the image height, the soles of the feet 6 % above the bottom edge, so that every pose of the series has the same size and the same ground line. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 13. Commis · il range

Fichier : `commis-range.png` · Format : **2:3 · 1024 × 1536 px** · Place dans l'image : 88 % de la hauteur · Affiché : 330 px de haut

```
Image format: exactly 2:3 portrait, 1024 x 1536 pixels. The kitchen helper (commis): a small young cook made of clay, round friendly face with rosy cheeks, short dark #2A2A2E hair under a small cream #F6EFE2 paper cook cap, cream #F6EFE2 cook jacket, teal #2B8C83 apron, black trousers and shoes, rounded hands, simple black dot eyes. Exactly the same character in every image. Pose: walking to the side, carrying one glass jar with a tomato red #D8432B lid in both hands in front of his chest. Facial expression: calm and confident, small smile, eyes looking ahead to where he will place the jar. Framing: full body, head to feet fully visible, centred horizontally, the character's total height (including the hat) is exactly 88 % of the image height, the soles of the feet 6 % above the bottom edge, so that every pose of the series has the same size and the same ground line. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 14. Commis · il imagine le goût

Fichier : `commis-imagine.png` · Format : **2:3 · 1024 × 1536 px** · Place dans l'image : 88 % de la hauteur · Affiché : 330 px de haut

```
Image format: exactly 2:3 portrait, 1024 x 1536 pixels. The kitchen helper (commis): a small young cook made of clay, round friendly face with rosy cheeks, short dark #2A2A2E hair under a small cream #F6EFE2 paper cook cap, cream #F6EFE2 cook jacket, teal #2B8C83 apron, black trousers and shoes, rounded hands, simple black dot eyes. Exactly the same character in every image. Pose: standing, holding a small white order ticket in one hand, the other hand touching his chin. Facial expression: eyes closed, dreamy smile, eyebrows raised, as if imagining a delicious taste. Framing: full body, head to feet fully visible, centred horizontally, the character's total height (including the hat) is exactly 88 % of the image height, the soles of the feet 6 % above the bottom edge, so that every pose of the series has the same size and the same ground line. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 15. Chef · il attend

Fichier : `chef-attend.png` · Format : **2:3 · 1024 × 1536 px** · Place dans l'image : 88 % de la hauteur · Affiché : 370 px de haut

```
Image format: exactly 2:3 portrait, 1024 x 1536 pixels. The head chef: a taller clay chef, round face with a big dark #2A2A2E moustache, tall cream #F6EFE2 toque, cream #F6EFE2 double-breasted jacket, tomato red #D8432B neckerchief, black trousers and shoes, rounded hands, simple black dot eyes. Exactly the same character in every image. Pose: standing still, arms crossed on his chest. Facial expression: neutral and ready, eyes looking forward, eyebrows relaxed, mouth closed under the moustache. Framing: full body, head to feet fully visible, centred horizontally, the character's total height (including the hat) is exactly 88 % of the image height, the soles of the feet 6 % above the bottom edge, so that every pose of the series has the same size and the same ground line. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 16. Chef · il improvise (bluff)

Fichier : `chef-improvise.png` · Format : **2:3 · 1024 × 1536 px** · Place dans l'image : 88 % de la hauteur · Affiché : 370 px de haut

```
Image format: exactly 2:3 portrait, 1024 x 1536 pixels. The head chef: a taller clay chef, round face with a big dark #2A2A2E moustache, tall cream #F6EFE2 toque, cream #F6EFE2 double-breasted jacket, tomato red #D8432B neckerchief, black trousers and shoes, rounded hands, simple black dot eyes. Exactly the same character in every image. Pose: standing, one hand scratching the back of his head under the toque, the other hand raised with the index finger up as if giving an answer anyway. Facial expression: overconfident bluff, big forced smile, one eyebrow raised, eyes looking sideways, one small sweat drop on the forehead. Framing: full body, head to feet fully visible, centred horizontally, the character's total height (including the hat) is exactly 88 % of the image height, the soles of the feet 6 % above the bottom edge, so that every pose of the series has the same size and the same ground line. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 17. Chef · il cuisine

Fichier : `chef-cuisine.png` · Format : **2:3 · 1024 × 1536 px** · Place dans l'image : 88 % de la hauteur · Affiché : 370 px de haut

```
Image format: exactly 2:3 portrait, 1024 x 1536 pixels. The head chef: a taller clay chef, round face with a big dark #2A2A2E moustache, tall cream #F6EFE2 toque, cream #F6EFE2 double-breasted jacket, tomato red #D8432B neckerchief, black trousers and shoes, rounded hands, simple black dot eyes. Exactly the same character in every image. Pose: standing, holding a frying pan with a wooden handle in one hand, reading a small white order ticket held in the other hand. Facial expression: satisfied and sure of himself, eyes on the ticket, small confident smile. Framing: full body, head to feet fully visible, centred horizontally, the character's total height (including the hat) is exactly 88 % of the image height, the soles of the feet 6 % above the bottom edge, so that every pose of the series has the same size and the same ground line. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

---

## Token · la planche à découper

### 18. La planche à découper

Fichier : `planche.png` · Format : **3:2 · 1536 × 1024 px** · Place dans l'image : 85 % de la largeur · Affiché : 440 px de large

```
Image format: exactly 3:2 landscape, 1536 x 1024 pixels. A large rectangular wooden cutting board in warm light wood #D9A66B with a darker rim and a small round handle hole, empty, lying flat. Framing: the object alone, centred, fully visible, nothing cropped, filling about 85 % de la largeur of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 19. Le couteau de chef

Fichier : `couteau.png` · Format : **3:2 · 1536 × 1024 px** · Place dans l'image : 80 % de la largeur · Affiché : 220 px de large

```
Image format: exactly 3:2 landscape, 1536 x 1024 pixels. A chef's knife lying flat, horizontal, blade pointing right, light grey steel blade with a soft shine, dark ink #2A2A2E handle with two small rivets. Framing: the object alone, centred, fully visible, nothing cropped, filling about 80 % de la largeur of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 20. Dé vierge (creme)

Fichier : `de-creme.png` · Format : **1:1 · 1024 × 1024 px** · Place dans l'image : 45 % · Affiché : 70 px de large

```
Image format: exactly 1:1 square, 1024 x 1024 pixels. One small clay cube like a diced vegetable piece, in cream #F6EFE2, completely plain on every face, slightly rounded edges. Framing: the object alone, centred, fully visible, nothing cropped, filling about 45 % of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 21. Dé vierge (tomate)

Fichier : `de-tomate.png` · Format : **1:1 · 1024 × 1024 px** · Place dans l'image : 45 % · Affiché : 70 px de large

```
Image format: exactly 1:1 square, 1024 x 1024 pixels. One small clay cube like a diced vegetable piece, in tomato red #D8432B, completely plain on every face, slightly rounded edges. Framing: the object alone, centred, fully visible, nothing cropped, filling about 45 % of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 22. Dé vierge (sarcelle)

Fichier : `de-sarcelle.png` · Format : **1:1 · 1024 × 1024 px** · Place dans l'image : 45 % · Affiché : 70 px de large

```
Image format: exactly 1:1 square, 1024 x 1024 pixels. One small clay cube like a diced vegetable piece, in teal #2B8C83, completely plain on every face, slightly rounded edges. Framing: the object alone, centred, fully visible, nothing cropped, filling about 45 % of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 23. Dé vierge (moutarde)

Fichier : `de-moutarde.png` · Format : **1:1 · 1024 × 1024 px** · Place dans l'image : 45 % · Affiché : 70 px de large

```
Image format: exactly 1:1 square, 1024 x 1024 pixels. One small clay cube like a diced vegetable piece, in mustard yellow #E0A21B, completely plain on every face, slightly rounded edges. Framing: the object alone, centred, fully visible, nothing cropped, filling about 45 % of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 24. La balance de cuisine

Fichier : `balance.png` · Format : **1:1 · 1024 × 1024 px** · Place dans l'image : 75 % · Affiché : 240 px de large

```
Image format: exactly 1:1 square, 1024 x 1024 pixels. A kitchen scale with a flat steel plate on top and a blank cream #F6EFE2 display with nothing shown on it, body in teal #2B8C83. Framing: the object alone, centred, fully visible, nothing cropped, filling about 75 % of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 25. La carotte entière

Fichier : `carotte.png` · Format : **3:2 · 1536 × 1024 px** · Place dans l'image : 75 % de la largeur · Affiché : 200 px de large

```
Image format: exactly 3:2 landscape, 1536 x 1024 pixels. One whole carrot lying flat horizontally, bright orange with a green leafy top. Framing: the object alone, centred, fully visible, nothing cropped, filling about 75 % de la largeur of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

---

## Température · le feu sous la poêle

### 26. Le feu éteint

Fichier : `feu-eteint.png` · Format : **1:1 · 1024 × 1024 px** · Place dans l'image : 75 % · Affiché : 230 px de large

```
Image format: exactly 1:1 square, 1024 x 1024 pixels. A round gas burner with a black cast iron grate, switched off, no flame. Framing: the object alone, centred, fully visible, nothing cropped, filling about 75 % of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 27. Le feu doux

Fichier : `feu-doux.png` · Format : **1:1 · 1024 × 1024 px** · Place dans l'image : 75 % · Affiché : 230 px de large

```
Image format: exactly 1:1 square, 1024 x 1024 pixels. The same round gas burner with a black cast iron grate, with a small gentle ring of blue flames. Framing: the object alone, centred, fully visible, nothing cropped, filling about 75 % of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 28. Le feu vif

Fichier : `feu-vif.png` · Format : **1:1 · 1024 × 1024 px** · Place dans l'image : 75 % · Affiché : 230 px de large

```
Image format: exactly 1:1 square, 1024 x 1024 pixels. The same round gas burner with a black cast iron grate, with big roaring orange and yellow flames. Framing: the object alone, centred, fully visible, nothing cropped, filling about 75 % of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 29. Le bouton de gazinière

Fichier : `bouton.png` · Format : **1:1 · 1024 × 1024 px** · Place dans l'image : 45 % · Affiché : 90 px de large

```
Image format: exactly 1:1 square, 1024 x 1024 pixels. One round stove knob in dark ink #2A2A2E seen from the front, with a small white pointer line pointing straight up. Framing: the object alone, centred, fully visible, nothing cropped, filling about 45 % of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 30. La poêle vide

Fichier : `poele.png` · Format : **3:2 · 1536 × 1024 px** · Place dans l'image : 85 % de la largeur · Affiché : 300 px de large

```
Image format: exactly 3:2 landscape, 1536 x 1024 pixels. An empty frying pan with a dark ink #2A2A2E non-stick inside and a warm light wood #D9A66B handle pointing right. Framing: the object alone, centred, fully visible, nothing cropped, filling about 85 % de la largeur of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 31. La poêle, steak parfait

Fichier : `poele-steak.png` · Format : **3:2 · 1536 × 1024 px** · Place dans l'image : 85 % de la largeur · Affiché : 300 px de large

```
Image format: exactly 3:2 landscape, 1536 x 1024 pixels. The same frying pan, handle pointing right, containing a perfectly seared golden-brown steak. Framing: the object alone, centred, fully visible, nothing cropped, filling about 85 % de la largeur of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 32. La poêle, plat brûlé

Fichier : `poele-brule.png` · Format : **3:2 · 1536 × 1024 px** · Place dans l'image : 85 % de la largeur · Affiché : 300 px de large

```
Image format: exactly 3:2 landscape, 1536 x 1024 pixels. The same frying pan, handle pointing right, containing a completely burnt black piece of food with small grey clay smoke puffs above it. Framing: the object alone, centred, fully visible, nothing cropped, filling about 85 % de la largeur of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

---

## Fenêtre de contexte · le plan de travail qui déborde

### 33. La poubelle

Fichier : `poubelle.png` · Format : **2:3 · 1024 × 1536 px** · Place dans l'image : 75 % de la hauteur · Affiché : 220 px de haut

```
Image format: exactly 2:3 portrait, 1024 x 1536 pixels. A brushed steel #C9CDD1 kitchen pedal bin with its lid wide open. Framing: the object alone, centred, fully visible, nothing cropped, filling about 75 % de la hauteur of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 34. La tomate

Fichier : `tomate.png` · Format : **1:1 · 1024 × 1024 px** · Place dans l'image : 60 % · Affiché : 110 px de large

```
Image format: exactly 1:1 square, 1024 x 1024 pixels. One ripe round tomato in tomato red #D8432B with a small green stem. Framing: the object alone, centred, fully visible, nothing cropped, filling about 60 % of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 35. L’oignon

Fichier : `oignon.png` · Format : **1:1 · 1024 × 1024 px** · Place dans l'image : 60 % · Affiché : 110 px de large

```
Image format: exactly 1:1 square, 1024 x 1024 pixels. One golden-brown onion with dry papery skin. Framing: the object alone, centred, fully visible, nothing cropped, filling about 60 % of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 36. Le citron

Fichier : `citron.png` · Format : **1:1 · 1024 × 1024 px** · Place dans l'image : 60 % · Affiché : 110 px de large

```
Image format: exactly 1:1 square, 1024 x 1024 pixels. One bright lemon in mustard yellow #E0A21B. Framing: the object alone, centred, fully visible, nothing cropped, filling about 60 % of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 37. Le fromage

Fichier : `fromage.png` · Format : **1:1 · 1024 × 1024 px** · Place dans l'image : 60 % · Affiché : 110 px de large

```
Image format: exactly 1:1 square, 1024 x 1024 pixels. One wedge of yellow cheese with round holes. Framing: the object alone, centred, fully visible, nothing cropped, filling about 60 % of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 38. Les œufs

Fichier : `oeufs.png` · Format : **1:1 · 1024 × 1024 px** · Place dans l'image : 60 % · Affiché : 110 px de large

```
Image format: exactly 1:1 square, 1024 x 1024 pixels. Two brown eggs side by side. Framing: the object alone, centred, fully visible, nothing cropped, filling about 60 % of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 39. Le beurre

Fichier : `beurre.png` · Format : **1:1 · 1024 × 1024 px** · Place dans l'image : 60 % · Affiché : 110 px de large

```
Image format: exactly 1:1 square, 1024 x 1024 pixels. One block of pale yellow butter on a small cream #F6EFE2 dish. Framing: the object alone, centred, fully visible, nothing cropped, filling about 60 % of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

---

## Hallucination · sous la cloche

### 40. La cloche fermée

Fichier : `cloche-fermee.png` · Format : **1:1 · 1024 × 1024 px** · Place dans l'image : 75 % · Affiché : 260 px de large

```
Image format: exactly 1:1 square, 1024 x 1024 pixels. A closed shiny steel serving cloche on a round white plate. Framing: the object alone, centred, fully visible, nothing cropped, filling about 75 % of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 41. La cloche ouverte, plat inventé

Fichier : `cloche-ouverte.png` · Format : **1:1 · 1024 × 1024 px** · Place dans l'image : 85 % · Affiché : 300 px de large

```
Image format: exactly 1:1 square, 1024 x 1024 pixels. The same shiny steel cloche lifted and tilted to the side, revealing a strange, clearly invented dish on the round white plate: a wobbly purple and green jelly with a fish tail sticking out of it. Framing: the object alone, centred, fully visible, nothing cropped, filling about 85 % of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

---

## Fine-tuning · le chef part en stage

### 42. Le gros livre de pâtisserie

Fichier : `livre.png` · Format : **1:1 · 1024 × 1024 px** · Place dans l'image : 70 % · Affiché : 200 px de large

```
Image format: exactly 1:1 square, 1024 x 1024 pixels. A big thick closed cookbook with a tomato red #D8432B cover and cream #F6EFE2 page edges, lying flat. Framing: the object alone, centred, fully visible, nothing cropped, filling about 70 % of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 43. Le gâteau de retour de stage

Fichier : `gateau.png` · Format : **1:1 · 1024 × 1024 px** · Place dans l'image : 70 % · Affiché : 200 px de large

```
Image format: exactly 1:1 square, 1024 x 1024 pixels. A small round layered cake on a cream plate, decorated with cream swirls and three red berries on top. Framing: the object alone, centred, fully visible, nothing cropped, filling about 70 % of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 44. Chef · il étudie

Fichier : `chef-etudie.png` · Format : **2:3 · 1024 × 1536 px** · Place dans l'image : 88 % de la hauteur · Affiché : 370 px de haut

```
Image format: exactly 2:3 portrait, 1024 x 1536 pixels. The head chef: a taller clay chef, round face with a big dark #2A2A2E moustache, tall cream #F6EFE2 toque, cream #F6EFE2 double-breasted jacket, tomato red #D8432B neckerchief, black trousers and shoes, rounded hands, simple black dot eyes. Exactly the same character in every image. Pose: sitting on a small wooden stool, reading a big thick book open on his knees, reading glasses on the tip of his nose. Facial expression: very focused, eyebrows drawn together, lips pressed, eyes on the page. Framing: full body, head to feet fully visible, centred horizontally, the character's total height (including the hat) is exactly 88 % of the image height, the soles of the feet 6 % above the bottom edge, so that every pose of the series has the same size and the same ground line. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 45. Chef · de retour de stage

Fichier : `chef-diplome.png` · Format : **2:3 · 1024 × 1536 px** · Place dans l'image : 88 % de la hauteur · Affiché : 370 px de haut

```
Image format: exactly 2:3 portrait, 1024 x 1536 pixels. The head chef: a taller clay chef, round face with a big dark #2A2A2E moustache, tall cream #F6EFE2 toque, cream #F6EFE2 double-breasted jacket, tomato red #D8432B neckerchief, black trousers and shoes, rounded hands, simple black dot eyes. Exactly the same character in every image. Pose: standing proud with a big mustard yellow #E0A21B rosette medal pinned on his jacket, holding a small cake decorated with cream swirls. Facial expression: chin up, proud satisfied smile, eyes half closed with pride. Framing: full body, head to feet fully visible, centred horizontally, the character's total height (including the hat) is exactly 88 % of the image height, the soles of the feet 6 % above the bottom edge, so that every pose of the series has the same size and the same ground line. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

---

## Appel d’outil · le chef demande, le commis va chercher

### 46. La porte de chambre froide

Fichier : `chambre-froide.png` · Format : **2:3 · 1024 × 1536 px** · Place dans l'image : 85 % de la hauteur · Affiché : 520 px de haut

```
Image format: exactly 2:3 portrait, 1024 x 1536 pixels. A heavy brushed steel #C9CDD1 walk-in cold room door with a big lever handle, closed, seen from the front, standing upright. Framing: the object alone, centred, fully visible, nothing cropped, filling about 85 % de la hauteur of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 47. Le téléphone mural

Fichier : `telephone.png` · Format : **2:3 · 1024 × 1536 px** · Place dans l'image : 60 % de la hauteur · Affiché : 220 px de haut

```
Image format: exactly 2:3 portrait, 1024 x 1536 pixels. A vintage cream #F6EFE2 wall telephone with its handset hanging on the side and a curly cord, seen from the front. Framing: the object alone, centred, fully visible, nothing cropped, filling about 60 % de la hauteur of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 48. Le carnet de bons

Fichier : `carnet.png` · Format : **1:1 · 1024 × 1024 px** · Place dans l'image : 60 % · Affiché : 150 px de large

```
Image format: exactly 1:1 square, 1024 x 1024 pixels. A small spiral order pad with blank cream #F6EFE2 pages and a pencil lying on it. Framing: the object alone, centred, fully visible, nothing cropped, filling about 60 % of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 49. Chef · il appelle une commande

Fichier : `chef-appelle.png` · Format : **2:3 · 1024 × 1536 px** · Place dans l'image : 88 % de la hauteur · Affiché : 370 px de haut

```
Image format: exactly 2:3 portrait, 1024 x 1536 pixels. The head chef: a taller clay chef, round face with a big dark #2A2A2E moustache, tall cream #F6EFE2 toque, cream #F6EFE2 double-breasted jacket, tomato red #D8432B neckerchief, black trousers and shoes, rounded hands, simple black dot eyes. Exactly the same character in every image. Pose: one hand cupped next to his mouth calling out to someone off to the side, the other hand pointing in that direction. Facial expression: mouth wide open calling, eyebrows raised, energetic and commanding. Framing: full body, head to feet fully visible, centred horizontally, the character's total height (including the hat) is exactly 88 % of the image height, the soles of the feet 6 % above the bottom edge, so that every pose of the series has the same size and the same ground line. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 50. Commis · il court chercher

Fichier : `commis-court.png` · Format : **2:3 · 1024 × 1536 px** · Place dans l'image : 88 % de la hauteur · Affiché : 330 px de haut

```
Image format: exactly 2:3 portrait, 1024 x 1536 pixels. The kitchen helper (commis): a small young cook made of clay, round friendly face with rosy cheeks, short dark #2A2A2E hair under a small cream #F6EFE2 paper cook cap, cream #F6EFE2 cook jacket, teal #2B8C83 apron, black trousers and shoes, rounded hands, simple black dot eyes. Exactly the same character in every image. Pose: running fast to the side, one foot in the air, carrying a brushed steel rectangular kitchen container in both hands. Facial expression: determined, eyebrows slightly drawn, small confident smile, eyes looking ahead. Framing: full body, head to feet fully visible, centred horizontally, the character's total height (including the hat) is exactly 88 % of the image height, the soles of the feet 6 % above the bottom edge, so that every pose of the series has the same size and the same ground line. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 51. Commis · il téléphone

Fichier : `commis-telephone.png` · Format : **2:3 · 1024 × 1536 px** · Place dans l'image : 88 % de la hauteur · Affiché : 330 px de haut

```
Image format: exactly 2:3 portrait, 1024 x 1536 pixels. The kitchen helper (commis): a small young cook made of clay, round friendly face with rosy cheeks, short dark #2A2A2E hair under a small cream #F6EFE2 paper cook cap, cream #F6EFE2 cook jacket, teal #2B8C83 apron, black trousers and shoes, rounded hands, simple black dot eyes. Exactly the same character in every image. Pose: holding a vintage cream telephone handset with a curly cord to his ear, the other hand writing on a small order pad. Facial expression: attentive, eyes looking up to the side while listening, mouth slightly open. Framing: full body, head to feet fully visible, centred horizontally, the character's total height (including the hat) is exactly 88 % of the image height, the soles of the feet 6 % above the bottom edge, so that every pose of the series has the same size and the same ground line. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 52. Commis · il écoute le chef

Fichier : `commis-ecoute.png` · Format : **2:3 · 1024 × 1536 px** · Place dans l'image : 88 % de la hauteur · Affiché : 330 px de haut

```
Image format: exactly 2:3 portrait, 1024 x 1536 pixels. The kitchen helper (commis): a small young cook made of clay, round friendly face with rosy cheeks, short dark #2A2A2E hair under a small cream #F6EFE2 paper cook cap, cream #F6EFE2 cook jacket, teal #2B8C83 apron, black trousers and shoes, rounded hands, simple black dot eyes. Exactly the same character in every image. Pose: standing straight, hands behind his back, head slightly tilted up as if listening to someone taller. Facial expression: nodding with a small attentive smile, eyebrows slightly raised. Framing: full body, head to feet fully visible, centred horizontally, the character's total height (including the hat) is exactly 88 % of the image height, the soles of the feet 6 % above the bottom edge, so that every pose of the series has the same size and the same ground line. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

---

## MCP · les bacs gastronormes

### 53. Bac GN 1/1 (entier)

Fichier : `gn-1-1.png` · Format : **3:2 · 1536 × 1024 px** · Place dans l'image : 85 % de la largeur · Affiché : 300 px de large

```
Image format: exactly 3:2 landscape, 1536 x 1024 pixels. One full-size rectangular brushed steel #C9CDD1 professional kitchen container (gastronorm pan) with a flat folded rim, seen from slightly above, proportions 53 x 32.5 cm, filled with fresh green herbs. Framing: the object alone, centred, fully visible, nothing cropped, filling about 85 % de la largeur of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 54. Bac GN 1/2 (demi)

Fichier : `gn-1-2.png` · Format : **1:1 · 1024 × 1024 px** · Place dans l'image : 70 % de la largeur · Affiché : 180 px de large

```
Image format: exactly 1:1 square, 1024 x 1024 pixels. One half-size brushed steel #C9CDD1 professional kitchen container (gastronorm pan) with a flat folded rim, seen from slightly above, almost square, proportions 32.5 x 26.5 cm, filled with tomato red #D8432B sauce. Framing: the object alone, centred, fully visible, nothing cropped, filling about 70 % de la largeur of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 55. Bac GN 1/3 (tiers)

Fichier : `gn-1-3.png` · Format : **3:2 · 1536 × 1024 px** · Place dans l'image : 65 % de la largeur · Affiché : 180 px de large

```
Image format: exactly 3:2 landscape, 1536 x 1024 pixels. One third-size brushed steel #C9CDD1 professional kitchen container (gastronorm pan) with a flat folded rim, seen from slightly above, long and narrow, proportions 32.5 x 17.6 cm, filled with mustard yellow #E0A21B corn. Framing: the object alone, centred, fully visible, nothing cropped, filling about 65 % de la largeur of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 56. Bac GN 1/6 (sixième)

Fichier : `gn-1-6.png` · Format : **1:1 · 1024 × 1024 px** · Place dans l'image : 55 % de la largeur · Affiché : 100 px de large

```
Image format: exactly 1:1 square, 1024 x 1024 pixels. One small sixth-size brushed steel #C9CDD1 professional kitchen container (gastronorm pan) with a flat folded rim, seen from slightly above, almost square, proportions 17.6 x 16.2 cm, filled with cream #F6EFE2 rice. Framing: the object alone, centred, fully visible, nothing cropped, filling about 55 % de la largeur of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 57. La saladette réfrigérée

Fichier : `saladette.png` · Format : **3:2 · 1536 × 1024 px** · Place dans l'image : 90 % de la largeur · Affiché : 330 px de large

```
Image format: exactly 3:2 landscape, 1536 x 1024 pixels. A refrigerated brushed steel #C9CDD1 prep counter with a row of empty rectangular openings on top, exactly the shape the steel kitchen containers fit into. Framing: the object alone, centred, fully visible, nothing cropped, filling about 90 % de la largeur of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 58. Le four mixte

Fichier : `four.png` · Format : **1:1 · 1024 × 1024 px** · Place dans l'image : 80 % · Affiché : 300 px de large

```
Image format: exactly 1:1 square, 1024 x 1024 pixels. A brushed steel #C9CDD1 professional combi oven, door closed, with a dark glass window and one round dark ink #2A2A2E knob. Framing: the object alone, centred, fully visible, nothing cropped, filling about 80 % of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 59. Le bain-marie

Fichier : `bain-marie.png` · Format : **3:2 · 1536 × 1024 px** · Place dans l'image : 90 % de la largeur · Affiché : 330 px de large

```
Image format: exactly 3:2 landscape, 1536 x 1024 pixels. A brushed steel #C9CDD1 bain-marie with two empty rectangular openings on top, a little steam rising. Framing: the object alone, centred, fully visible, nothing cropped, filling about 90 % de la largeur of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 60. Les boîtes bricolées

Fichier : `boites-bricolees.png` · Format : **3:2 · 1536 × 1024 px** · Place dans l'image : 85 % de la largeur · Affiché : 300 px de large

```
Image format: exactly 3:2 landscape, 1536 x 1024 pixels. A messy group of three mismatched home-made containers that obviously do not fit together: a round tomato red #D8432B plastic box, a crooked teal #2B8C83 tupperware whose lid does not close, a tiny mustard #E0A21B jar with a string around it. Framing: the object alone, centred, fully visible, nothing cropped, filling about 85 % de la largeur of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 61. Commis · il porte un bac

Fichier : `commis-porte-bac.png` · Format : **2:3 · 1024 × 1536 px** · Place dans l'image : 88 % de la hauteur · Affiché : 330 px de haut

```
Image format: exactly 2:3 portrait, 1024 x 1536 pixels. The kitchen helper (commis): a small young cook made of clay, round friendly face with rosy cheeks, short dark #2A2A2E hair under a small cream #F6EFE2 paper cook cap, cream #F6EFE2 cook jacket, teal #2B8C83 apron, black trousers and shoes, rounded hands, simple black dot eyes. Exactly the same character in every image. Pose: walking calmly, holding a full-size brushed steel rectangular kitchen container flat in front of him with both hands. Facial expression: careful and calm, eyes on the container, small smile. Framing: full body, head to feet fully visible, centred horizontally, the character's total height (including the hat) is exactly 88 % of the image height, the soles of the feet 6 % above the bottom edge, so that every pose of the series has the same size and the same ground line. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

---

## Agent · le chef en plein coup de feu

### 62. Le minuteur

Fichier : `minuteur.png` · Format : **1:1 · 1024 × 1024 px** · Place dans l'image : 55 % · Affiché : 110 px de large

```
Image format: exactly 1:1 square, 1024 x 1024 pixels. A round kitchen timer shaped like a tomato #D8432B with a small green stem on top. Framing: the object alone, centred, fully visible, nothing cropped, filling about 55 % of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 63. La sonnette de service

Fichier : `sonnette.png` · Format : **1:1 · 1024 × 1024 px** · Place dans l'image : 50 % · Affiché : 110 px de large

```
Image format: exactly 1:1 square, 1024 x 1024 pixels. A small chrome service bell of the kind you tap on a counter. Framing: the object alone, centred, fully visible, nothing cropped, filling about 50 % of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 64. La salière

Fichier : `saliere.png` · Format : **1:1 · 1024 × 1024 px** · Place dans l'image : 50 % · Affiché : 90 px de large

```
Image format: exactly 1:1 square, 1024 x 1024 pixels. A small cream #F6EFE2 ceramic salt shaker with holes on top. Framing: the object alone, centred, fully visible, nothing cropped, filling about 50 % of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 65. Chef · il goûte et grimace

Fichier : `chef-goute.png` · Format : **2:3 · 1024 × 1536 px** · Place dans l'image : 88 % de la hauteur · Affiché : 370 px de haut

```
Image format: exactly 2:3 portrait, 1024 x 1536 pixels. The head chef: a taller clay chef, round face with a big dark #2A2A2E moustache, tall cream #F6EFE2 toque, cream #F6EFE2 double-breasted jacket, tomato red #D8432B neckerchief, black trousers and shoes, rounded hands, simple black dot eyes. Exactly the same character in every image. Pose: holding a small tasting spoon at his lips, the other hand on his hip. Facial expression: one eye closed, nose wrinkled, mouth twisted to the side, clearly thinking it needs something more. Framing: full body, head to feet fully visible, centred horizontally, the character's total height (including the hat) is exactly 88 % of the image height, the soles of the feet 6 % above the bottom edge, so that every pose of the series has the same size and the same ground line. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 66. Chef · il rectifie

Fichier : `chef-sale.png` · Format : **2:3 · 1024 × 1536 px** · Place dans l'image : 88 % de la hauteur · Affiché : 370 px de haut

```
Image format: exactly 2:3 portrait, 1024 x 1536 pixels. The head chef: a taller clay chef, round face with a big dark #2A2A2E moustache, tall cream #F6EFE2 toque, cream #F6EFE2 double-breasted jacket, tomato red #D8432B neckerchief, black trousers and shoes, rounded hands, simple black dot eyes. Exactly the same character in every image. Pose: sprinkling a pinch of salt from high up with his fingers, the other hand holding a small salt shaker. Facial expression: focused, tongue slightly out at the corner of the mouth, eyes on his fingers. Framing: full body, head to feet fully visible, centred horizontally, the character's total height (including the hat) is exactly 88 % of the image height, the soles of the feet 6 % above the bottom edge, so that every pose of the series has the same size and the same ground line. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 67. Chef · content

Fichier : `chef-content.png` · Format : **2:3 · 1024 × 1536 px** · Place dans l'image : 88 % de la hauteur · Affiché : 370 px de haut

```
Image format: exactly 2:3 portrait, 1024 x 1536 pixels. The head chef: a taller clay chef, round face with a big dark #2A2A2E moustache, tall cream #F6EFE2 toque, cream #F6EFE2 double-breasted jacket, tomato red #D8432B neckerchief, black trousers and shoes, rounded hands, simple black dot eyes. Exactly the same character in every image. Pose: standing, one thumb up, the other hand on his belly. Facial expression: big happy smile with eyes closed, cheeks raised, proud. Framing: full body, head to feet fully visible, centred horizontally, the character's total height (including the hat) is exactly 88 % of the image height, the soles of the feet 6 % above the bottom edge, so that every pose of the series has the same size and the same ground line. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 68. Chef · débordé

Fichier : `chef-panique.png` · Format : **2:3 · 1024 × 1536 px** · Place dans l'image : 88 % de la hauteur · Affiché : 370 px de haut

```
Image format: exactly 2:3 portrait, 1024 x 1536 pixels. The head chef: a taller clay chef, round face with a big dark #2A2A2E moustache, tall cream #F6EFE2 toque, cream #F6EFE2 double-breasted jacket, tomato red #D8432B neckerchief, black trousers and shoes, rounded hands, simple black dot eyes. Exactly the same character in every image. Pose: both arms up in panic, toque slightly crooked, small sweat drops flying around his head. Facial expression: eyes wide open, mouth open in an O, eyebrows high, total panic. Framing: full body, head to feet fully visible, centred horizontally, the character's total height (including the hat) is exactly 88 % of the image height, the soles of the feet 6 % above the bottom edge, so that every pose of the series has the same size and the same ground line. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 69. Commis · il présente l’assiette

Fichier : `commis-presente.png` · Format : **2:3 · 1024 × 1536 px** · Place dans l'image : 88 % de la hauteur · Affiché : 330 px de haut

```
Image format: exactly 2:3 portrait, 1024 x 1536 pixels. The kitchen helper (commis): a small young cook made of clay, round friendly face with rosy cheeks, short dark #2A2A2E hair under a small cream #F6EFE2 paper cook cap, cream #F6EFE2 cook jacket, teal #2B8C83 apron, black trousers and shoes, rounded hands, simple black dot eyes. Exactly the same character in every image. Pose: holding a small white plate forward with both hands towards the viewer. Facial expression: proud big smile, eyes shining, eyebrows raised. Framing: full body, head to feet fully visible, centred horizontally, the character's total height (including the hat) is exactly 88 % of the image height, the soles of the feet 6 % above the bottom edge, so that every pose of the series has the same size and the same ground line. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 70. Commis · il coupe en dés

Fichier : `commis-coupe.png` · Format : **2:3 · 1024 × 1536 px** · Place dans l'image : 88 % de la hauteur · Affiché : 330 px de haut

```
Image format: exactly 2:3 portrait, 1024 x 1536 pixels. The kitchen helper (commis): a small young cook made of clay, round friendly face with rosy cheeks, short dark #2A2A2E hair under a small cream #F6EFE2 paper cook cap, cream #F6EFE2 cook jacket, teal #2B8C83 apron, black trousers and shoes, rounded hands, simple black dot eyes. Exactly the same character in every image. Pose: standing behind a small wooden cutting board, cutting a carrot into small cubes with a chef's knife. Facial expression: concentrated, eyes on the knife, lips pressed, eyebrows slightly drawn together. Framing: full body, head to feet fully visible, centred horizontally, the character's total height (including the hat) is exactly 88 % of the image height, the soles of the feet 6 % above the bottom edge, so that every pose of the series has the same size and the same ground line. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```
