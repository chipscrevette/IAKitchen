# Pack d'images n° 2 · La cuisine (storyboard)

**73 images, une par asset**, rangées dans l'ordre des chapitres du storyboard (`STORYBOARD.md`).

## Mode d'emploi

1. **Joins toujours en référence** le plan de travail et un objet du même type déjà réussi (pour les bocaux : `bocal.png` ; pour les poêles : `poele.png` ; pour un personnage existant : une de ses poses). Ajoute : « Keep exactly the same clay style, lighting, camera angle and character design as the reference images. »
2. **Nouveaux personnages** (serveur, patronne, critique, pâtissière, saucier) : génère d'abord UNE pose, puis joins-la en référence pour ses autres poses.
3. **Les poses ne contiennent que ce que le personnage tient en main** : jamais de planche, de table ni de nourriture devant lui (elles existent déjà dans la scène).
4. Fond transparent (ou blanc pur #FFFFFF). Génère au double si possible.
5. Dépose dans `sources/brut/` avec **exactement** le nom indiqué, puis lance `python outils/images/preparer_images.py` (détourage, mise à l'échelle, tailles.js).

| Format | Pixels | Pour quoi |
|---|---|---|
| 1:1 | 1024 × 1024 | objets compacts |
| 3:2 | 1536 × 1024 | objets longs |
| 3:1 | 1536 × 512 | objets très longs (carottes, grand tronçon) |
| 2:3 | 1024 × 1536 | tout ce qui est debout, personnages |

## Sommaire

| # | Fichier | Asset | Format | Place dans l'image | Affiché dans la scène |
|---|---|---|---|---|---|
| | **1 · Le mot suivant** | | | | |
| 1 | `sac-farine.png` | Sac de farine | 2:3 · 1024 × 1536 px | 75 % de la hauteur | 170 px de haut |
| 2 | `brique-lait.png` | Brique de lait | 2:3 · 1024 × 1536 px | 75 % de la hauteur | 150 px de haut |
| 3 | `paquet-sucre.png` | Paquet de sucre | 1:1 · 1024 × 1024 px | 65 % | 110 px de large |
| 4 | `fouet.png` | Fouet | 3:2 · 1536 × 1024 px | 80 % de la largeur | 200 px de large |
| 5 | `poele-crepe.png` | Poêle avec une crêpe | 3:2 · 1536 × 1024 px | 85 % de la largeur | 300 px de large |
| 6 | `chef-verse.png` | Chef · il verse | 2:3 · 1024 × 1536 px | 88 % de la hauteur | 370 px de haut |
| | **2 · Token** | | | | |
| 7 | `carotte-longue.png` | Carotte très longue | 3:1 · 1536 × 512 px | 92 % de la largeur | 700 px de long |
| 8 | `carotte-fine.png` | Carotte fine | 3:1 · 1536 × 512 px | 90 % de la largeur | 420 px de long |
| 9 | `troncon-court.png` | Tronçon de carotte court | 1:1 · 1024 × 1024 px | 55 % | 48 px de long |
| 10 | `troncon-moyen.png` | Tronçon de carotte moyen | 3:2 · 1536 × 1024 px | 70 % de la largeur | 90 px de long |
| 11 | `troncon-long.png` | Tronçon de carotte long | 3:1 · 1536 × 512 px | 80 % de la largeur | 170 px de long |
| 12 | `commis-coupe.png` | Commis · il coupe | 2:3 · 1024 × 1536 px | 88 % de la hauteur | 330 px de haut |
| 13 | `serveur-ticket.png` | Serveur · il apporte un ticket | 2:3 · 1024 × 1536 px | 88 % de la hauteur | 380 px de haut |
| | **3 · Température** | | | | |
| 14 | `epice-sel.png` | Pot à épices · sel | 1:1 · 1024 × 1024 px | 60 % de la hauteur | 90 px de haut |
| 15 | `epice-poivre.png` | Pot à épices · poivre | 1:1 · 1024 × 1024 px | 60 % de la hauteur | 90 px de haut |
| 16 | `epice-sucre.png` | Pot à épices · sucre | 1:1 · 1024 × 1024 px | 60 % de la hauteur | 90 px de haut |
| 17 | `epice-paprika.png` | Pot à épices · paprika | 1:1 · 1024 × 1024 px | 60 % de la hauteur | 90 px de haut |
| 18 | `epice-thym.png` | Pot à épices · thym | 1:1 · 1024 × 1024 px | 60 % de la hauteur | 90 px de haut |
| 19 | `epice-piment.png` | Pot à épices · piment | 1:1 · 1024 × 1024 px | 60 % de la hauteur | 90 px de haut |
| 20 | `epice-cannelle.png` | Pot à épices · cannelle | 1:1 · 1024 × 1024 px | 60 % de la hauteur | 90 px de haut |
| 21 | `epice-chocolat.png` | Pot à épices · chocolat | 1:1 · 1024 × 1024 px | 60 % de la hauteur | 90 px de haut |
| 22 | `poele-sauce.png` | Poêle de sauce | 3:2 · 1536 × 1024 px | 85 % de la largeur | 300 px de large |
| 23 | `poele-sauce-brulee.png` | Poêle de sauce brûlée | 3:2 · 1536 × 1024 px | 85 % de la largeur | 300 px de large |
| | **4 · Entraînement** | | | | |
| 24 | `pile-livres.png` | Pile de livres de recettes | 2:3 · 1024 × 1536 px | 85 % de la hauteur | 420 px de haut |
| 25 | `diplome.png` | Diplôme | 3:2 · 1536 × 1024 px | 75 % de la largeur | 180 px de large |
| 26 | `commis-lit.png` | Commis · il lit | 2:3 · 1024 × 1536 px | 88 % de la hauteur | 330 px de haut |
| 27 | `critique-goute.png` | Critique · il goûte | 2:3 · 1024 × 1536 px | 88 % de la hauteur | 360 px de haut |
| 28 | `critique-note.png` | Critique · il note | 2:3 · 1024 × 1536 px | 88 % de la hauteur | 360 px de haut |
| | **6 · Fine-tuning (et tous les chapitres où la patronne apparaît)** | | | | |
| 29 | `patronne-lit.png` | Patronne · elle lit un bon | 2:3 · 1024 × 1536 px | 88 % de la hauteur | 350 px de haut |
| 30 | `patronne-signe.png` | Patronne · elle signe | 2:3 · 1024 × 1536 px | 88 % de la hauteur | 350 px de haut |
| 31 | `patronne-refuse.png` | Patronne · elle refuse | 2:3 · 1024 × 1536 px | 88 % de la hauteur | 350 px de haut |
| 32 | `patissiere-poche.png` | Pâtissière · elle garnit | 2:3 · 1024 × 1536 px | 88 % de la hauteur | 360 px de haut |
| 33 | `patissiere-attend.png` | Pâtissière · elle attend | 2:3 · 1024 × 1536 px | 88 % de la hauteur | 360 px de haut |
| | **7 · Fenêtre de contexte** | | | | |
| 34 | `seau-compost.png` | Seau à compost | 1:1 · 1024 × 1024 px | 65 % | 150 px de haut |
| 35 | `serveur-attend.png` | Serveur · il attend | 2:3 · 1024 × 1536 px | 88 % de la hauteur | 380 px de haut |
| | **8 et 11 · Lost in the middle, context engineering** | | | | |
| 36 | `ramequin-vide.png` | Ramequin · vide | 1:1 · 1024 × 1024 px | 60 % | 80 px de large |
| 37 | `ramequin-sel.png` | Ramequin · sel | 1:1 · 1024 × 1024 px | 60 % | 80 px de large |
| 38 | `ramequin-paprika.png` | Ramequin · paprika | 1:1 · 1024 × 1024 px | 60 % | 80 px de large |
| 39 | `ramequin-herbes.png` | Ramequin · herbes | 1:1 · 1024 × 1024 px | 60 % | 80 px de large |
| 40 | `ramequin-sucre.png` | Ramequin · sucre | 1:1 · 1024 × 1024 px | 60 % | 80 px de large |
| 41 | `ardoise.png` | Ardoise | 3:2 · 1536 × 1024 px | 90 % de la largeur | 420 px de large |
| | **9 et 10 · Embeddings et RAG** | | | | |
| 42 | `bocal-pate-sablee.png` | Bocal rempli · pate-sablee | 1:1 · 1024 × 1024 px | 70 % de la hauteur | 110 px de large |
| 43 | `bocal-creme-amande.png` | Bocal rempli · creme-amande | 1:1 · 1024 × 1024 px | 70 % de la hauteur | 110 px de large |
| 44 | `bocal-poires-pochees.png` | Bocal rempli · poires-pochees | 1:1 · 1024 × 1024 px | 70 % de la hauteur | 110 px de large |
| 45 | `bocal-fond-brun.png` | Bocal rempli · fond-brun | 1:1 · 1024 × 1024 px | 70 % de la hauteur | 110 px de large |
| 46 | `bocal-vinaigrette.png` | Bocal rempli · vinaigrette | 1:1 · 1024 × 1024 px | 70 % de la hauteur | 110 px de large |
| 47 | `bocal-veloute-potiron.png` | Bocal rempli · veloute-potiron | 1:1 · 1024 × 1024 px | 70 % de la hauteur | 110 px de large |
| 48 | `bocal-beurre-blanc.png` | Bocal rempli · beurre-blanc | 1:1 · 1024 × 1024 px | 70 % de la hauteur | 110 px de large |
| 49 | `bocal-coulis-framboise.png` | Bocal rempli · coulis-framboise | 1:1 · 1024 × 1024 px | 70 % de la hauteur | 110 px de large |
| 50 | `louche.png` | Louche | 3:2 · 1536 × 1024 px | 80 % de la largeur | 200 px de large |
| 51 | `commis-remplit.png` | Commis · il remplit un bocal | 2:3 · 1024 × 1536 px | 88 % de la hauteur | 330 px de haut |
| | **12 · Appel d’outil** | | | | |
| 52 | `boite-oeufs.png` | Boîte d’œufs | 3:2 · 1536 × 1024 px | 75 % de la largeur | 180 px de large |
| 53 | `commis-presente.png` | Commis · il présente | 2:3 · 1024 × 1536 px | 88 % de la hauteur | 330 px de haut |
| | **14 · MCP** | | | | |
| 54 | `saladette-pleine.png` | Saladette pleine | 3:2 · 1536 × 1024 px | 90 % de la largeur | 360 px de large |
| 55 | `bain-marie-plein.png` | Bain-marie plein | 3:2 · 1536 × 1024 px | 90 % de la largeur | 320 px de large |
| | **15 · Trop d’outils** | | | | |
| 56 | `tiroir-bazar.png` | Tiroir en vrac | 3:2 · 1536 × 1024 px | 90 % de la largeur | 420 px de large |
| 57 | `ecumoire.png` | Ecumoire | 3:2 · 1536 × 1024 px | 80 % de la largeur | 170 px de large |
| 58 | `passoire.png` | Passoire | 3:2 · 1536 × 1024 px | 80 % de la largeur | 170 px de large |
| 59 | `spatule.png` | Spatule | 3:2 · 1536 × 1024 px | 80 % de la largeur | 170 px de large |
| 60 | `pince.png` | Pince | 3:2 · 1536 × 1024 px | 80 % de la largeur | 170 px de large |
| 61 | `rape.png` | Rape | 3:2 · 1536 × 1024 px | 80 % de la largeur | 170 px de large |
| 62 | `econome.png` | Econome | 3:2 · 1536 × 1024 px | 80 % de la largeur | 170 px de large |
| 63 | `cuillere-bois.png` | Cuillere bois | 3:2 · 1536 × 1024 px | 80 % de la largeur | 170 px de large |
| 64 | `ciseaux.png` | Ciseaux | 3:2 · 1536 × 1024 px | 80 % de la largeur | 170 px de large |
| | **19 · Multi-agents** | | | | |
| 65 | `saucier-fouette.png` | Saucier · il fouette | 2:3 · 1024 × 1536 px | 88 % de la hauteur | 360 px de haut |
| 66 | `saucier-attend.png` | Saucier · il attend | 2:3 · 1024 × 1536 px | 88 % de la hauteur | 360 px de haut |
| | **Toujours manquants depuis le pack n° 1** | | | | |
| 67 | `chef-content.png` | Chef · content | 2:3 · 1024 × 1536 px | 88 % de la hauteur | 370 px de haut |
| 68 | `chef-panique.png` | Chef · débordé | 2:3 · 1024 × 1536 px | 88 % de la hauteur | 370 px de haut |
| | **23 · Coût et délai** | | | | |
| 69 | `addition.png` | Addition | 2:3 · 1024 × 1536 px | 80 % de la hauteur | 260 px de haut |
| 70 | `pieces.png` | Pièces | 1:1 · 1024 × 1024 px | 55 % | 90 px de large |
| 71 | `sablier.png` | Sablier | 2:3 · 1024 × 1536 px | 70 % de la hauteur | 160 px de haut |
| | **24 et 25 · Injection, données confidentielles** | | | | |
| 72 | `carnet-secret.png` | Carnet secret | 1:1 · 1024 × 1024 px | 65 % | 150 px de large |
| 73 | `coffre.png` | Coffre | 1:1 · 1024 × 1024 px | 65 % | 160 px de large |

---

## 1 · Le mot suivant

### 1. Sac de farine

Fichier : `sac-farine.png` · Format : **2:3 · 1024 × 1536 px** · Place dans l'image : 75 % de la hauteur · Affiché : 170 px de haut

```
Image format: exactly 2:3 portrait, 1024 x 1536 pixels. A paper flour bag in cream #F6EFE2, the top rolled down and open, a little white flour visible inside, a small dusting of flour at its base. Framing: the object alone, centred, fully visible, nothing cropped, filling about 75 % de la hauteur of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 2. Brique de lait

Fichier : `brique-lait.png` · Format : **2:3 · 1024 × 1536 px** · Place dans l'image : 75 % de la hauteur · Affiché : 150 px de haut

```
Image format: exactly 2:3 portrait, 1024 x 1536 pixels. A milk carton with a gable top, white with a teal #2B8C83 band, closed, standing upright. Framing: the object alone, centred, fully visible, nothing cropped, filling about 75 % de la hauteur of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 3. Paquet de sucre

Fichier : `paquet-sucre.png` · Format : **1:1 · 1024 × 1024 px** · Place dans l'image : 65 % · Affiché : 110 px de large

```
Image format: exactly 1:1 square, 1024 x 1024 pixels. A small white box of sugar with a mustard yellow #E0A21B band, standing upright, a few sugar cubes in front of it. Framing: the object alone, centred, fully visible, nothing cropped, filling about 65 % of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 4. Fouet

Fichier : `fouet.png` · Format : **3:2 · 1536 × 1024 px** · Place dans l'image : 80 % de la largeur · Affiché : 200 px de large

```
Image format: exactly 3:2 landscape, 1536 x 1024 pixels. A steel balloon whisk with a dark ink #2A2A2E handle. Lying flat on its side, horizontal, seen from the same slightly high angle. Framing: the object alone, centred, fully visible, nothing cropped, filling about 80 % de la largeur of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 5. Poêle avec une crêpe

Fichier : `poele-crepe.png` · Format : **3:2 · 1536 × 1024 px** · Place dans l'image : 85 % de la largeur · Affiché : 300 px de large

```
Image format: exactly 3:2 landscape, 1536 x 1024 pixels. The same frying pan as in the reference (dark ink #2A2A2E inside, light wood #D9A66B handle pointing right) containing one thin golden crêpe with light brown spots. Framing: the object alone, centred, fully visible, nothing cropped, filling about 85 % de la largeur of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 6. Chef · il verse

Fichier : `chef-verse.png` · Format : **2:3 · 1024 × 1536 px** · Place dans l'image : 88 % de la hauteur · Affiché : 370 px de haut

```
Image format: exactly 2:3 portrait, 1024 x 1536 pixels. The head chef, exactly the same character as in the reference images: a taller clay chef, round face with a big dark #2A2A2E moustache, tall cream #F6EFE2 toque, cream double-breasted jacket, tomato red #D8432B neckerchief, black trousers and shoes, rounded hands, simple black dot eyes. Pose: holding a milk carton in the right hand, tilted forward and down as if pouring into something in front of him, the left hand on his hip. Facial expression: focused and confident, eyes looking down at where he pours, small smile under the moustache. Framing: full body, head to feet fully visible, centred horizontally, the character's total height (including any hat) is exactly 88 % of the image height, the soles of the feet 6 % above the bottom edge, so that every pose of the series has the same size and the same ground line. The character holds ONLY the objects named below: there is no table, no cutting board, no counter and no food in front of them. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

---

## 2 · Token

### 7. Carotte très longue

Fichier : `carotte-longue.png` · Format : **3:1 · 1536 × 512 px** · Place dans l'image : 92 % de la largeur · Affiché : 700 px de long

```
Image format: exactly 3:1 wide landscape, 1536 x 512 pixels. One very long, straight, thick carrot, about 8 times longer than it is thick, bright orange with fine rings, green leafy top at the left end. Lying flat on its side, horizontal, seen from the same slightly high angle. Framing: the object alone, centred, fully visible, nothing cropped, filling about 92 % de la largeur of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 8. Carotte fine

Fichier : `carotte-fine.png` · Format : **3:1 · 1536 × 512 px** · Place dans l'image : 90 % de la largeur · Affiché : 420 px de long

```
Image format: exactly 3:1 wide landscape, 1536 x 512 pixels. One long thin carrot, about 12 times longer than it is thick, bright orange, small green leafy top at the left end. Lying flat on its side, horizontal, seen from the same slightly high angle. Framing: the object alone, centred, fully visible, nothing cropped, filling about 90 % de la largeur of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 9. Tronçon de carotte court

Fichier : `troncon-court.png` · Format : **1:1 · 1024 × 1024 px** · Place dans l'image : 55 % · Affiché : 48 px de long

```
Image format: exactly 1:1 square, 1024 x 1024 pixels. One short piece of carrot cut with a knife at both ends, as long as it is thick, both cut faces clean and visible showing the paler orange flesh with rings. Lying flat on its side, horizontal, seen from the same slightly high angle. Framing: the object alone, centred, fully visible, nothing cropped, filling about 55 % of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 10. Tronçon de carotte moyen

Fichier : `troncon-moyen.png` · Format : **3:2 · 1536 × 1024 px** · Place dans l'image : 70 % de la largeur · Affiché : 90 px de long

```
Image format: exactly 3:2 landscape, 1536 x 1024 pixels. One piece of carrot cut with a knife at both ends, twice as long as it is thick, both cut faces clean showing the paler orange flesh with rings. Lying flat on its side, horizontal, seen from the same slightly high angle. Framing: the object alone, centred, fully visible, nothing cropped, filling about 70 % de la largeur of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 11. Tronçon de carotte long

Fichier : `troncon-long.png` · Format : **3:1 · 1536 × 512 px** · Place dans l'image : 80 % de la largeur · Affiché : 170 px de long

```
Image format: exactly 3:1 wide landscape, 1536 x 512 pixels. One piece of carrot cut with a knife at both ends, four times as long as it is thick, both cut faces clean showing the paler orange flesh with rings. Lying flat on its side, horizontal, seen from the same slightly high angle. Framing: the object alone, centred, fully visible, nothing cropped, filling about 80 % de la largeur of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 12. Commis · il coupe

Fichier : `commis-coupe.png` · Format : **2:3 · 1024 × 1536 px** · Place dans l'image : 88 % de la hauteur · Affiché : 330 px de haut

```
Image format: exactly 2:3 portrait, 1024 x 1536 pixels. The kitchen helper (commis), exactly the same character as in the reference images: a small young cook made of clay, round friendly face with rosy cheeks, short dark #2A2A2E hair under a small cream #F6EFE2 paper cook cap, cream #F6EFE2 cook jacket, teal #2B8C83 apron, black trousers and shoes, rounded hands, simple black dot eyes. Pose: standing, the chef's knife held in the right hand with the blade pointing down and forward, as if slicing something on a table just in front of him, the left hand flat and slightly forward as if holding the food in place. Facial expression: concentrated, eyes looking down at the knife, lips pressed, eyebrows slightly drawn together. Framing: full body, head to feet fully visible, centred horizontally, the character's total height (including any hat) is exactly 88 % of the image height, the soles of the feet 6 % above the bottom edge, so that every pose of the series has the same size and the same ground line. The character holds ONLY the objects named below: there is no table, no cutting board, no counter and no food in front of them. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 13. Serveur · il apporte un ticket

Fichier : `serveur-ticket.png` · Format : **2:3 · 1024 × 1536 px** · Place dans l'image : 88 % de la hauteur · Affiché : 380 px de haut

```
Image format: exactly 2:3 portrait, 1024 x 1536 pixels. The waiter, a NEW character of the same clay series: a tall slim clay waiter, neat side-parted dark #2A2A2E hair, a thin moustache, white shirt with rolled sleeves, black waistcoat, black bow tie, long white apron down to the knees, black trousers and shoes, rounded hands, simple black dot eyes. Same character in every image. Pose: holding a small white order ticket forward in the right hand at chest height, the left arm folded behind his back. Facial expression: polite professional smile, eyebrows slightly raised, eyes looking forward. Framing: full body, head to feet fully visible, centred horizontally, the character's total height (including any hat) is exactly 88 % of the image height, the soles of the feet 6 % above the bottom edge, so that every pose of the series has the same size and the same ground line. The character holds ONLY the objects named below: there is no table, no cutting board, no counter and no food in front of them. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

---

## 3 · Température

### 14. Pot à épices · sel

Fichier : `epice-sel.png` · Format : **1:1 · 1024 × 1024 px** · Place dans l'image : 60 % de la hauteur · Affiché : 90 px de haut

```
Image format: exactly 1:1 square, 1024 x 1024 pixels. One small round glass spice jar with a cork stopper, as tall as it is wide, filled with coarse white salt, a blank strip of white masking tape across the front (nothing written). Framing: the object alone, centred, fully visible, nothing cropped, filling about 60 % de la hauteur of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 15. Pot à épices · poivre

Fichier : `epice-poivre.png` · Format : **1:1 · 1024 × 1024 px** · Place dans l'image : 60 % de la hauteur · Affiché : 90 px de haut

```
Image format: exactly 1:1 square, 1024 x 1024 pixels. One small round glass spice jar with a cork stopper, as tall as it is wide, filled with black peppercorns, a blank strip of white masking tape across the front (nothing written). Framing: the object alone, centred, fully visible, nothing cropped, filling about 60 % de la hauteur of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 16. Pot à épices · sucre

Fichier : `epice-sucre.png` · Format : **1:1 · 1024 × 1024 px** · Place dans l'image : 60 % de la hauteur · Affiché : 90 px de haut

```
Image format: exactly 1:1 square, 1024 x 1024 pixels. One small round glass spice jar with a cork stopper, as tall as it is wide, filled with white sugar crystals, a blank strip of white masking tape across the front (nothing written). Framing: the object alone, centred, fully visible, nothing cropped, filling about 60 % de la hauteur of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 17. Pot à épices · paprika

Fichier : `epice-paprika.png` · Format : **1:1 · 1024 × 1024 px** · Place dans l'image : 60 % de la hauteur · Affiché : 90 px de haut

```
Image format: exactly 1:1 square, 1024 x 1024 pixels. One small round glass spice jar with a cork stopper, as tall as it is wide, filled with bright red paprika powder, a blank strip of white masking tape across the front (nothing written). Framing: the object alone, centred, fully visible, nothing cropped, filling about 60 % de la hauteur of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 18. Pot à épices · thym

Fichier : `epice-thym.png` · Format : **1:1 · 1024 × 1024 px** · Place dans l'image : 60 % de la hauteur · Affiché : 90 px de haut

```
Image format: exactly 1:1 square, 1024 x 1024 pixels. One small round glass spice jar with a cork stopper, as tall as it is wide, filled with dried green thyme, a blank strip of white masking tape across the front (nothing written). Framing: the object alone, centred, fully visible, nothing cropped, filling about 60 % de la hauteur of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 19. Pot à épices · piment

Fichier : `epice-piment.png` · Format : **1:1 · 1024 × 1024 px** · Place dans l'image : 60 % de la hauteur · Affiché : 90 px de haut

```
Image format: exactly 1:1 square, 1024 x 1024 pixels. One small round glass spice jar with a cork stopper, as tall as it is wide, filled with small dried red chillies, a blank strip of white masking tape across the front (nothing written). Framing: the object alone, centred, fully visible, nothing cropped, filling about 60 % de la hauteur of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 20. Pot à épices · cannelle

Fichier : `epice-cannelle.png` · Format : **1:1 · 1024 × 1024 px** · Place dans l'image : 60 % de la hauteur · Affiché : 90 px de haut

```
Image format: exactly 1:1 square, 1024 x 1024 pixels. One small round glass spice jar with a cork stopper, as tall as it is wide, filled with brown cinnamon sticks, a blank strip of white masking tape across the front (nothing written). Framing: the object alone, centred, fully visible, nothing cropped, filling about 60 % de la hauteur of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 21. Pot à épices · chocolat

Fichier : `epice-chocolat.png` · Format : **1:1 · 1024 × 1024 px** · Place dans l'image : 60 % de la hauteur · Affiché : 90 px de haut

```
Image format: exactly 1:1 square, 1024 x 1024 pixels. One small round glass spice jar with a cork stopper, as tall as it is wide, filled with dark chocolate chips, a blank strip of white masking tape across the front (nothing written). Framing: the object alone, centred, fully visible, nothing cropped, filling about 60 % de la hauteur of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 22. Poêle de sauce

Fichier : `poele-sauce.png` · Format : **3:2 · 1536 × 1024 px** · Place dans l'image : 85 % de la largeur · Affiché : 300 px de large

```
Image format: exactly 3:2 landscape, 1536 x 1024 pixels. The same frying pan as in the reference (dark ink inside, light wood handle pointing right) filled with a glossy tomato red #D8432B sauce. Framing: the object alone, centred, fully visible, nothing cropped, filling about 85 % de la largeur of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 23. Poêle de sauce brûlée

Fichier : `poele-sauce-brulee.png` · Format : **3:2 · 1536 × 1024 px** · Place dans l'image : 85 % de la largeur · Affiché : 300 px de large

```
Image format: exactly 3:2 landscape, 1536 x 1024 pixels. The same frying pan, handle pointing right, with the sauce burnt into a black crust and small grey clay smoke puffs rising. Framing: the object alone, centred, fully visible, nothing cropped, filling about 85 % de la largeur of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

---

## 4 · Entraînement

### 24. Pile de livres de recettes

Fichier : `pile-livres.png` · Format : **2:3 · 1024 × 1536 px** · Place dans l'image : 85 % de la hauteur · Affiché : 420 px de haut

```
Image format: exactly 2:3 portrait, 1024 x 1536 pixels. A tall slightly wobbly stack of about 15 thick cookbooks of different sizes, covers in tomato red, teal, mustard, cream and dark ink, lying flat on top of each other. Framing: the object alone, centred, fully visible, nothing cropped, filling about 85 % de la hauteur of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 25. Diplôme

Fichier : `diplome.png` · Format : **3:2 · 1536 × 1024 px** · Place dans l'image : 75 % de la largeur · Affiché : 180 px de large

```
Image format: exactly 3:2 landscape, 1536 x 1024 pixels. A rolled cream #F6EFE2 parchment diploma tied with a tomato red #D8432B ribbon and a small wax seal. Lying flat on its side, horizontal, seen from the same slightly high angle. Framing: the object alone, centred, fully visible, nothing cropped, filling about 75 % de la largeur of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 26. Commis · il lit

Fichier : `commis-lit.png` · Format : **2:3 · 1024 × 1536 px** · Place dans l'image : 88 % de la hauteur · Affiché : 330 px de haut

```
Image format: exactly 2:3 portrait, 1024 x 1536 pixels. The kitchen helper (commis), exactly the same character as in the reference images: a small young cook made of clay, round friendly face with rosy cheeks, short dark #2A2A2E hair under a small cream #F6EFE2 paper cook cap, cream #F6EFE2 cook jacket, teal #2B8C83 apron, black trousers and shoes, rounded hands, simple black dot eyes. Pose: standing, reading an open thick cookbook held in both hands in front of his chest. Facial expression: absorbed, eyes on the page, mouth slightly open, eyebrows raised with curiosity. Framing: full body, head to feet fully visible, centred horizontally, the character's total height (including any hat) is exactly 88 % of the image height, the soles of the feet 6 % above the bottom edge, so that every pose of the series has the same size and the same ground line. The character holds ONLY the objects named below: there is no table, no cutting board, no counter and no food in front of them. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 27. Critique · il goûte

Fichier : `critique-goute.png` · Format : **2:3 · 1024 × 1536 px** · Place dans l'image : 88 % de la hauteur · Affiché : 360 px de haut

```
Image format: exactly 2:3 portrait, 1024 x 1536 pixels. The food critic, a NEW character of the same clay series: a thin clay man with a small dark ink #2A2A2E beret, round glasses, a long mustard yellow #E0A21B scarf, a grey jacket, dark trousers and shoes, rounded hands, simple black dot eyes. Same character in every image. Pose: tasting from a small spoon held in the right hand, a small notebook in the left hand. Facial expression: eyes closed, one eyebrow raised, lips pursed, judging seriously. Framing: full body, head to feet fully visible, centred horizontally, the character's total height (including any hat) is exactly 88 % of the image height, the soles of the feet 6 % above the bottom edge, so that every pose of the series has the same size and the same ground line. The character holds ONLY the objects named below: there is no table, no cutting board, no counter and no food in front of them. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 28. Critique · il note

Fichier : `critique-note.png` · Format : **2:3 · 1024 × 1536 px** · Place dans l'image : 88 % de la hauteur · Affiché : 360 px de haut

```
Image format: exactly 2:3 portrait, 1024 x 1536 pixels. The food critic, a NEW character of the same clay series: a thin clay man with a small dark ink #2A2A2E beret, round glasses, a long mustard yellow #E0A21B scarf, a grey jacket, dark trousers and shoes, rounded hands, simple black dot eyes. Same character in every image. Pose: writing in his small notebook with a pencil. Facial expression: stern, one eyebrow raised, eyes on the notebook. Framing: full body, head to feet fully visible, centred horizontally, the character's total height (including any hat) is exactly 88 % of the image height, the soles of the feet 6 % above the bottom edge, so that every pose of the series has the same size and the same ground line. The character holds ONLY the objects named below: there is no table, no cutting board, no counter and no food in front of them. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

---

## 6 · Fine-tuning (et tous les chapitres où la patronne apparaît)

### 29. Patronne · elle lit un bon

Fichier : `patronne-lit.png` · Format : **2:3 · 1024 × 1536 px** · Place dans l'image : 88 % de la hauteur · Affiché : 350 px de haut

```
Image format: exactly 2:3 portrait, 1024 x 1536 pixels. The owner (la patronne), a NEW character of the same clay series: a clay woman in her sixties, grey hair in a neat bun, round glasses, a burgundy cardigan over a cream #F6EFE2 blouse, dark ink #2A2A2E skirt, black shoes, a pencil behind her ear, rounded hands, simple black dot eyes behind the glasses. Same character in every image. Pose: holding a small paper slip in both hands and reading it through her glasses. Facial expression: attentive, eyebrows raised, lips pressed. Framing: full body, head to feet fully visible, centred horizontally, the character's total height (including any hat) is exactly 88 % of the image height, the soles of the feet 6 % above the bottom edge, so that every pose of the series has the same size and the same ground line. The character holds ONLY the objects named below: there is no table, no cutting board, no counter and no food in front of them. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 30. Patronne · elle signe

Fichier : `patronne-signe.png` · Format : **2:3 · 1024 × 1536 px** · Place dans l'image : 88 % de la hauteur · Affiché : 350 px de haut

```
Image format: exactly 2:3 portrait, 1024 x 1536 pixels. The owner (la patronne), a NEW character of the same clay series: a clay woman in her sixties, grey hair in a neat bun, round glasses, a burgundy cardigan over a cream #F6EFE2 blouse, dark ink #2A2A2E skirt, black shoes, a pencil behind her ear, rounded hands, simple black dot eyes behind the glasses. Same character in every image. Pose: signing a paper slip held against her left palm with a pencil. Facial expression: satisfied small smile, eyes on the paper. Framing: full body, head to feet fully visible, centred horizontally, the character's total height (including any hat) is exactly 88 % of the image height, the soles of the feet 6 % above the bottom edge, so that every pose of the series has the same size and the same ground line. The character holds ONLY the objects named below: there is no table, no cutting board, no counter and no food in front of them. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 31. Patronne · elle refuse

Fichier : `patronne-refuse.png` · Format : **2:3 · 1024 × 1536 px** · Place dans l'image : 88 % de la hauteur · Affiché : 350 px de haut

```
Image format: exactly 2:3 portrait, 1024 x 1536 pixels. The owner (la patronne), a NEW character of the same clay series: a clay woman in her sixties, grey hair in a neat bun, round glasses, a burgundy cardigan over a cream #F6EFE2 blouse, dark ink #2A2A2E skirt, black shoes, a pencil behind her ear, rounded hands, simple black dot eyes behind the glasses. Same character in every image. Pose: right hand raised flat, palm forward, in a firm stop gesture, the left hand holding a paper slip. Facial expression: stern, eyebrows drawn together, mouth firm. Framing: full body, head to feet fully visible, centred horizontally, the character's total height (including any hat) is exactly 88 % of the image height, the soles of the feet 6 % above the bottom edge, so that every pose of the series has the same size and the same ground line. The character holds ONLY the objects named below: there is no table, no cutting board, no counter and no food in front of them. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 32. Pâtissière · elle garnit

Fichier : `patissiere-poche.png` · Format : **2:3 · 1024 × 1536 px** · Place dans l'image : 88 % de la hauteur · Affiché : 360 px de haut

```
Image format: exactly 2:3 portrait, 1024 x 1536 pixels. The pastry chef, a NEW character of the same clay series: a clay young woman with short curly dark hair under a tall cream #F6EFE2 toque, cream double-breasted jacket, mustard yellow #E0A21B neckerchief, black trousers and shoes, rounded hands, simple black dot eyes. Same character in every image. Pose: holding a piping bag in both hands, pressing it as if piping cream downwards. Facial expression: focused, tongue slightly out at the corner of the mouth. Framing: full body, head to feet fully visible, centred horizontally, the character's total height (including any hat) is exactly 88 % of the image height, the soles of the feet 6 % above the bottom edge, so that every pose of the series has the same size and the same ground line. The character holds ONLY the objects named below: there is no table, no cutting board, no counter and no food in front of them. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 33. Pâtissière · elle attend

Fichier : `patissiere-attend.png` · Format : **2:3 · 1024 × 1536 px** · Place dans l'image : 88 % de la hauteur · Affiché : 360 px de haut

```
Image format: exactly 2:3 portrait, 1024 x 1536 pixels. The pastry chef, a NEW character of the same clay series: a clay young woman with short curly dark hair under a tall cream #F6EFE2 toque, cream double-breasted jacket, mustard yellow #E0A21B neckerchief, black trousers and shoes, rounded hands, simple black dot eyes. Same character in every image. Pose: standing, arms crossed. Facial expression: confident friendly smile. Framing: full body, head to feet fully visible, centred horizontally, the character's total height (including any hat) is exactly 88 % of the image height, the soles of the feet 6 % above the bottom edge, so that every pose of the series has the same size and the same ground line. The character holds ONLY the objects named below: there is no table, no cutting board, no counter and no food in front of them. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

---

## 7 · Fenêtre de contexte

### 34. Seau à compost

Fichier : `seau-compost.png` · Format : **1:1 · 1024 × 1024 px** · Place dans l'image : 65 % · Affiché : 150 px de haut

```
Image format: exactly 1:1 square, 1024 x 1024 pixels. A small countertop compost bin in cream #F6EFE2 enamel with a teal #2B8C83 lid wide open, a few vegetable peels visible inside. Framing: the object alone, centred, fully visible, nothing cropped, filling about 65 % of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 35. Serveur · il attend

Fichier : `serveur-attend.png` · Format : **2:3 · 1024 × 1536 px** · Place dans l'image : 88 % de la hauteur · Affiché : 380 px de haut

```
Image format: exactly 2:3 portrait, 1024 x 1536 pixels. The waiter, a NEW character of the same clay series: a tall slim clay waiter, neat side-parted dark #2A2A2E hair, a thin moustache, white shirt with rolled sleeves, black waistcoat, black bow tie, long white apron down to the knees, black trousers and shoes, rounded hands, simple black dot eyes. Same character in every image. Pose: standing straight, a white napkin folded over the left forearm, the right hand at his side. Facial expression: calm and polite, small smile. Framing: full body, head to feet fully visible, centred horizontally, the character's total height (including any hat) is exactly 88 % of the image height, the soles of the feet 6 % above the bottom edge, so that every pose of the series has the same size and the same ground line. The character holds ONLY the objects named below: there is no table, no cutting board, no counter and no food in front of them. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

---

## 8 et 11 · Lost in the middle, context engineering

### 36. Ramequin · vide

Fichier : `ramequin-vide.png` · Format : **1:1 · 1024 × 1024 px** · Place dans l'image : 60 % · Affiché : 80 px de large

```
Image format: exactly 1:1 square, 1024 x 1024 pixels. One small round white ceramic ramekin, empty. Framing: the object alone, centred, fully visible, nothing cropped, filling about 60 % of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 37. Ramequin · sel

Fichier : `ramequin-sel.png` · Format : **1:1 · 1024 × 1024 px** · Place dans l'image : 60 % · Affiché : 80 px de large

```
Image format: exactly 1:1 square, 1024 x 1024 pixels. One small round white ceramic ramekin, filled with coarse white salt. Framing: the object alone, centred, fully visible, nothing cropped, filling about 60 % of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 38. Ramequin · paprika

Fichier : `ramequin-paprika.png` · Format : **1:1 · 1024 × 1024 px** · Place dans l'image : 60 % · Affiché : 80 px de large

```
Image format: exactly 1:1 square, 1024 x 1024 pixels. One small round white ceramic ramekin, filled with bright red paprika powder. Framing: the object alone, centred, fully visible, nothing cropped, filling about 60 % of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 39. Ramequin · herbes

Fichier : `ramequin-herbes.png` · Format : **1:1 · 1024 × 1024 px** · Place dans l'image : 60 % · Affiché : 80 px de large

```
Image format: exactly 1:1 square, 1024 x 1024 pixels. One small round white ceramic ramekin, filled with chopped green herbs. Framing: the object alone, centred, fully visible, nothing cropped, filling about 60 % of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 40. Ramequin · sucre

Fichier : `ramequin-sucre.png` · Format : **1:1 · 1024 × 1024 px** · Place dans l'image : 60 % · Affiché : 80 px de large

```
Image format: exactly 1:1 square, 1024 x 1024 pixels. One small round white ceramic ramekin, filled with white sugar. Framing: the object alone, centred, fully visible, nothing cropped, filling about 60 % of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 41. Ardoise

Fichier : `ardoise.png` · Format : **3:2 · 1536 × 1024 px** · Place dans l'image : 90 % de la largeur · Affiché : 420 px de large

```
Image format: exactly 3:2 landscape, 1536 x 1024 pixels. A small blackboard slate with a light wood #D9A66B frame, completely blank and clean, standing slightly tilted. Framing: the object alone, centred, fully visible, nothing cropped, filling about 90 % de la largeur of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

---

## 9 et 10 · Embeddings et RAG

### 42. Bocal rempli · pate-sablee

Fichier : `bocal-pate-sablee.png` · Format : **1:1 · 1024 × 1024 px** · Place dans l'image : 70 % de la hauteur · Affiché : 110 px de large

```
Image format: exactly 1:1 square, 1024 x 1024 pixels. Exactly the same round glass jar as in the reference (tomato red #D8432B clay lid, blank strip of white masking tape across the front, nothing written), filled with crumbly golden beige shortcrust dough. Framing: the object alone, centred, fully visible, nothing cropped, filling about 70 % de la hauteur of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 43. Bocal rempli · creme-amande

Fichier : `bocal-creme-amande.png` · Format : **1:1 · 1024 × 1024 px** · Place dans l'image : 70 % de la hauteur · Affiché : 110 px de large

```
Image format: exactly 1:1 square, 1024 x 1024 pixels. Exactly the same round glass jar as in the reference (tomato red #D8432B clay lid, blank strip of white masking tape across the front, nothing written), filled with pale yellow almond cream. Framing: the object alone, centred, fully visible, nothing cropped, filling about 70 % de la hauteur of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 44. Bocal rempli · poires-pochees

Fichier : `bocal-poires-pochees.png` · Format : **1:1 · 1024 × 1024 px** · Place dans l'image : 70 % de la hauteur · Affiché : 110 px de large

```
Image format: exactly 1:1 square, 1024 x 1024 pixels. Exactly the same round glass jar as in the reference (tomato red #D8432B clay lid, blank strip of white masking tape across the front, nothing written), filled with dark red wine-poached pear halves. Framing: the object alone, centred, fully visible, nothing cropped, filling about 70 % de la hauteur of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 45. Bocal rempli · fond-brun

Fichier : `bocal-fond-brun.png` · Format : **1:1 · 1024 × 1024 px** · Place dans l'image : 70 % de la hauteur · Affiché : 110 px de large

```
Image format: exactly 1:1 square, 1024 x 1024 pixels. Exactly the same round glass jar as in the reference (tomato red #D8432B clay lid, blank strip of white masking tape across the front, nothing written), filled with a dark brown glossy stock. Framing: the object alone, centred, fully visible, nothing cropped, filling about 70 % de la hauteur of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 46. Bocal rempli · vinaigrette

Fichier : `bocal-vinaigrette.png` · Format : **1:1 · 1024 × 1024 px** · Place dans l'image : 70 % de la hauteur · Affiché : 110 px de large

```
Image format: exactly 1:1 square, 1024 x 1024 pixels. Exactly the same round glass jar as in the reference (tomato red #D8432B clay lid, blank strip of white masking tape across the front, nothing written), filled with a golden oil and mustard vinaigrette. Framing: the object alone, centred, fully visible, nothing cropped, filling about 70 % de la hauteur of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 47. Bocal rempli · veloute-potiron

Fichier : `bocal-veloute-potiron.png` · Format : **1:1 · 1024 × 1024 px** · Place dans l'image : 70 % de la hauteur · Affiché : 110 px de large

```
Image format: exactly 1:1 square, 1024 x 1024 pixels. Exactly the same round glass jar as in the reference (tomato red #D8432B clay lid, blank strip of white masking tape across the front, nothing written), filled with a smooth orange pumpkin soup. Framing: the object alone, centred, fully visible, nothing cropped, filling about 70 % de la hauteur of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 48. Bocal rempli · beurre-blanc

Fichier : `bocal-beurre-blanc.png` · Format : **1:1 · 1024 × 1024 px** · Place dans l'image : 70 % de la hauteur · Affiché : 110 px de large

```
Image format: exactly 1:1 square, 1024 x 1024 pixels. Exactly the same round glass jar as in the reference (tomato red #D8432B clay lid, blank strip of white masking tape across the front, nothing written), filled with a pale creamy butter sauce. Framing: the object alone, centred, fully visible, nothing cropped, filling about 70 % de la hauteur of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 49. Bocal rempli · coulis-framboise

Fichier : `bocal-coulis-framboise.png` · Format : **1:1 · 1024 × 1024 px** · Place dans l'image : 70 % de la hauteur · Affiché : 110 px de large

```
Image format: exactly 1:1 square, 1024 x 1024 pixels. Exactly the same round glass jar as in the reference (tomato red #D8432B clay lid, blank strip of white masking tape across the front, nothing written), filled with a deep red raspberry coulis. Framing: the object alone, centred, fully visible, nothing cropped, filling about 70 % de la hauteur of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 50. Louche

Fichier : `louche.png` · Format : **3:2 · 1536 × 1024 px** · Place dans l'image : 80 % de la largeur · Affiché : 200 px de large

```
Image format: exactly 3:2 landscape, 1536 x 1024 pixels. A brushed steel ladle. Lying flat on its side, horizontal, seen from the same slightly high angle. Framing: the object alone, centred, fully visible, nothing cropped, filling about 80 % de la largeur of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 51. Commis · il remplit un bocal

Fichier : `commis-remplit.png` · Format : **2:3 · 1024 × 1536 px** · Place dans l'image : 88 % de la hauteur · Affiché : 330 px de haut

```
Image format: exactly 2:3 portrait, 1024 x 1536 pixels. The kitchen helper (commis), exactly the same character as in the reference images: a small young cook made of clay, round friendly face with rosy cheeks, short dark #2A2A2E hair under a small cream #F6EFE2 paper cook cap, cream #F6EFE2 cook jacket, teal #2B8C83 apron, black trousers and shoes, rounded hands, simple black dot eyes. Pose: holding a steel ladle in the right hand, tilted as if pouring, and an open glass jar (red lid removed) in the left hand. Facial expression: careful, eyes on the jar, tongue slightly out. Framing: full body, head to feet fully visible, centred horizontally, the character's total height (including any hat) is exactly 88 % of the image height, the soles of the feet 6 % above the bottom edge, so that every pose of the series has the same size and the same ground line. The character holds ONLY the objects named below: there is no table, no cutting board, no counter and no food in front of them. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

---

## 12 · Appel d’outil

### 52. Boîte d’œufs

Fichier : `boite-oeufs.png` · Format : **3:2 · 1536 × 1024 px** · Place dans l'image : 75 % de la largeur · Affiché : 180 px de large

```
Image format: exactly 3:2 landscape, 1536 x 1024 pixels. An open cardboard egg carton in cream #F6EFE2 holding 12 brown eggs. Framing: the object alone, centred, fully visible, nothing cropped, filling about 75 % de la largeur of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 53. Commis · il présente

Fichier : `commis-presente.png` · Format : **2:3 · 1024 × 1536 px** · Place dans l'image : 88 % de la hauteur · Affiché : 330 px de haut

```
Image format: exactly 2:3 portrait, 1024 x 1536 pixels. The kitchen helper (commis), exactly the same character as in the reference images: a small young cook made of clay, round friendly face with rosy cheeks, short dark #2A2A2E hair under a small cream #F6EFE2 paper cook cap, cream #F6EFE2 cook jacket, teal #2B8C83 apron, black trousers and shoes, rounded hands, simple black dot eyes. Pose: holding an open egg carton forward with both hands towards the viewer. Facial expression: proud big smile, eyes shining, eyebrows raised. Framing: full body, head to feet fully visible, centred horizontally, the character's total height (including any hat) is exactly 88 % of the image height, the soles of the feet 6 % above the bottom edge, so that every pose of the series has the same size and the same ground line. The character holds ONLY the objects named below: there is no table, no cutting board, no counter and no food in front of them. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

---

## 14 · MCP

### 54. Saladette pleine

Fichier : `saladette-pleine.png` · Format : **3:2 · 1536 × 1024 px** · Place dans l'image : 90 % de la largeur · Affiché : 360 px de large

```
Image format: exactly 3:2 landscape, 1536 x 1024 pixels. Exactly the same refrigerated brushed steel prep counter as in the reference, now with a steel gastronorm pan inserted in EVERY opening on top, each filled with a colourful ingredient (green herbs, red sauce, yellow corn, white rice, orange carrots, black olives). Framing: the object alone, centred, fully visible, nothing cropped, filling about 90 % de la largeur of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 55. Bain-marie plein

Fichier : `bain-marie-plein.png` · Format : **3:2 · 1536 × 1024 px** · Place dans l'image : 90 % de la largeur · Affiché : 320 px de large

```
Image format: exactly 3:2 landscape, 1536 x 1024 pixels. Exactly the same brushed steel bain-marie as in the reference, now with two steel gastronorm pans inserted in its openings, one with tomato red sauce, one with golden corn, a little steam rising. Framing: the object alone, centred, fully visible, nothing cropped, filling about 90 % de la largeur of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

---

## 15 · Trop d’outils

### 56. Tiroir en vrac

Fichier : `tiroir-bazar.png` · Format : **3:2 · 1536 × 1024 px** · Place dans l'image : 90 % de la largeur · Affiché : 420 px de large

```
Image format: exactly 3:2 landscape, 1536 x 1024 pixels. An open wooden kitchen drawer seen from above, overflowing with about 30 mixed utensils in total disorder (ladles, whisks, spatulas, tongs, graters, peelers, spoons, scissors, sieves), all tangled. Framing: the object alone, centred, fully visible, nothing cropped, filling about 90 % de la largeur of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 57. Ecumoire

Fichier : `ecumoire.png` · Format : **3:2 · 1536 × 1024 px** · Place dans l'image : 80 % de la largeur · Affiché : 170 px de large

```
Image format: exactly 3:2 landscape, 1536 x 1024 pixels. A flat round steel skimmer with holes and a long handle. Lying flat on its side, horizontal, seen from the same slightly high angle. Framing: the object alone, centred, fully visible, nothing cropped, filling about 80 % de la largeur of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 58. Passoire

Fichier : `passoire.png` · Format : **3:2 · 1536 × 1024 px** · Place dans l'image : 80 % de la largeur · Affiché : 170 px de large

```
Image format: exactly 3:2 landscape, 1536 x 1024 pixels. A round steel sieve with a handle. Lying flat on its side, horizontal, seen from the same slightly high angle. Framing: the object alone, centred, fully visible, nothing cropped, filling about 80 % de la largeur of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 59. Spatule

Fichier : `spatule.png` · Format : **3:2 · 1536 × 1024 px** · Place dans l'image : 80 % de la largeur · Affiché : 170 px de large

```
Image format: exactly 3:2 landscape, 1536 x 1024 pixels. A light wood spatula. Lying flat on its side, horizontal, seen from the same slightly high angle. Framing: the object alone, centred, fully visible, nothing cropped, filling about 80 % de la largeur of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 60. Pince

Fichier : `pince.png` · Format : **3:2 · 1536 × 1024 px** · Place dans l'image : 80 % de la largeur · Affiché : 170 px de large

```
Image format: exactly 3:2 landscape, 1536 x 1024 pixels. A pair of steel kitchen tongs. Lying flat on its side, horizontal, seen from the same slightly high angle. Framing: the object alone, centred, fully visible, nothing cropped, filling about 80 % de la largeur of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 61. Rape

Fichier : `rape.png` · Format : **3:2 · 1536 × 1024 px** · Place dans l'image : 80 % de la largeur · Affiché : 170 px de large

```
Image format: exactly 3:2 landscape, 1536 x 1024 pixels. A steel box grater. Lying flat on its side, horizontal, seen from the same slightly high angle. Framing: the object alone, centred, fully visible, nothing cropped, filling about 80 % de la largeur of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 62. Econome

Fichier : `econome.png` · Format : **3:2 · 1536 × 1024 px** · Place dans l'image : 80 % de la largeur · Affiché : 170 px de large

```
Image format: exactly 3:2 landscape, 1536 x 1024 pixels. A vegetable peeler with a teal handle. Lying flat on its side, horizontal, seen from the same slightly high angle. Framing: the object alone, centred, fully visible, nothing cropped, filling about 80 % de la largeur of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 63. Cuillere bois

Fichier : `cuillere-bois.png` · Format : **3:2 · 1536 × 1024 px** · Place dans l'image : 80 % de la largeur · Affiché : 170 px de large

```
Image format: exactly 3:2 landscape, 1536 x 1024 pixels. A long wooden spoon. Lying flat on its side, horizontal, seen from the same slightly high angle. Framing: the object alone, centred, fully visible, nothing cropped, filling about 80 % de la largeur of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 64. Ciseaux

Fichier : `ciseaux.png` · Format : **3:2 · 1536 × 1024 px** · Place dans l'image : 80 % de la largeur · Affiché : 170 px de large

```
Image format: exactly 3:2 landscape, 1536 x 1024 pixels. A pair of kitchen scissors with tomato red handles. Lying flat on its side, horizontal, seen from the same slightly high angle. Framing: the object alone, centred, fully visible, nothing cropped, filling about 80 % de la largeur of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

---

## 19 · Multi-agents

### 65. Saucier · il fouette

Fichier : `saucier-fouette.png` · Format : **2:3 · 1024 × 1536 px** · Place dans l'image : 88 % de la hauteur · Affiché : 360 px de haut

```
Image format: exactly 2:3 portrait, 1024 x 1536 pixels. The sauce cook, a NEW character of the same clay series: a stocky clay man, bald with a short dark beard, cream cook jacket, teal #2B8C83 neckerchief, black trousers and shoes, rounded hands, simple black dot eyes. Same character in every image. Pose: holding a small saucepan in the left hand and whisking in it with the right hand. Facial expression: focused, eyebrows drawn together, small satisfied smile. Framing: full body, head to feet fully visible, centred horizontally, the character's total height (including any hat) is exactly 88 % of the image height, the soles of the feet 6 % above the bottom edge, so that every pose of the series has the same size and the same ground line. The character holds ONLY the objects named below: there is no table, no cutting board, no counter and no food in front of them. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 66. Saucier · il attend

Fichier : `saucier-attend.png` · Format : **2:3 · 1024 × 1536 px** · Place dans l'image : 88 % de la hauteur · Affiché : 360 px de haut

```
Image format: exactly 2:3 portrait, 1024 x 1536 pixels. The sauce cook, a NEW character of the same clay series: a stocky clay man, bald with a short dark beard, cream cook jacket, teal #2B8C83 neckerchief, black trousers and shoes, rounded hands, simple black dot eyes. Same character in every image. Pose: standing, hands on hips. Facial expression: friendly confident grin. Framing: full body, head to feet fully visible, centred horizontally, the character's total height (including any hat) is exactly 88 % of the image height, the soles of the feet 6 % above the bottom edge, so that every pose of the series has the same size and the same ground line. The character holds ONLY the objects named below: there is no table, no cutting board, no counter and no food in front of them. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

---

## Toujours manquants depuis le pack n° 1

### 67. Chef · content

Fichier : `chef-content.png` · Format : **2:3 · 1024 × 1536 px** · Place dans l'image : 88 % de la hauteur · Affiché : 370 px de haut

```
Image format: exactly 2:3 portrait, 1024 x 1536 pixels. The head chef, exactly the same character as in the reference images: a taller clay chef, round face with a big dark #2A2A2E moustache, tall cream #F6EFE2 toque, cream double-breasted jacket, tomato red #D8432B neckerchief, black trousers and shoes, rounded hands, simple black dot eyes. Pose: standing, one thumb up, the other hand on his belly. Facial expression: big happy smile with eyes closed, cheeks raised, proud. Framing: full body, head to feet fully visible, centred horizontally, the character's total height (including any hat) is exactly 88 % of the image height, the soles of the feet 6 % above the bottom edge, so that every pose of the series has the same size and the same ground line. The character holds ONLY the objects named below: there is no table, no cutting board, no counter and no food in front of them. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 68. Chef · débordé

Fichier : `chef-panique.png` · Format : **2:3 · 1024 × 1536 px** · Place dans l'image : 88 % de la hauteur · Affiché : 370 px de haut

```
Image format: exactly 2:3 portrait, 1024 x 1536 pixels. The head chef, exactly the same character as in the reference images: a taller clay chef, round face with a big dark #2A2A2E moustache, tall cream #F6EFE2 toque, cream double-breasted jacket, tomato red #D8432B neckerchief, black trousers and shoes, rounded hands, simple black dot eyes. Pose: both arms up in panic, toque slightly crooked, small sweat drops flying. Facial expression: eyes wide open, mouth open in an O, eyebrows high. Framing: full body, head to feet fully visible, centred horizontally, the character's total height (including any hat) is exactly 88 % of the image height, the soles of the feet 6 % above the bottom edge, so that every pose of the series has the same size and the same ground line. The character holds ONLY the objects named below: there is no table, no cutting board, no counter and no food in front of them. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

---

## 23 · Coût et délai

### 69. Addition

Fichier : `addition.png` · Format : **2:3 · 1024 × 1536 px** · Place dans l'image : 80 % de la hauteur · Affiché : 260 px de haut

```
Image format: exactly 2:3 portrait, 1024 x 1536 pixels. A long white paper restaurant receipt, slightly curled at the bottom, with faint grey lines but nothing written. Framing: the object alone, centred, fully visible, nothing cropped, filling about 80 % de la hauteur of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 70. Pièces

Fichier : `pieces.png` · Format : **1:1 · 1024 × 1024 px** · Place dans l'image : 55 % · Affiché : 90 px de large

```
Image format: exactly 1:1 square, 1024 x 1024 pixels. A small pile of gold coins, plain, no symbols. Framing: the object alone, centred, fully visible, nothing cropped, filling about 55 % of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 71. Sablier

Fichier : `sablier.png` · Format : **2:3 · 1024 × 1536 px** · Place dans l'image : 70 % de la hauteur · Affiché : 160 px de haut

```
Image format: exactly 2:3 portrait, 1024 x 1536 pixels. An hourglass with a light wood frame and mustard yellow sand, half run through. Framing: the object alone, centred, fully visible, nothing cropped, filling about 70 % de la hauteur of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

---

## 24 et 25 · Injection, données confidentielles

### 72. Carnet secret

Fichier : `carnet-secret.png` · Format : **1:1 · 1024 × 1024 px** · Place dans l'image : 65 % · Affiché : 150 px de large

```
Image format: exactly 1:1 square, 1024 x 1024 pixels. A thick notebook with a dark ink #2A2A2E leather cover, closed with a strap and a small brass padlock. Framing: the object alone, centred, fully visible, nothing cropped, filling about 65 % of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```

### 73. Coffre

Fichier : `coffre.png` · Format : **1:1 · 1024 × 1024 px** · Place dans l'image : 65 % · Affiché : 160 px de large

```
Image format: exactly 1:1 square, 1024 x 1024 pixels. A small brushed steel safe with a round dial, door closed. Framing: the object alone, centred, fully visible, nothing cropped, filling about 65 % of the image. Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image of the series, so objects show their top and their front. Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image. Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1. Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.
```
