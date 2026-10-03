// Audit UX des chapitres « cuisine » (mise en page roman visuel) : pour chaque étape, mesure à l'écran
// 1. ce qui est caché : un objet ou une étiquette sous l'encart (la fiche à droite), sous la boîte de dialogue, sous la marque, hors écran ;
// 2. les étiquettes qui se chevauchent entre elles ;
// 3. la taille réelle des textes : étiquettes du monde (taille × zoom de la caméra) et texte de l'encart (taille × zoom de la fiche).
// Usage (dans la page d'un chapitre) : const m = await import('/outils/controle/audit-ux.js'); await m.audit()
const aire = (a, b) => Math.max(0, Math.min(a[2], b[2]) - Math.max(a[0], b[0])) * Math.max(0, Math.min(a[3], b[3]) - Math.max(a[1], b[1]));
const boite = r => [r.left, r.top, r.right, r.bottom];
const surf = b => Math.max(1, (b[2] - b[0]) * (b[3] - b[1]));
const visible = el => { for (let e = el; e && e.id !== 'scene'; e = e.parentElement) { const c = getComputedStyle(e); if (c.opacity === '0' || c.display === 'none' || e.classList.contains('cache')) return false; } return true; };
const petitTexte = el => { let min = 99; el.querySelectorAll('*').forEach(x => { if ([...x.childNodes].some(n => n.nodeType === 3 && n.textContent.trim())) min = Math.min(min, parseFloat(getComputedStyle(x).fontSize)); }); return min; };

function mesurer() {
  const scene = Cuisine.scene, zoom = new DOMMatrix(getComputedStyle(scene).transform).a, vw = innerWidth, vh = innerHeight;
  const ui = [];
  const dock = document.getElementById('dock'); if (!dock.classList.contains('cache')) ui.push({ nom: 'la boîte', b: boite(dock.getBoundingClientRect()) });
  const portrait = dock.querySelector('.portrait'); if (getComputedStyle(portrait).display !== 'none') ui.push({ nom: 'le portrait', b: boite(portrait.getBoundingClientRect()) });
  const preuve = document.getElementById('preuve'), fiche = [...preuve.querySelectorAll('.fiche')].find(f => !f.classList.contains('cache'));
  if (!preuve.classList.contains('cache') && fiche) ui.push({ nom: 'l’encart', b: boite(fiche.getBoundingClientRect()) });
  document.querySelectorAll('#marque > *').forEach(e => ui.push({ nom: 'la marque', b: boite(e.getBoundingClientRect()) }));
  const objets = [], etiquettes = [];
  for (const el of scene.children) {
    if (!el.classList.contains('o') || !visible(el) || !el._pos) continue;
    const img = el.querySelector('img');
    if (img) {
      const r = img.getBoundingClientRect(), src = img.getAttribute('src').split('/').pop().replace('.png', ''), B = (window.BOITES || {})[src] || [0, 1, 0, 1];
      objets.push({ id: el.id, b: [r.left + B[0] * r.width, r.top + B[2] * r.height, r.left + B[1] * r.width, r.top + B[3] * r.height] });
    }
    el.querySelectorAll('.etiq, .score').forEach(t => { if (visible(t) && t.textContent.trim()) etiquettes.push({ id: el.id, de: el.id, b: boite(t.getBoundingClientRect()), px: parseFloat(getComputedStyle(t).fontSize) * zoom * (el._pos.s || 1) }); });
  }
  // les bons et fiches restés dans le monde (bons de commande, consignes au mur)
  for (const el of scene.children) if (!el.classList.contains('o') && !el.dataset.sur && visible(el) && el._pos && el.textContent.trim()) etiquettes.push({ id: el.className.split(' ')[0], b: boite(el.getBoundingClientRect()), px: petitTexte(el) * zoom });
  const pb = [];
  for (const o of objets) {
    for (const x of ui) { const p = aire(o.b, x.b) / surf(o.b); if (p > .1) pb.push(`${o.id} caché à ${Math.round(p * 100)} % par ${x.nom}`); }
    if (o.b[2] < 0 || o.b[0] > vw || o.b[3] < 0 || o.b[1] > vh) continue;
    const dehors = 1 - aire(o.b, [0, 0, vw, vh]) / surf(o.b); if (dehors > .15) pb.push(`${o.id} coupé par le bord (${Math.round(dehors * 100)} %)`);
  }
  for (const t of etiquettes) for (const x of ui) if (aire(t.b, x.b) > 30) pb.push(`texte de ${t.id} sous ${x.nom}`);
  // un papier volant (bon, consigne, contrat) posé sur un objet : il doit être dans un espace libre (sauf s'il est posé là exprès : data-sur)
  for (const t of etiquettes) for (const o of objets) {
    if (t.de) continue;
    const p = aire(t.b, o.b) / surf(t.b); if (p > .3) pb.push(`texte de ${t.id} posé sur ${o.id} (${Math.round(p * 100)} %)`);
  }
  for (let i = 0; i < etiquettes.length; i++) for (let j = i + 1; j < etiquettes.length; j++)
    if (aire(etiquettes[i].b, etiquettes[j].b) > .25 * Math.min(surf(etiquettes[i].b), surf(etiquettes[j].b))) pb.push(`textes de ${etiquettes[i].id} et ${etiquettes[j].id} se chevauchent`);
  const tailles = etiquettes.map(t => t.px);
  const encart = fiche ? petitTexte(fiche) * (parseFloat(fiche.style.zoom) || 1) : null;
  return { zoom: +zoom.toFixed(2), pb: [...new Set(pb)], minEtiq: tailles.length ? +Math.min(...tailles).toFixed(1) : null, encart: encart && +encart.toFixed(1) };
}

export async function audit() {
  if (!document.getElementById('sans-anim')) { const st = document.createElement('style'); st.id = 'sans-anim'; st.textContent = '*,*::before,*::after{transition:none!important;animation:none!important}'; document.head.appendChild(st); }
  const n = document.querySelectorAll('#dock .prog button').length - 1, out = [];
  for (let k = 0; k < n; k++) {
    Cuisine.aller(k);
    await new Promise(r => setTimeout(r, 40));   // pas de requestAnimationFrame : gelé si l'onglet est caché
    out.push({ k, ...mesurer() });
  }
  return out;
}
