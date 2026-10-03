# Audit UX de tous les chapitres « cuisine » à une taille de fenêtre : lance outils/audit-tout.html dans Chrome sans fenêtre
# et imprime, étape par étape, ce qui est caché ou se chevauche, et les textes trop petits (< 14 px à l'écran).
# Usage (serveur lancé à la racine du dépôt) : python outils/controle/audit.py 1280x720 [rag,token]
import html, io, json, os, re, subprocess, sys, tempfile

CHROME = os.environ.get('CHROME', r'C:\Program Files\Google\Chrome\Application\chrome.exe')   # ou la variable d'environnement CHROME
PROFIL = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sortie', '_profil-audit')
taille = sys.argv[1] if len(sys.argv) > 1 else '1280x720'
chap = ('&c=' + sys.argv[2]) if len(sys.argv) > 2 else ''
r = subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--disk-cache-size=1', f'--user-data-dir={PROFIL}', '--virtual-time-budget=120000',
                    '--dump-dom', f'http://localhost:4740/outils/controle/audit-tout.html?t={taille}{chap}'], capture_output=True)
m = re.search(r'<pre id="sortie">(.*?)</pre>', r.stdout.decode('utf-8', 'replace'), re.S)
data = json.loads(html.unescape(m.group(1)))
json.dump(data, io.open(os.path.join(os.path.dirname(PROFIL), f'audit-{taille}.json'), 'w', encoding='utf-8'), ensure_ascii=False)
n = 0
for c, etapes in data.items():
    for e in etapes:
        petit = [f"étiquettes {e['minEtiq']} px"] if e['minEtiq'] and e['minEtiq'] < 14 else []
        if e['encart'] and e['encart'] < 13: petit.append(f"encart {e['encart']} px")
        if e['pb'] or petit:
            n += 1
            print(f"{c} {e['k']} (zoom {e['zoom']}) : " + ' | '.join(e['pb'] + petit))
print(f'{n} étapes à revoir sur {sum(len(v) for v in data.values())}')
