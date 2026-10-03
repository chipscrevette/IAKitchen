# Pack de prompts « la cuisine » : UNE image par asset, format et pixels exacts pour chacun.
# Sortie : CUISINE-PROMPTS.md (sommaire + un bloc autonome à coller par image).
import os

STYLE = ("Style: handmade plasticine / modelling clay miniature, stop-motion look, soft rounded shapes, matte clay surface "
         "with subtle fingerprints and tiny imperfections, clean and cute but not childish, soft warm studio light coming "
         "from the top-left. Absolutely no text, no letters, no numbers, no logo anywhere in the image.")
ANGLE = ("Camera: slightly high angle, looking down at about 30 degrees from the front, the same angle for every image "
         "of the series, so objects show their top and their front.")
PALETTE = ("Colour palette of the whole series: warm light wood #D9A66B, white marble #EDEAE3, cream #F6EFE2, "
           "tomato red #D8432B, teal #2B8C83, mustard yellow #E0A21B, dark ink #2A2A2E, brushed steel light grey #C9CDD1.")
FOND = ("Background: transparent (PNG with alpha channel). If your tool cannot make transparency, use a perfectly flat, "
        "uniform pure white background #FFFFFF with no gradient. No floor, no table, no cast shadow, no other object.")

FORMATS = {
    '16:9': ('exactly 16:9 landscape, 1920 x 1080 pixels (or 2560 x 1440 if possible)', '16:9 · 1920 × 1080 px (ou 2560 × 1440)'),
    '1:1': ('exactly 1:1 square, 1024 x 1024 pixels', '1:1 · 1024 × 1024 px'),
    '3:2': ('exactly 3:2 landscape, 1536 x 1024 pixels', '3:2 · 1536 × 1024 px'),
    '2:3': ('exactly 2:3 portrait, 1024 x 1536 pixels', '2:3 · 1024 × 1536 px'),
}

SECTIONS = []   # (titre de section, [assets])
def section(titre): SECTIONS.append((titre, []))
def asset(fichier, nom, fmt, remplissage, affiche, sujet, cadrage=None, visage=None, fond=FOND, angle=ANGLE):
    en, fr = FORMATS[fmt]
    cad = cadrage or (f"Framing: the object alone, centred, fully visible, nothing cropped, filling about {remplissage} of the image.")
    parties = [f"Image format: {en}.", sujet, cad, angle, STYLE, PALETTE, fond]
    if visage: parties.insert(2, visage)
    SECTIONS[-1][1].append(dict(fichier=fichier, nom=nom, fmt=fr, remplissage=remplissage, affiche=affiche, prompt=' '.join(parties)))

# identités des deux personnages (mêmes mots dans chaque pose)
COMMIS = ("The kitchen helper (commis): a small young cook made of clay, round friendly face with rosy cheeks, short dark "
          "#2A2A2E hair under a small cream #F6EFE2 paper cook cap, cream #F6EFE2 cook jacket, teal #2B8C83 apron, black "
          "trousers and shoes, rounded hands, simple black dot eyes. Exactly the same character in every image.")
CHEF = ("The head chef: a taller clay chef, round face with a big dark #2A2A2E moustache, tall cream #F6EFE2 toque, cream "
        "#F6EFE2 double-breasted jacket, tomato red #D8432B neckerchief, black trousers and shoes, rounded hands, simple black "
        "dot eyes. Exactly the same character in every image.")
PERSO_CADRE = ("Framing: full body, head to feet fully visible, centred horizontally, the character's total height (including "
               "the hat) is exactly 88 % of the image height, the soles of the feet 6 % above the bottom edge, so that every "
               "pose of the series has the same size and the same ground line.")
def perso(fichier, nom, qui, pose, visage, affiche):
    asset(fichier, nom, '2:3', '88 % de la hauteur', affiche, (CHEF if qui == 'chef' else COMMIS) + ' ' + pose,
          cadrage=PERSO_CADRE, visage=visage)

# ── 0. le fond ──
section('Le fond (sert à toutes les notions)')
asset('plan-de-travail.png', 'Le plan de travail', '16:9', 'toute l’image', 'plein écran, 1900 × 1069 px',
      "A long empty kitchen countertop seen from above at a high angle, filling the ENTIRE image edge to edge: the left two "
      "thirds are warm light wood butcher block #D9A66B, the right third is a smooth white marble slab #EDEAE3 with soft grey "
      "veins #BDB7AC. Along the very top edge only, a thin strip of cream #F6EFE2 square wall tiles with a horizontal steel "
      "ticket rail. The countertop surface takes at least 85 % of the image height. Completely empty and tidy: no object, no food, no utensil.",
      cadrage="Framing: the countertop fills the frame edge to edge, lots of free space.",
      fond="Background: none, the countertop itself fills the entire image.",
      angle="Camera: high angle, almost top-down, about 75 degrees.")

# ── 1. RAG : la tarte de la maison ──
section('RAG · la tarte de la maison')
asset('cocotte.png', 'La cocotte (grande préparation)', '1:1', '75 %', '250 px de large',
      "A big round cast-iron casserole pot in tomato red #D8432B with its lid on and a dark ink #2A2A2E knob, two small handles.")
asset('saladier.png', 'Le saladier (grande préparation)', '1:1', '75 %', '210 px de large',
      "A large round ceramic mixing bowl, cream #F6EFE2 inside with a teal #2B8C83 rim, filled with a smooth cream-coloured preparation.")
asset('marmite.png', 'La marmite (grande préparation)', '1:1', '75 %', '220 px de large',
      "A tall brushed steel #C9CDD1 stock pot with two handles and no lid, filled with a golden mustard #E0A21B preparation, a wooden spoon resting inside.")
asset('pichet.png', 'Le pichet (grande préparation)', '1:1', '65 %', '150 px de large',
      "A teal #2B8C83 ceramic jug with a handle, filled with a deep red sauce.")
asset('bocal.png', 'Le bocal étiqueté', '1:1', '70 % de la hauteur', '96 px de large',
      "One round glass kitchen jar with a tomato red #D8432B clay lid, slightly bluish transparent glass, empty, and a blank "
      "strip of white masking tape stuck horizontally across the front of the jar (the tape is empty, nothing written).")
asset('ticket.png', 'Le ticket de commande', '1:1', '65 % de la hauteur', '150 px de large',
      "One small white paper kitchen order ticket, portrait orientation, slightly curled, with a thin tomato red #D8432B "
      "stripe at the top and nothing written on it, lying flat.")
asset('plateau.png', 'Le plateau de service', '3:2', '85 % de la largeur', '380 px de large',
      "An empty rectangular serving tray in teal #2B8C83 clay with low rounded edges, lying flat.")
asset('tarte.png', 'La tarte de la maison', '1:1', '75 %', '220 px de large',
      "A round white plate with a slice of pear and almond tart: golden crust in mustard yellow #E0A21B, fanned pear slices "
      "in cream #F6EFE2, a few flaked almonds on top.")
asset('tarte-pommes.png', 'La tarte ratée (sans RAG)', '1:1', '75 %', '220 px de large',
      "A round white plate with a slice of a very ordinary apple tart: pale crust, thin apple slices in a plain circle, "
      "nothing special, a bit sad-looking.")
perso('commis-goute.png', 'Commis · il goûte', 'commis',
      "Pose: standing, holding a small tasting spoon to his mouth, the other hand on his hip.",
      "Facial expression: eyes half closed in concentration, eyebrows slightly raised, lips pursed on the spoon, head tilted a little to the side, as if analysing a subtle taste.", '330 px de haut')
perso('commis-ecrit.png', 'Commis · il étiquette', 'commis',
      "Pose: standing, leaning forward, writing with a black marker with a mustard yellow #E0A21B cap on a strip of masking tape stuck on a glass jar he holds in the other hand.",
      "Facial expression: focused, eyes looking down at the tape, tongue slightly out at the corner of the mouth, eyebrows drawn together.", '330 px de haut')
perso('commis-range.png', 'Commis · il range', 'commis',
      "Pose: walking to the side, carrying one glass jar with a tomato red #D8432B lid in both hands in front of his chest.",
      "Facial expression: calm and confident, small smile, eyes looking ahead to where he will place the jar.", '330 px de haut')
perso('commis-imagine.png', 'Commis · il imagine le goût', 'commis',
      "Pose: standing, holding a small white order ticket in one hand, the other hand touching his chin.",
      "Facial expression: eyes closed, dreamy smile, eyebrows raised, as if imagining a delicious taste.", '330 px de haut')
perso('chef-attend.png', 'Chef · il attend', 'chef',
      "Pose: standing still, arms crossed on his chest.",
      "Facial expression: neutral and ready, eyes looking forward, eyebrows relaxed, mouth closed under the moustache.", '370 px de haut')
perso('chef-improvise.png', 'Chef · il improvise (bluff)', 'chef',
      "Pose: standing, one hand scratching the back of his head under the toque, the other hand raised with the index finger up as if giving an answer anyway.",
      "Facial expression: overconfident bluff, big forced smile, one eyebrow raised, eyes looking sideways, one small sweat drop on the forehead.", '370 px de haut')
perso('chef-cuisine.png', 'Chef · il cuisine', 'chef',
      "Pose: standing, holding a frying pan with a wooden handle in one hand, reading a small white order ticket held in the other hand.",
      "Facial expression: satisfied and sure of himself, eyes on the ticket, small confident smile.", '370 px de haut')

# ── 2. Token : la planche à découper ──
section('Token · la planche à découper')
asset('planche.png', 'La planche à découper', '3:2', '85 % de la largeur', '440 px de large',
      "A large rectangular wooden cutting board in warm light wood #D9A66B with a darker rim and a small round handle hole, empty, lying flat.")
asset('couteau.png', 'Le couteau de chef', '3:2', '80 % de la largeur', '220 px de large',
      "A chef's knife lying flat, horizontal, blade pointing right, light grey steel blade with a soft shine, dark ink #2A2A2E handle with two small rivets.")
for c, hexa in [('creme', 'cream #F6EFE2'), ('tomate', 'tomato red #D8432B'), ('sarcelle', 'teal #2B8C83'), ('moutarde', 'mustard yellow #E0A21B')]:
    asset(f'de-{c}.png', f'Dé vierge ({c})', '1:1', '45 %', '70 px de large',
          f"One small clay cube like a diced vegetable piece, in {hexa}, completely plain on every face, slightly rounded edges.")
asset('balance.png', 'La balance de cuisine', '1:1', '75 %', '240 px de large',
      "A kitchen scale with a flat steel plate on top and a blank cream #F6EFE2 display with nothing shown on it, body in teal #2B8C83.")
asset('carotte.png', 'La carotte entière', '3:2', '75 % de la largeur', '200 px de large',
      "One whole carrot lying flat horizontally, bright orange with a green leafy top.")

# ── 3. Température : le feu ──
section('Température · le feu sous la poêle')
asset('feu-eteint.png', 'Le feu éteint', '1:1', '75 %', '230 px de large',
      "A round gas burner with a black cast iron grate, switched off, no flame.")
asset('feu-doux.png', 'Le feu doux', '1:1', '75 %', '230 px de large',
      "The same round gas burner with a black cast iron grate, with a small gentle ring of blue flames.")
asset('feu-vif.png', 'Le feu vif', '1:1', '75 %', '230 px de large',
      "The same round gas burner with a black cast iron grate, with big roaring orange and yellow flames.")
asset('bouton.png', 'Le bouton de gazinière', '1:1', '45 %', '90 px de large',
      "One round stove knob in dark ink #2A2A2E seen from the front, with a small white pointer line pointing straight up.")
asset('poele.png', 'La poêle vide', '3:2', '85 % de la largeur', '300 px de large',
      "An empty frying pan with a dark ink #2A2A2E non-stick inside and a warm light wood #D9A66B handle pointing right.")
asset('poele-steak.png', 'La poêle, steak parfait', '3:2', '85 % de la largeur', '300 px de large',
      "The same frying pan, handle pointing right, containing a perfectly seared golden-brown steak.")
asset('poele-brule.png', 'La poêle, plat brûlé', '3:2', '85 % de la largeur', '300 px de large',
      "The same frying pan, handle pointing right, containing a completely burnt black piece of food with small grey clay smoke puffs above it.")

# ── 4. Fenêtre de contexte : le plan de travail trop petit ──
section('Fenêtre de contexte · le plan de travail qui déborde')
asset('poubelle.png', 'La poubelle', '2:3', '75 % de la hauteur', '220 px de haut',
      "A brushed steel #C9CDD1 kitchen pedal bin with its lid wide open.")
for f, n, s in [('tomate', 'La tomate', 'One ripe round tomato in tomato red #D8432B with a small green stem.'),
                ('oignon', 'L’oignon', 'One golden-brown onion with dry papery skin.'),
                ('citron', 'Le citron', 'One bright lemon in mustard yellow #E0A21B.'),
                ('fromage', 'Le fromage', 'One wedge of yellow cheese with round holes.'),
                ('oeufs', 'Les œufs', 'Two brown eggs side by side.'),
                ('beurre', 'Le beurre', 'One block of pale yellow butter on a small cream #F6EFE2 dish.')]:
    asset(f'{f}.png', n, '1:1', '60 %', '110 px de large', s)

# ── 5. Hallucination : la cloche ──
section('Hallucination · sous la cloche')
asset('cloche-fermee.png', 'La cloche fermée', '1:1', '75 %', '260 px de large',
      "A closed shiny steel serving cloche on a round white plate.")
asset('cloche-ouverte.png', 'La cloche ouverte, plat inventé', '1:1', '85 %', '300 px de large',
      "The same shiny steel cloche lifted and tilted to the side, revealing a strange, clearly invented dish on the round white plate: a wobbly purple and green jelly with a fish tail sticking out of it.")

# ── 6. Fine-tuning : le stage ──
section('Fine-tuning · le chef part en stage')
asset('livre.png', 'Le gros livre de pâtisserie', '1:1', '70 %', '200 px de large',
      "A big thick closed cookbook with a tomato red #D8432B cover and cream #F6EFE2 page edges, lying flat.")
asset('gateau.png', 'Le gâteau de retour de stage', '1:1', '70 %', '200 px de large',
      "A small round layered cake on a cream plate, decorated with cream swirls and three red berries on top.")
perso('chef-etudie.png', 'Chef · il étudie', 'chef',
      "Pose: sitting on a small wooden stool, reading a big thick book open on his knees, reading glasses on the tip of his nose.",
      "Facial expression: very focused, eyebrows drawn together, lips pressed, eyes on the page.", '370 px de haut')
perso('chef-diplome.png', 'Chef · de retour de stage', 'chef',
      "Pose: standing proud with a big mustard yellow #E0A21B rosette medal pinned on his jacket, holding a small cake decorated with cream swirls.",
      "Facial expression: chin up, proud satisfied smile, eyes half closed with pride.", '370 px de haut')

# ── 7. Appel d'outil : le chef demande, le commis exécute ──
section('Appel d’outil · le chef demande, le commis va chercher')
asset('chambre-froide.png', 'La porte de chambre froide', '2:3', '85 % de la hauteur', '520 px de haut',
      "A heavy brushed steel #C9CDD1 walk-in cold room door with a big lever handle, closed, seen from the front, standing upright.")
asset('telephone.png', 'Le téléphone mural', '2:3', '60 % de la hauteur', '220 px de haut',
      "A vintage cream #F6EFE2 wall telephone with its handset hanging on the side and a curly cord, seen from the front.")
asset('carnet.png', 'Le carnet de bons', '1:1', '60 %', '150 px de large',
      "A small spiral order pad with blank cream #F6EFE2 pages and a pencil lying on it.")
perso('chef-appelle.png', 'Chef · il appelle une commande', 'chef',
      "Pose: one hand cupped next to his mouth calling out to someone off to the side, the other hand pointing in that direction.",
      "Facial expression: mouth wide open calling, eyebrows raised, energetic and commanding.", '370 px de haut')
perso('commis-court.png', 'Commis · il court chercher', 'commis',
      "Pose: running fast to the side, one foot in the air, carrying a brushed steel rectangular kitchen container in both hands.",
      "Facial expression: determined, eyebrows slightly drawn, small confident smile, eyes looking ahead.", '330 px de haut')
perso('commis-telephone.png', 'Commis · il téléphone', 'commis',
      "Pose: holding a vintage cream telephone handset with a curly cord to his ear, the other hand writing on a small order pad.",
      "Facial expression: attentive, eyes looking up to the side while listening, mouth slightly open.", '330 px de haut')
perso('commis-ecoute.png', 'Commis · il écoute le chef', 'commis',
      "Pose: standing straight, hands behind his back, head slightly tilted up as if listening to someone taller.",
      "Facial expression: nodding with a small attentive smile, eyebrows slightly raised.", '330 px de haut')

# ── 8. MCP : la norme gastro ──
section('MCP · les bacs gastronormes')
GN = "brushed steel #C9CDD1 professional kitchen container (gastronorm pan) with a flat folded rim, seen from slightly above"
asset('gn-1-1.png', 'Bac GN 1/1 (entier)', '3:2', '85 % de la largeur', '300 px de large',
      f"One full-size rectangular {GN}, proportions 53 x 32.5 cm, filled with fresh green herbs.")
asset('gn-1-2.png', 'Bac GN 1/2 (demi)', '1:1', '70 % de la largeur', '180 px de large',
      f"One half-size {GN}, almost square, proportions 32.5 x 26.5 cm, filled with tomato red #D8432B sauce.")
asset('gn-1-3.png', 'Bac GN 1/3 (tiers)', '3:2', '65 % de la largeur', '180 px de large',
      f"One third-size {GN}, long and narrow, proportions 32.5 x 17.6 cm, filled with mustard yellow #E0A21B corn.")
asset('gn-1-6.png', 'Bac GN 1/6 (sixième)', '1:1', '55 % de la largeur', '100 px de large',
      f"One small sixth-size {GN}, almost square, proportions 17.6 x 16.2 cm, filled with cream #F6EFE2 rice.")
asset('saladette.png', 'La saladette réfrigérée', '3:2', '90 % de la largeur', '330 px de large',
      "A refrigerated brushed steel #C9CDD1 prep counter with a row of empty rectangular openings on top, exactly the shape the steel kitchen containers fit into.")
asset('four.png', 'Le four mixte', '1:1', '80 %', '300 px de large',
      "A brushed steel #C9CDD1 professional combi oven, door closed, with a dark glass window and one round dark ink #2A2A2E knob.")
asset('bain-marie.png', 'Le bain-marie', '3:2', '90 % de la largeur', '330 px de large',
      "A brushed steel #C9CDD1 bain-marie with two empty rectangular openings on top, a little steam rising.")
asset('boites-bricolees.png', 'Les boîtes bricolées', '3:2', '85 % de la largeur', '300 px de large',
      "A messy group of three mismatched home-made containers that obviously do not fit together: a round tomato red #D8432B plastic box, a crooked teal #2B8C83 tupperware whose lid does not close, a tiny mustard #E0A21B jar with a string around it.")
perso('commis-porte-bac.png', 'Commis · il porte un bac', 'commis',
      "Pose: walking calmly, holding a full-size brushed steel rectangular kitchen container flat in front of him with both hands.",
      "Facial expression: careful and calm, eyes on the container, small smile.", '330 px de haut')

# ── 9. Agent : le coup de feu ──
section('Agent · le chef en plein coup de feu')
asset('minuteur.png', 'Le minuteur', '1:1', '55 %', '110 px de large',
      "A round kitchen timer shaped like a tomato #D8432B with a small green stem on top.")
asset('sonnette.png', 'La sonnette de service', '1:1', '50 %', '110 px de large',
      "A small chrome service bell of the kind you tap on a counter.")
asset('saliere.png', 'La salière', '1:1', '50 %', '90 px de large',
      "A small cream #F6EFE2 ceramic salt shaker with holes on top.")
perso('chef-goute.png', 'Chef · il goûte et grimace', 'chef',
      "Pose: holding a small tasting spoon at his lips, the other hand on his hip.",
      "Facial expression: one eye closed, nose wrinkled, mouth twisted to the side, clearly thinking it needs something more.", '370 px de haut')
perso('chef-sale.png', 'Chef · il rectifie', 'chef',
      "Pose: sprinkling a pinch of salt from high up with his fingers, the other hand holding a small salt shaker.",
      "Facial expression: focused, tongue slightly out at the corner of the mouth, eyes on his fingers.", '370 px de haut')
perso('chef-content.png', 'Chef · content', 'chef',
      "Pose: standing, one thumb up, the other hand on his belly.",
      "Facial expression: big happy smile with eyes closed, cheeks raised, proud.", '370 px de haut')
perso('chef-panique.png', 'Chef · débordé', 'chef',
      "Pose: both arms up in panic, toque slightly crooked, small sweat drops flying around his head.",
      "Facial expression: eyes wide open, mouth open in an O, eyebrows high, total panic.", '370 px de haut')
perso('commis-presente.png', 'Commis · il présente l’assiette', 'commis',
      "Pose: holding a small white plate forward with both hands towards the viewer.",
      "Facial expression: proud big smile, eyes shining, eyebrows raised.", '330 px de haut')
perso('commis-coupe.png', 'Commis · il coupe en dés', 'commis',
      "Pose: standing behind a small wooden cutting board, cutting a carrot into small cubes with a chef's knife.",
      "Facial expression: concentrated, eyes on the knife, lips pressed, eyebrows slightly drawn together.", '330 px de haut')

# ── écriture ──
tous = [a for _, l in SECTIONS for a in l]
L = ["# Pack d'images · La cuisine", "",
     f"**{len(tous)} images, une par asset.** Chaque bloc donne le nom du fichier, le format exact en pixels, la place que l'objet doit prendre dans l'image et la taille à laquelle il sera affiché dans la scène.", "",
     "## Mode d'emploi", "",
     "1. Génère d'abord **le plan de travail**, puis **une première pose de chaque personnage** (`commis-goute.png` et `chef-attend.png`).",
     "2. Pour **toutes les autres images**, joins en image de référence le plan de travail et, pour un personnage, sa première pose réussie. Ajoute cette phrase à la fin du prompt : « Keep exactly the same clay style, lighting, camera angle and character design as the reference images. »",
     "3. **Une image = un seul objet**, fond transparent (ou blanc pur #FFFFFF si ton outil ne sait pas faire).",
     "4. Si ton outil le permet, génère **au double** de la taille indiquée (par exemple 2048 × 2048 au lieu de 1024 × 1024) : c'est plus net.",
     "5. Dépose les fichiers dans `sources/brut/` **avec exactement le nom indiqué**, puis lance `python outils/images/preparer_images.py` (détourage, mise à l'échelle, tailles.js).",
     "Les formats utilisés :", "",
     "| Format | Pixels | Pour quoi |", "|---|---|---|",
     "| 16:9 | 1920 × 1080 (ou 2560 × 1440) | le fond |",
     "| 1:1 | 1024 × 1024 | les objets ronds ou compacts |",
     "| 3:2 | 1536 × 1024 | les objets longs : planche, couteau, poêles, plateau, bacs larges |",
     "| 2:3 | 1024 × 1536 | tout ce qui est debout : les personnages, la porte, le téléphone, la poubelle |", "",
     "## Sommaire", "", "| # | Fichier | Asset | Format | Place dans l'image | Affiché dans la scène |", "|---|---|---|---|---|---|"]
n = 0
for titre, l in SECTIONS:
    L.append(f"| | **{titre}** | | | | |")
    for a in l:
        n += 1; a['n'] = n
        L.append(f"| {n} | `{a['fichier']}` | {a['nom']} | {a['fmt']} | {a['remplissage']} | {a['affiche']} |")
L.append("")
for titre, l in SECTIONS:
    L += ["---", "", f"## {titre}", ""]
    for a in l:
        L += [f"### {a['n']}. {a['nom']}", "",
              f"Fichier : `{a['fichier']}` · Format : **{a['fmt']}** · Place dans l'image : {a['remplissage']} · Affiché : {a['affiche']}", "",
              "```", a['prompt'], "```", ""]
out = os.path.join(os.path.dirname(__file__), '..', '..', 'docs', 'prompts', 'pack-1.md')
with open(out, 'w', encoding='utf-8') as fh: fh.write('\n'.join(L))
print(len(tous), 'images ->', os.path.abspath(out))
