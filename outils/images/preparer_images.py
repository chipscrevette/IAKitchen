# Images de la cuisine : sources/brut/ → site/images/ (fond retiré, recadré au contenu, 900 px au plus),
# le décor (plan de travail, et sa version prolongée par symétrie pour la caméra), puis site/donnees/tailles.js
# et une planche de contrôle.
#
#   python outils/images/preparer_images.py                  tout refaire
#   python outils/images/preparer_images.py --tailles        ne regénérer que tailles.js
#   python outils/images/preparer_images.py planche.png chef-attend,commis-lit   planche de contrôle de quelques images
#
# Le fond blanc éventuel n'est retiré que s'il touche les bords (remplissage depuis les bords), pour ne pas trouer
# les objets blancs (ticket, assiettes, veste).
import json, os, sys
import numpy as np
from PIL import Image, ImageDraw
from scipy import ndimage as nd

RACINE = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', '..'))
BRUT = os.path.join(RACINE, 'sources', 'brut')
IMAGES = os.path.join(RACINE, 'site', 'images')
DECOR = os.path.join(IMAGES, 'decor')
TAILLES = os.path.join(RACINE, 'site', 'donnees', 'tailles.js')
os.makedirs(DECOR, exist_ok=True)

# le monde fait 1900 × 1069 ; le décor est prolongé à droite et en bas pour que la caméra puisse reculer (moteur.css)
MONDE, PROLONGE = 1900, (1000, 450)

def detourer(im):
    a = np.array(im.convert('RGBA'))
    alpha = a[:, :, 3]
    if (alpha < 20).mean() > 0.05:            # déjà transparent
        return Image.fromarray(a), 'alpha'
    rgb = a[:, :, :3].astype(int)
    blanc = (rgb.min(axis=2) > 236) & (np.ptp(rgb, axis=2) < 14)
    lab, _ = nd.label(blanc)
    bords = set(np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))) - {0}
    fond = np.isin(lab, list(bords))
    fond = nd.binary_dilation(fond, iterations=1) & blanc | fond
    a[:, :, 3] = np.where(fond, 0, 255)
    return Image.fromarray(a), 'blanc retiré'

def decor(im):
    plan = im.convert('RGB').resize((MONDE, round(im.height * MONDE / im.width)), Image.LANCZOS)
    plan.save(os.path.join(DECOR, 'plan-de-travail.jpg'), quality=90)
    large = np.pad(np.array(plan), ((0, PROLONGE[1]), (0, PROLONGE[0]), (0, 0)), mode='symmetric')
    Image.fromarray(large).save(os.path.join(DECOR, 'plan-de-travail-large.jpg'), quality=84, optimize=True, progressive=True)

def traiter(nom):
    im = Image.open(os.path.join(BRUT, nom))
    if nom.startswith('plan-de-travail'):
        decor(im)
        return 'décor'
    im, mode = detourer(im)
    bb = im.getbbox()
    if bb:
        p = 6
        im = im.crop((max(0, bb[0] - p), max(0, bb[1] - p), min(im.width, bb[2] + p), min(im.height, bb[3] + p)))
    if max(im.size) > 900:
        k = 900 / max(im.size); im = im.resize((round(im.width * k), round(im.height * k)), Image.LANCZOS)
    im.save(os.path.join(IMAGES, os.path.splitext(nom)[0] + '.png'), optimize=True)
    return f'{mode} {im.size}'

def tailles():
    # taille réelle de chaque image et sa silhouette visible (alpha > 60), pour poser les objets par leur base ;
    # pour les personnages, le centre de la tête (bande 5–25 % de la silhouette), pour cadrer leur portrait
    T, B, TETES = {}, {}, {}
    PERSOS = ('chef-', 'commis-', 'serveur-', 'patronne-', 'critique-', 'patissiere-', 'saucier-')
    for f in sorted(os.listdir(IMAGES)):
        if not f.endswith('.png'): continue
        a = np.array(Image.open(os.path.join(IMAGES, f)).convert('RGBA'))[:, :, 3] > 60
        H, W = a.shape; ys, xs = np.where(a); n = f[:-4]
        T[n] = [W, H]
        B[n] = [round(float(xs.min()) / W, 3), round(float(xs.max() + 1) / W, 3), round(float(ys.min()) / H, 3), round(float(ys.max() + 1) / H, 3)]
        if n.startswith(PERSOS):
            y0, y1 = ys.min(), ys.max() + 1; hs = y1 - y0
            by, bx = np.where(a[int(y0 + .05 * hs):int(y0 + .25 * hs)])
            TETES[n] = round(float(bx.mean()) / W, 3)
    with open(TAILLES, 'w', encoding='utf-8') as fh:
        fh.write('// généré par outils/images/preparer_images.py : taille réelle de chaque image ([largeur, hauteur]), silhouette visible\n'
                 '// (fractions x0, x1, y0, y1) et, pour les personnages, le centre horizontal de la tête (fraction de la largeur)\n'
                 'window.TAILLES = ' + json.dumps(T) + ';\nwindow.BOITES = ' + json.dumps(B) + ';\nwindow.TETES = ' + json.dumps(TETES) + ';\n')
    print(len(T), 'images dans tailles.js')

def planche(sortie, seuls=None):
    # damier derrière chaque image, pour voir les restes de fond
    fichiers = sorted(f for f in os.listdir(IMAGES) if f.endswith('.png') and (not seuls or f[:-4] in seuls)); c = 200; cols = 8
    rows = (len(fichiers) + cols - 1) // cols
    sheet = Image.new('RGB', (cols * c, rows * (c + 18)), 'white'); d = ImageDraw.Draw(sheet)
    for i, f in enumerate(fichiers):
        x, y = (i % cols) * c, (i // cols) * (c + 18)
        for yy in range(0, c, 16):
            for xx in range(0, c, 16):
                if (xx // 16 + yy // 16) % 2: d.rectangle([x + xx, y + yy, x + xx + 15, y + yy + 15], fill=(210, 210, 210))
        im = Image.open(os.path.join(IMAGES, f)); im.thumbnail((c - 8, c - 8))
        sheet.paste(im, (x + (c - im.width) // 2, y + (c - im.height) // 2), im)
        d.text((x + 4, y + c + 2), f[:-4][:24], fill='black')
    sheet.save(sortie)
    print(len(fichiers), 'images sur la planche', sortie)

if __name__ == '__main__':
    if '--tailles' in sys.argv:
        tailles(); sys.exit()
    for n in sorted(f for f in os.listdir(BRUT) if f.lower().endswith(('.png', '.webp', '.jpg'))):
        print(n, traiter(n))
    tailles()
    planche(sys.argv[1] if len(sys.argv) > 1 else os.path.join(RACINE, 'sources', 'controle.png'), set(sys.argv[2].split(',')) if len(sys.argv) > 2 else None)
