# Pack de prompts n° 2 « la cuisine » : les assets qui manquent au storyboard (STORYBOARD.md).
# UNE image par asset, format et pixels exacts, rangés par chapitre. Sortie : CUISINE-PROMPTS-2.md
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
    '1:1': ('exactly 1:1 square, 1024 x 1024 pixels', '1:1 · 1024 × 1024 px'),
    '3:2': ('exactly 3:2 landscape, 1536 x 1024 pixels', '3:2 · 1536 × 1024 px'),
    '2:3': ('exactly 2:3 portrait, 1024 x 1536 pixels', '2:3 · 1024 × 1536 px'),
    '3:1': ('exactly 3:1 wide landscape, 1536 x 512 pixels', '3:1 · 1536 × 512 px'),
}
SECTIONS = []
def section(t): SECTIONS.append((t, []))
def asset(fichier, nom, fmt, remplissage, affiche, sujet, cadrage=None, visage=None):
    en, fr = FORMATS[fmt]
    cad = cadrage or f"Framing: the object alone, centred, fully visible, nothing cropped, filling about {remplissage} of the image."
    parties = [f"Image format: {en}.", sujet, cad, ANGLE, STYLE, PALETTE, FOND]
    if visage: parties.insert(2, visage)
    SECTIONS[-1][1].append(dict(fichier=fichier, nom=nom, fmt=fr, remplissage=remplissage, affiche=affiche, prompt=' '.join(parties)))

PERSO_CADRE = ("Framing: full body, head to feet fully visible, centred horizontally, the character's total height (including "
               "any hat) is exactly 88 % of the image height, the soles of the feet 6 % above the bottom edge, so that every "
               "pose of the series has the same size and the same ground line. The character holds ONLY the objects named "
               "below: there is no table, no cutting board, no counter and no food in front of them.")
QUI = {
    'commis': ("The kitchen helper (commis), exactly the same character as in the reference images: a small young cook made of clay, "
               "round friendly face with rosy cheeks, short dark #2A2A2E hair under a small cream #F6EFE2 paper cook cap, cream "
               "#F6EFE2 cook jacket, teal #2B8C83 apron, black trousers and shoes, rounded hands, simple black dot eyes."),
    'chef': ("The head chef, exactly the same character as in the reference images: a taller clay chef, round face with a big dark "
             "#2A2A2E moustache, tall cream #F6EFE2 toque, cream double-breasted jacket, tomato red #D8432B neckerchief, black "
             "trousers and shoes, rounded hands, simple black dot eyes."),
    'serveur': ("The waiter, a NEW character of the same clay series: a tall slim clay waiter, neat side-parted dark #2A2A2E hair, "
                "a thin moustache, white shirt with rolled sleeves, black waistcoat, black bow tie, long white apron down to the "
                "knees, black trousers and shoes, rounded hands, simple black dot eyes. Same character in every image."),
    'patronne': ("The owner (la patronne), a NEW character of the same clay series: a clay woman in her sixties, grey hair in a neat "
                 "bun, round glasses, a burgundy cardigan over a cream #F6EFE2 blouse, dark ink #2A2A2E skirt, black shoes, a "
                 "pencil behind her ear, rounded hands, simple black dot eyes behind the glasses. Same character in every image."),
    'critique': ("The food critic, a NEW character of the same clay series: a thin clay man with a small dark ink #2A2A2E beret, "
                 "round glasses, a long mustard yellow #E0A21B scarf, a grey jacket, dark trousers and shoes, rounded hands, "
                 "simple black dot eyes. Same character in every image."),
    'patissiere': ("The pastry chef, a NEW character of the same clay series: a clay young woman with short curly dark hair under a "
                   "tall cream #F6EFE2 toque, cream double-breasted jacket, mustard yellow #E0A21B neckerchief, black trousers and "
                   "shoes, rounded hands, simple black dot eyes. Same character in every image."),
    'saucier': ("The sauce cook, a NEW character of the same clay series: a stocky clay man, bald with a short dark beard, cream "
                "cook jacket, teal #2B8C83 neckerchief, black trousers and shoes, rounded hands, simple black dot eyes. Same "
                "character in every image."),
}
HAUT = {'commis': '330', 'chef': '370', 'serveur': '380', 'patronne': '350', 'critique': '360', 'patissiere': '360', 'saucier': '360'}
def perso(fichier, nom, qui, pose, visage):
    asset(fichier, nom, '2:3', '88 % de la hauteur', HAUT[qui] + ' px de haut', QUI[qui] + ' ' + pose, cadrage=PERSO_CADRE, visage=visage)
POSE_OBJET = "Lying flat on its side, horizontal, seen from the same slightly high angle."

# ── APÉRITIF ──
section('1 · Le mot suivant')
asset('sac-farine.png', 'Sac de farine', '2:3', '75 % de la hauteur', '170 px de haut',
      "A paper flour bag in cream #F6EFE2, the top rolled down and open, a little white flour visible inside, a small dusting of flour at its base.")
asset('brique-lait.png', 'Brique de lait', '2:3', '75 % de la hauteur', '150 px de haut',
      "A milk carton with a gable top, white with a teal #2B8C83 band, closed, standing upright.")
asset('paquet-sucre.png', 'Paquet de sucre', '1:1', '65 %', '110 px de large',
      "A small white box of sugar with a mustard yellow #E0A21B band, standing upright, a few sugar cubes in front of it.")
asset('fouet.png', 'Fouet', '3:2', '80 % de la largeur', '200 px de large', "A steel balloon whisk with a dark ink #2A2A2E handle. " + POSE_OBJET)
asset('poele-crepe.png', 'Poêle avec une crêpe', '3:2', '85 % de la largeur', '300 px de large',
      "The same frying pan as in the reference (dark ink #2A2A2E inside, light wood #D9A66B handle pointing right) containing one thin golden crêpe with light brown spots.")
perso('chef-verse.png', 'Chef · il verse', 'chef',
      "Pose: holding a milk carton in the right hand, tilted forward and down as if pouring into something in front of him, the left hand on his hip.",
      "Facial expression: focused and confident, eyes looking down at where he pours, small smile under the moustache.")

section('2 · Token')
asset('carotte-longue.png', 'Carotte très longue', '3:1', '92 % de la largeur', '700 px de long',
      "One very long, straight, thick carrot, about 8 times longer than it is thick, bright orange with fine rings, green leafy top at the left end. " + POSE_OBJET)
asset('carotte-fine.png', 'Carotte fine', '3:1', '90 % de la largeur', '420 px de long',
      "One long thin carrot, about 12 times longer than it is thick, bright orange, small green leafy top at the left end. " + POSE_OBJET)
asset('troncon-court.png', 'Tronçon de carotte court', '1:1', '55 %', '48 px de long',
      "One short piece of carrot cut with a knife at both ends, as long as it is thick, both cut faces clean and visible showing the paler orange flesh with rings. " + POSE_OBJET)
asset('troncon-moyen.png', 'Tronçon de carotte moyen', '3:2', '70 % de la largeur', '90 px de long',
      "One piece of carrot cut with a knife at both ends, twice as long as it is thick, both cut faces clean showing the paler orange flesh with rings. " + POSE_OBJET)
asset('troncon-long.png', 'Tronçon de carotte long', '3:1', '80 % de la largeur', '170 px de long',
      "One piece of carrot cut with a knife at both ends, four times as long as it is thick, both cut faces clean showing the paler orange flesh with rings. " + POSE_OBJET)
perso('commis-coupe.png', 'Commis · il coupe', 'commis',
      "Pose: standing, the chef's knife held in the right hand with the blade pointing down and forward, as if slicing something on a table just in front of him, the left hand flat and slightly forward as if holding the food in place.",
      "Facial expression: concentrated, eyes looking down at the knife, lips pressed, eyebrows slightly drawn together.")
perso('serveur-ticket.png', 'Serveur · il apporte un ticket', 'serveur',
      "Pose: holding a small white order ticket forward in the right hand at chest height, the left arm folded behind his back.",
      "Facial expression: polite professional smile, eyebrows slightly raised, eyes looking forward.")

section('3 · Température')
EPICES = [('sel', 'coarse white salt'), ('poivre', 'black peppercorns'), ('sucre', 'white sugar crystals'), ('paprika', 'bright red paprika powder'),
          ('thym', 'dried green thyme'), ('piment', 'small dried red chillies'), ('cannelle', 'brown cinnamon sticks'), ('chocolat', 'dark chocolate chips')]
for n, c in EPICES:
    asset(f'epice-{n}.png', f'Pot à épices · {n}', '1:1', '60 % de la hauteur', '90 px de haut',
          f"One small round glass spice jar with a cork stopper, as tall as it is wide, filled with {c}, a blank strip of white masking tape across the front (nothing written).")
asset('poele-sauce.png', 'Poêle de sauce', '3:2', '85 % de la largeur', '300 px de large',
      "The same frying pan as in the reference (dark ink inside, light wood handle pointing right) filled with a glossy tomato red #D8432B sauce.")
asset('poele-sauce-brulee.png', 'Poêle de sauce brûlée', '3:2', '85 % de la largeur', '300 px de large',
      "The same frying pan, handle pointing right, with the sauce burnt into a black crust and small grey clay smoke puffs rising.")

section('4 · Entraînement')
asset('pile-livres.png', 'Pile de livres de recettes', '2:3', '85 % de la hauteur', '420 px de haut',
      "A tall slightly wobbly stack of about 15 thick cookbooks of different sizes, covers in tomato red, teal, mustard, cream and dark ink, lying flat on top of each other.")
asset('diplome.png', 'Diplôme', '3:2', '75 % de la largeur', '180 px de large',
      "A rolled cream #F6EFE2 parchment diploma tied with a tomato red #D8432B ribbon and a small wax seal. " + POSE_OBJET)
perso('commis-lit.png', 'Commis · il lit', 'commis',
      "Pose: standing, reading an open thick cookbook held in both hands in front of his chest.",
      "Facial expression: absorbed, eyes on the page, mouth slightly open, eyebrows raised with curiosity.")
perso('critique-goute.png', 'Critique · il goûte', 'critique',
      "Pose: tasting from a small spoon held in the right hand, a small notebook in the left hand.",
      "Facial expression: eyes closed, one eyebrow raised, lips pursed, judging seriously.")
perso('critique-note.png', 'Critique · il note', 'critique',
      "Pose: writing in his small notebook with a pencil.",
      "Facial expression: stern, one eyebrow raised, eyes on the notebook.")

section('6 · Fine-tuning (et tous les chapitres où la patronne apparaît)')
perso('patronne-lit.png', 'Patronne · elle lit un bon', 'patronne',
      "Pose: holding a small paper slip in both hands and reading it through her glasses.",
      "Facial expression: attentive, eyebrows raised, lips pressed.")
perso('patronne-signe.png', 'Patronne · elle signe', 'patronne',
      "Pose: signing a paper slip held against her left palm with a pencil.",
      "Facial expression: satisfied small smile, eyes on the paper.")
perso('patronne-refuse.png', 'Patronne · elle refuse', 'patronne',
      "Pose: right hand raised flat, palm forward, in a firm stop gesture, the left hand holding a paper slip.",
      "Facial expression: stern, eyebrows drawn together, mouth firm.")
perso('patissiere-poche.png', 'Pâtissière · elle garnit', 'patissiere',
      "Pose: holding a piping bag in both hands, pressing it as if piping cream downwards.",
      "Facial expression: focused, tongue slightly out at the corner of the mouth.")
perso('patissiere-attend.png', 'Pâtissière · elle attend', 'patissiere',
      "Pose: standing, arms crossed.", "Facial expression: confident friendly smile.")

# ── ENTRÉES ──
section('7 · Fenêtre de contexte')
asset('seau-compost.png', 'Seau à compost', '1:1', '65 %', '150 px de haut',
      "A small countertop compost bin in cream #F6EFE2 enamel with a teal #2B8C83 lid wide open, a few vegetable peels visible inside.")
perso('serveur-attend.png', 'Serveur · il attend', 'serveur',
      "Pose: standing straight, a white napkin folded over the left forearm, the right hand at his side.",
      "Facial expression: calm and polite, small smile.")

section('8 et 11 · Lost in the middle, context engineering')
for n, c in [('vide', 'empty'), ('sel', 'filled with coarse white salt'), ('paprika', 'filled with bright red paprika powder'),
             ('herbes', 'filled with chopped green herbs'), ('sucre', 'filled with white sugar')]:
    asset(f'ramequin-{n}.png', f'Ramequin · {n}', '1:1', '60 %', '80 px de large', f"One small round white ceramic ramekin, {c}.")
asset('ardoise.png', 'Ardoise', '3:2', '90 % de la largeur', '420 px de large',
      "A small blackboard slate with a light wood #D9A66B frame, completely blank and clean, standing slightly tilted.")

section('9 et 10 · Embeddings et RAG')
BOCAUX = [('pate-sablee', 'crumbly golden beige shortcrust dough'), ('creme-amande', 'pale yellow almond cream'),
          ('poires-pochees', 'dark red wine-poached pear halves'), ('fond-brun', 'a dark brown glossy stock'),
          ('vinaigrette', 'a golden oil and mustard vinaigrette'), ('veloute-potiron', 'a smooth orange pumpkin soup'),
          ('beurre-blanc', 'a pale creamy butter sauce'), ('coulis-framboise', 'a deep red raspberry coulis')]
for n, c in BOCAUX:
    asset(f'bocal-{n}.png', f'Bocal rempli · {n}', '1:1', '70 % de la hauteur', '110 px de large',
          f"Exactly the same round glass jar as in the reference (tomato red #D8432B clay lid, blank strip of white masking tape across the front, nothing written), filled with {c}.")
asset('louche.png', 'Louche', '3:2', '80 % de la largeur', '200 px de large', "A brushed steel ladle. " + POSE_OBJET)
perso('commis-remplit.png', 'Commis · il remplit un bocal', 'commis',
      "Pose: holding a steel ladle in the right hand, tilted as if pouring, and an open glass jar (red lid removed) in the left hand.",
      "Facial expression: careful, eyes on the jar, tongue slightly out.")

# ── PLATS ──
section('12 · Appel d’outil')
asset('boite-oeufs.png', 'Boîte d’œufs', '3:2', '75 % de la largeur', '180 px de large',
      "An open cardboard egg carton in cream #F6EFE2 holding 12 brown eggs.")
perso('commis-presente.png', 'Commis · il présente', 'commis',
      "Pose: holding an open egg carton forward with both hands towards the viewer.",
      "Facial expression: proud big smile, eyes shining, eyebrows raised.")

section('14 · MCP')
asset('saladette-pleine.png', 'Saladette pleine', '3:2', '90 % de la largeur', '360 px de large',
      "Exactly the same refrigerated brushed steel prep counter as in the reference, now with a steel gastronorm pan inserted in EVERY opening on top, each filled with a colourful ingredient (green herbs, red sauce, yellow corn, white rice, orange carrots, black olives).")
asset('bain-marie-plein.png', 'Bain-marie plein', '3:2', '90 % de la largeur', '320 px de large',
      "Exactly the same brushed steel bain-marie as in the reference, now with two steel gastronorm pans inserted in its openings, one with tomato red sauce, one with golden corn, a little steam rising.")

section('15 · Trop d’outils')
asset('tiroir-bazar.png', 'Tiroir en vrac', '3:2', '90 % de la largeur', '420 px de large',
      "An open wooden kitchen drawer seen from above, overflowing with about 30 mixed utensils in total disorder (ladles, whisks, spatulas, tongs, graters, peelers, spoons, scissors, sieves), all tangled.")
for n, c in [('ecumoire', 'A flat round steel skimmer with holes and a long handle'), ('passoire', 'A round steel sieve with a handle'),
             ('spatule', 'A light wood spatula'), ('pince', 'A pair of steel kitchen tongs'), ('rape', 'A steel box grater'),
             ('econome', 'A vegetable peeler with a teal handle'), ('cuillere-bois', 'A long wooden spoon'), ('ciseaux', 'A pair of kitchen scissors with tomato red handles')]:
    asset(f'{n}.png', n.replace('-', ' ').capitalize(), '3:2', '80 % de la largeur', '170 px de large', c + '. ' + POSE_OBJET)

# ── DESSERTS ──
section('19 · Multi-agents')
perso('saucier-fouette.png', 'Saucier · il fouette', 'saucier',
      "Pose: holding a small saucepan in the left hand and whisking in it with the right hand.",
      "Facial expression: focused, eyebrows drawn together, small satisfied smile.")
perso('saucier-attend.png', 'Saucier · il attend', 'saucier', "Pose: standing, hands on hips.", "Facial expression: friendly confident grin.")
section('Toujours manquants depuis le pack n° 1')
perso('chef-content.png', 'Chef · content', 'chef', "Pose: standing, one thumb up, the other hand on his belly.",
      "Facial expression: big happy smile with eyes closed, cheeks raised, proud.")
perso('chef-panique.png', 'Chef · débordé', 'chef', "Pose: both arms up in panic, toque slightly crooked, small sweat drops flying.",
      "Facial expression: eyes wide open, mouth open in an O, eyebrows high.")

# ── CAFÉ ET ADDITION ──
section('23 · Coût et délai')
asset('addition.png', 'Addition', '2:3', '80 % de la hauteur', '260 px de haut',
      "A long white paper restaurant receipt, slightly curled at the bottom, with faint grey lines but nothing written.")
asset('pieces.png', 'Pièces', '1:1', '55 %', '90 px de large', "A small pile of gold coins, plain, no symbols.")
asset('sablier.png', 'Sablier', '2:3', '70 % de la hauteur', '160 px de haut', "An hourglass with a light wood frame and mustard yellow sand, half run through.")
section('24 et 25 · Injection, données confidentielles')
asset('carnet-secret.png', 'Carnet secret', '1:1', '65 %', '150 px de large',
      "A thick notebook with a dark ink #2A2A2E leather cover, closed with a strap and a small brass padlock.")
asset('coffre.png', 'Coffre', '1:1', '65 %', '160 px de large', "A small brushed steel safe with a round dial, door closed.")

# ── écriture ──
tous = [a for _, l in SECTIONS for a in l]
L = ["# Pack d'images n° 2 · La cuisine (storyboard)", "",
     f"**{len(tous)} images, une par asset**, rangées dans l'ordre des chapitres du storyboard (`STORYBOARD.md`).", "",
     "## Mode d'emploi", "",
     "1. **Joins toujours en référence** le plan de travail et un objet du même type déjà réussi (pour les bocaux : `bocal.png` ; pour les poêles : `poele.png` ; pour un personnage existant : une de ses poses). Ajoute : « Keep exactly the same clay style, lighting, camera angle and character design as the reference images. »",
     "2. **Nouveaux personnages** (serveur, patronne, critique, pâtissière, saucier) : génère d'abord UNE pose, puis joins-la en référence pour ses autres poses.",
     "3. **Les poses ne contiennent que ce que le personnage tient en main** : jamais de planche, de table ni de nourriture devant lui (elles existent déjà dans la scène).",
     "4. Fond transparent (ou blanc pur #FFFFFF). Génère au double si possible.",
     "5. Dépose dans `sources/brut/` avec **exactement** le nom indiqué, puis lance `python outils/images/preparer_images.py` (détourage, mise à l'échelle, tailles.js).",
     "| Format | Pixels | Pour quoi |", "|---|---|---|",
     "| 1:1 | 1024 × 1024 | objets compacts |", "| 3:2 | 1536 × 1024 | objets longs |",
     "| 3:1 | 1536 × 512 | objets très longs (carottes, grand tronçon) |", "| 2:3 | 1024 × 1536 | tout ce qui est debout, personnages |", "",
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
out = os.path.join(os.path.dirname(__file__), '..', '..', 'docs', 'prompts', 'pack-2.md')
with open(out, 'w', encoding='utf-8') as fh: fh.write('\n'.join(L))
print(len(tous), 'images ->', os.path.abspath(out))
