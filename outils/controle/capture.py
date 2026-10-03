# Captures de contrôle des chapitres « cuisine » à une VRAIE taille de fenêtre.
# Le Chrome sans fenêtre met la page en page à 1264 × 625 puis la redimensionne à la taille demandée juste avant la capture :
# la caméra « saute » au redimensionnement (moteur.js), donc la capture est juste à la taille demandée.
# Usage (serveur lancé à la racine du dépôt) :
#   python outils/controle/capture.py 1280x720 outils/controle/sortie/captures rag:9 token:8
#   « rag:9 » = étapes 0 à 8 + titre + récapitulatif ; « rag:1.0,1.2 » = ces lignes précises (étape.ligne)
import os, subprocess, sys, urllib.request
from PIL import Image

CHROME = os.environ.get('CHROME', r'C:\Program Files\Google\Chrome\Application\chrome.exe')   # ou la variable d'environnement CHROME
BASE = 'http://localhost:4740/site/chapitres/'   # serveur lancé à la racine du dépôt
PROFIL = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sortie', '_profil-chrome')

def capture(url, w, h, fichier, essais=4):
    # Chrome sans fenêtre rend parfois un fichier vide ou tronqué : on vérifie l'image et on recommence
    for _ in range(essais):
        fichier = os.path.abspath(fichier)
        if os.path.exists(fichier): os.remove(fichier)
        # profil Chrome sur D: (le disque C: est plein)
        subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--hide-scrollbars', f'--window-size={w},{h}', f'--user-data-dir={PROFIL}', '--disk-cache-size=1',
                        '--virtual-time-budget=6000', f'--screenshot={fichier}', url], capture_output=True)
        try:
            with Image.open(fichier) as im: im.load(); return
        except Exception:
            pass
    raise RuntimeError('capture impossible : ' + url)

def serveur_ok():
    try: urllib.request.urlopen(BASE + '../index.html', timeout=3); return True
    except Exception: return False

if __name__ == '__main__':
    if not serveur_ok(): sys.exit('Le serveur local (port 4740) ne répond pas : lancer « python -m http.server 4740 » à la racine du dépôt.')
    w, h = map(int, sys.argv[1].split('x'))
    out = sys.argv[2]; os.makedirs(out, exist_ok=True)
    for arg in sys.argv[3:]:
        page, n = arg.split(':')
        # « page?mise=colonne » : même page avec un paramètre ; le fichier prend le suffixe de sa valeur (page-colonne-3.png)
        nom, _, q = page.partition('?')
        suffixe = ('-' + q.split('=')[-1]) if q else ''
        # « :5 » = les étapes 0 à 4 (+ titre et fin) ; « :1.0,1.1,3.2 » = exactement ces cibles (étape.ligne)
        cibles = n.split(',') if (',' in n or '.' in n) else [str(i) for i in range(int(n))] + ['titre', 'fin']
        for c in cibles:
            url = BASE + nom + '.html' + ('?' + q if q else '') + ('' if c == 'titre' else '#' + c)
            capture(url, w, h, os.path.join(out, f'{nom}{suffixe}-{c}.png'))
    print('ok')
