// La cuisine de l'IA · le moteur commun des chapitres.
// Un chapitre crée ses objets (Cuisine.objet), puis appelle Cuisine.lancer({ ... }) avec ses étapes et sa fonction monde(k)
// qui pose chaque objet pour l'étape k. Le moteur gère la caméra, la boîte de dialogue, l'écran de titre, le récapitulatif,
// le clavier, le lien #n (#n.l : la ligne l de l'étape n ; #fin : le récapitulatif) et la mémoire « chapitre vu ».
//
// Façon roman visuel : la scène au centre ; en bas, une boîte de dialogue qui déroule chaque étape phrase par phrase avec
// « Suivant ». Une étape = { nom, t, lignes, v } :
//   t      : le récit (facultatif), sans visage ;
//   lignes : [{ qui: 'chef', dit: '« … »', pose: 'chef-panique', tampon: 'RATÉ' | { txt, vert: true } }, { dit: 'récit' }, …]
//            « qui » est l'id d'un objet du chapitre ; sans « qui », la ligne est du récit ;
//   v      : « En vrai », le sens technique, toujours en dernier.
// Celui qui parle a son portrait dans la boîte (sa pose, cadrée sur la tête), un repère au-dessus de la tête dans la scène,
// et il réagit (petit saut) ; un personnage qui change de place marche ; un objet qui apparaît « pop ».
// La fiche de l'étape (élément .fiche visible) s'affiche en encart à droite pendant toute l'étape ; la caméra cadre la scène
// dans l'espace qui reste. Les noms des personnages se changent par chapitre : lancer({ noms: { commis: 'L’apprenti' } }).
window.Cuisine = (() => {
  const A = n => `../images/${n}.png`;   // chemins relatifs à la page d'un chapitre (site/chapitres/)
  const fr = (v, d = 2) => v.toFixed(d).replace('.', ',').replace('-', '−');
  const pct = (p, d = 0) => (p * 100).toFixed(d).replace('.', ',') + ' %';
  const O = {};
  let scene, dock, ecran, prog, suiv, prec, preuve, CFG, RECAP, cur = -1, LIGNES = [], ligne = 0;
  const NOMS = { chef: 'Le chef', commis: 'Le commis', serveur: 'Le serveur', patronne: 'La patronne', critique: 'Le critique', patissiere: 'La pâtissière', saucier: 'Le saucier' };
  const nomImage = src => (src || '').split('/').pop().replace('.png', '');
  const famille = src => nomImage(src).split('-')[0];

  function construire(cfg) {
    document.body.insertAdjacentHTML('afterbegin', `
      <div id="scene"></div>
      <header id="marque"><a class="logo" href="../index.html">La cuisine de l’IA</a><span class="chap"><b>${cfg.notion}</b> · ${cfg.titre}</span></header>
      <div id="preuve" class="cache"></div>
      <section id="dock" class="cache" aria-live="polite">
        <div class="prog"></div>
        <div class="corps">
          <div class="portrait"><div class="coupe"><img alt=""></div></div>
          <div class="texte"><p class="meta"><span class="qui"></span><span class="num"></span><span class="nom"></span></p><p class="phrase"></p></div>
          <div class="nav"><button class="prec" aria-label="Retour">←</button><button class="suiv">Suivant <span>→</span></button></div>
        </div>
        <span class="tampon-boite"></span>
      </section>
      <div id="ecran"></div>`);
    scene = document.getElementById('scene'); dock = document.getElementById('dock'); ecran = document.getElementById('ecran'); preuve = document.getElementById('preuve');
    prog = dock.querySelector('.prog'); suiv = dock.querySelector('.suiv'); prec = dock.querySelector('.prec');
  }

  // ── les objets du monde ──
  function objet(id, src, w, extra = '') {
    const d = document.createElement('div'); d.className = 'o'; d.id = id; d.style.width = w + 'px';
    d.innerHTML = (src ? `<img src="${A(src)}" alt="">` : '') + extra;
    scene.appendChild(d);
    return O[id] = d;
  }
  function element(cls, html = '') {
    const d = document.createElement('div'); d.className = cls + ' cache'; d.innerHTML = html; scene.appendChild(d); return d;
  }
  // relance une animation CSS (la classe est retirée, le navigateur « oublie », on la remet)
  const rejouer = (el, cls, duree) => { el.classList.remove(cls); void el.offsetWidth; el.classList.add(cls); clearTimeout(el['_t' + cls]); el['_t' + cls] = setTimeout(() => el.classList.remove(cls), duree); };
  let anime = false;   // pas d'animation d'entrée au premier affichage ni quand on saute d'étape en étape par la barre
  function poser(id, x, y, s = 1, vis = true, delai = 0, rot = 0) {
    const o = O[id], avant = o._pos, etaitVisible = avant && !o.classList.contains('cache');
    o.style.transitionDelay = delai + 's'; o._pos = { x, y, s }; o.style.setProperty('--os', s);
    o.style.transform = `translate(${x}px, ${y}px) scale(${s})` + (rot ? ` rotate(${rot}deg)` : '');
    o.classList.toggle('cache', !vis);
    if (!anime || !vis) return;
    if (!etaitVisible) rejouer(o, 'apparait', 450);                                                       // il arrive : pop
    else if (estPerso(o) && Math.hypot(x - avant.x, y - avant.y) > 40) rejouer(o, 'marche', 1000);         // il se déplace : il marche
  }
  // change l'image d'un objet en gardant une HAUTEUR fixe (les poses d'un personnage n'ont pas la même largeur)
  function image(id, src, haut) {
    const i = O[id].querySelector('img'); if (i.getAttribute('src') !== A(src)) i.setAttribute('src', A(src));
    const t = window.TAILLES && TAILLES[src];
    if (t && haut) O[id].style.width = Math.round(t[0] / t[1] * haut) + 'px';
  }
  function placer(el, x, y, vis = true, rot = 0, extra = '') {
    el._pos = { x, y, s: 1 };
    el.style.transform = `translate(${x}px, ${y}px)` + (rot ? ` rotate(${rot}deg)` : '') + extra;
    el.classList.toggle('cache', !vis);
  }

  // ── géométrie du monde ──
  // silhouette visible d'un objet (sans les marges transparentes de son image) ; hauteur tirée de tailles.js
  // (au premier rendu, l'image n'est pas encore chargée : sa hauteur affichée vaut 0)
  function silhouette(el) {
    const p = el._pos, img = el.querySelector('img'), w = el.offsetWidth * p.s;
    if (!img) return [p.x, p.y, p.x + w, p.y + el.offsetHeight * p.s];
    const src = nomImage(img.getAttribute('src')), B = (window.BOITES || {})[src] || [0, 1, 0, 1], T = (window.TAILLES || {})[src];
    const ih = T ? w * T[1] / T[0] : img.offsetHeight * p.s;
    return [p.x + B[0] * w, p.y + B[2] * ih, p.x + B[1] * w, p.y + B[3] * ih];
  }
  const vu = el => el._pos && !el.classList.contains('cache') && getComputedStyle(el).display !== 'none';
  const boiteTexte = el => { const p = el._pos; return [p.x, p.y - (el.querySelector('.tampon') ? 80 : 0), p.x + el.offsetWidth, p.y + el.offsetHeight]; };
  // un personnage = un objet dont l'image s'appelle chef-…, commis-…, serveur-…
  const estPerso = e => { const i = e.classList && e.classList.contains('o') && e.querySelector('img'); return !!(i && NOMS[famille(i.getAttribute('src'))]); };
  // cadrage : tout ce qui est visible dans le monde, avec une marge ; au moins 950 × 520 du monde
  function cadreAuto() {
    let u = null;
    for (const el of scene.children) {
      if (!vu(el)) continue;
      const b = el.classList.contains('o') ? silhouette(el) : boiteTexte(el);
      if (el.querySelector('.etiq')) b[3] += 40;
      u = u ? [Math.min(u[0], b[0]), Math.min(u[1], b[1]), Math.max(u[2], b[2]), Math.max(u[3], b[3])] : b;
    }
    if (!u) return [0, 0, 1900, 1069];
    const p = 50; u = [u[0] - p, u[1] - p, u[2] + p, u[3] + p];
    const w = Math.max(950, u[2] - u[0]), h = Math.max(520, u[3] - u[1]), cx = (u[0] + u[2]) / 2, cy = (u[1] + u[3]) / 2;
    return [cx - w / 2, cy - h / 2, w, h];
  }

  // ── la caméra : cadre le rectangle utile dans l'espace libre (entre la marque et la boîte de dialogue) ──
  let cadre = null;
  function camera(r) {
    if (r) cadre = r; r = cadre;
    const vw = innerWidth, vh = innerHeight;
    if (!vw || !vh || !r) return;                       // fenêtre pas encore dimensionnée : on réessaiera au redimensionnement
    const m = parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--marge')) || 24;
    const haut = document.getElementById('marque').getBoundingClientRect().bottom + m * .6;
    const bas = dock.classList.contains('cache') ? m : vh - dock.getBoundingClientRect().top + m * 1.2;   // le portrait déborde au-dessus : compris
    const droite = preuve.classList.contains('cache') ? m : vw - preuve.getBoundingClientRect().left + m;   // l'encart à droite
    const aw = vw - m - droite, ah = Math.max(80, vh - haut - bas);
    const couvre = Math.max(vw / 1900, vh / 1069);
    // cadrer r ; puis, si un objet visible est coupé par le bord (ou passe sous la marque / la boîte), agrandir r pour l'inclure entier
    const cadrer = r => {
      // la caméra peut reculer au-delà du bord du monde (le fond est prolongé à droite et en bas, moteur.css),
      // jamais au point de découvrir le bord du fond prolongé, ni sous ×0,3
      let s = Math.min(aw / r[2], ah / r[3], 1.35); s = Math.max(s, Math.min(couvre, Math.max(.3, vw / 2900, vh / 1519)));
      let tx = m + aw / 2 - (r[0] + r[2] / 2) * s, ty = haut + ah / 2 - (r[1] + r[3] / 2) * s;
      tx = Math.min(0, Math.max(vw - 2900 * s, tx)); ty = Math.min(0, Math.max(vh - 1519 * s, ty));   // fond prolongé (moteur.css)
      return { s, tx, ty };
    };
    let { s, tx, ty } = cadrer(r);
    for (let passe = 0; passe < 6; passe++) {
      const V = [-tx / s, (haut - ty) / s, (vw - droite - tx) / s, (vh - bas - ty) / s];
      let r2 = null;
      for (const el of scene.children) {
        if (!vu(el)) continue;
        const p = el._pos, w = el.offsetWidth * p.s, h = (el.offsetHeight + (el.querySelector('.etiq') ? 34 : 0)) * p.s;
        const b = [p.x, p.y, p.x + w, p.y + h], tol = .06;
        if (b[2] < V[0] || b[0] > V[2] || b[3] < V[1] || b[1] > V[3]) continue;          // hors champ : rien à faire
        const dedans = b[0] >= V[0] - tol * w && b[2] <= V[2] + tol * w && b[1] >= V[1] - tol * h && b[3] <= V[3] + tol * h;
        if (dedans) continue;
        const u = r2 || [r[0], r[1], r[0] + r[2], r[1] + r[3]];
        r2 = [Math.max(0, Math.min(u[0], b[0] - 10)), Math.max(0, Math.min(u[1], b[1] - 10)), Math.min(1900, Math.max(u[2], b[2] + 10)), Math.min(1069, Math.max(u[3], b[3] + 10))];
      }
      if (!r2) break;
      r = [r2[0], r2[1], r2[2] - r2[0], r2[3] - r2[1]];
      ({ s, tx, ty } = cadrer(r));
    }
    scene.style.transform = `translate(${tx}px, ${ty}px) scale(${s})`;
    scene.style.setProperty('--z', s.toFixed(3));                                        // les étiquettes restent lisibles quel que soit le zoom
    document.documentElement.style.setProperty('--hdock', (vh - dock.getBoundingClientRect().top) + 'px');   // la preuve s'arrête au-dessus de la boîte
  }

  // ── écrans ──
  const vignette = n => `<div class="vignette"><img src="${A(n)}" alt=""></div>`;
  function ecranTitre() {
    ecran.innerHTML = `<div class="carte"><p class="k">Notion · ${CFG.notion}</p><h1>${CFG.titre}</h1>
      <p class="chapeau">${CFG.chapeau}</p>
      <div class="pied"><span class="info">${CFG.etapes.length} étapes · ${CFG.duree || '2 minutes'}</span><div class="boutons"><a class="bouton vide" href="../index.html">La carte</a><button class="bouton plein" data-go="0">Commencer <span>→</span></button></div></div></div>`;
  }
  function ecranRecap() {
    const r = CFG.recap;
    ecran.innerHTML = `<div class="carte"><p class="k">À retenir</p><h1>${r.titre}</h1>
      <div class="trois">${r.trois.map(c => `<div>${vignette(c.img)}<p><b>${c.t}</b>${c.d}</p></div>`).join('')}</div>
      <p class="entretien"><b>En entretien, en 30 secondes :</b> ${r.entretien}</p>
      <div class="pied"><span class="info">${r.source || ''}</span><div class="boutons"><button class="bouton vide" data-go="0">Revoir</button>` +
      (CFG.suivant ? `<a class="bouton plein" href="${CFG.suivant.href}">${CFG.suivant.titre} <span>→</span></a>` : `<a class="bouton plein" href="../index.html">La carte <span>→</span></a>`) +
      `</div></div></div>`;
    try { const v = new Set(JSON.parse(localStorage.getItem('cuisine-vus') || '[]')); v.add(CFG.id); localStorage.setItem('cuisine-vus', JSON.stringify([...v])); } catch (e) {}
  }

  // ── la boîte de dialogue ──
  const tampon = t => t && (typeof t === 'string' ? { txt: t, vert: false } : t);
  // une réplique : qui (id d'un objet), pose (image du portrait et de la scène ; par défaut sa pose de l'étape), texte, tampon
  function replique(quiId, pose, html, t) {
    const qui = O[quiId] || null, src = pose || (qui && nomImage(qui.querySelector('img').getAttribute('src')));
    const noms = { ...NOMS, ...(CFG.noms || {}) };
    return { type: 'dit', html, qui, pose, src, nom: noms[famille(src)] || '', tampon: tampon(t) };
  }
  // les lignes d'une étape, dans l'ordre du script ; « En vrai » en dernier
  function lignesEtape(e) {
    const L = [];
    if (e.t) L.push({ type: 'recit', html: e.t });
    (e.lignes || []).forEach(l => L.push(l.qui ? replique(l.qui, l.pose, l.dit, l.tampon) : { type: 'recit', html: l.dit, tampon: tampon(l.tampon) }));
    L.push({ type: 'vrai', html: e.v });
    return L;
  }
  // le portrait : la tête du personnage déborde du cadre par le haut ; le cadre prend la couleur du personnage
  function cadrerPortrait(src) {
    const cadreEl = dock.querySelector('.portrait'), img = cadreEl.querySelector('img');
    const n = nomImage(src), T = (window.TAILLES || {})[n], B = (window.BOITES || {})[n], cx = (window.TETES || {})[n];
    if (img.getAttribute('src') !== A(n)) img.setAttribute('src', A(n));
    cadreEl.dataset.famille = famille(n);
    if (!T || !B) return;
    const F = cadreEl.offsetWidth, Fh = cadreEl.offsetHeight, hs = B[3] - B[2];
    // la bande « buste » = le haut de la silhouette sur 44 % de sa hauteur ; elle occupe le cadre + 16 % au-dessus
    const h = Fh * 1.16 / (.44 * hs), w = h * T[0] / T[1];
    img.style.height = h + 'px'; img.style.width = w + 'px';
    img.style.top = (-.16 * Fh - B[2] * h) + 'px';
    img.style.left = (F / 2 - (cx == null ? (B[0] + B[1]) / 2 : cx) * w) + 'px';
  }
  // pendant une réplique, le personnage prend la pose de la réplique dans la scène (et la quitte ensuite)
  function poses(L) {
    for (const p of scene.children) {
      if (!p._pied || !p._poseMonde) continue;
      const voulu = L.type !== 'vrai' && L.qui === p && L.pose ? L.pose : p._poseMonde;
      if (nomImage(p.querySelector('img').getAttribute('src')) !== voulu) {
        image(p.id, voulu, p._pied.haut);
        const vis = !p.classList.contains('cache'), a = anime; anime = false;
        poserSur(p.id, p._pied.cx, p._pied.pieds, 1, vis); anime = a;
      }
    }
  }
  // l'encart : la fiche de l'étape, à droite, à la plus grande taille qui tient (au plus 38 % de la largeur, ×0,8 à ×1,45)
  function encart() {
    const f = [...preuve.querySelectorAll('.fiche')].find(x => !x.classList.contains('cache'));
    preuve.classList.toggle('cache', !f);
    if (!f) { preuve.style.width = ''; return; }
    f.style.zoom = 1;
    const H = preuve.getBoundingClientRect().height, w = f.offsetWidth, h = f.offsetHeight;
    if (!w || !h || !H) return;
    const z = Math.max(.8, Math.min(1.45, .38 * innerWidth / w, (H - 20) / h));
    f.style.zoom = z.toFixed(3); preuve.style.width = Math.ceil(w * z) + 'px';
  }
  function montrerLigne(l) {
    ligne = l; const L = LIGNES[l], parle = !!(L.qui || L.src) && L.type !== 'vrai';
    dock.dataset.ligne = L.type;
    dock.classList.toggle('avec-portrait', parle);
    dock.querySelector('.qui').textContent = parle ? L.nom : L.type === 'vrai' ? 'En vrai' : '';
    if (parle) { cadrerPortrait(L.src); if (anime) rejouer(dock.querySelector('.portrait'), 'entre', 400); }
    dock.querySelector('.phrase').innerHTML = L.type === 'vrai' ? L.html.charAt(0).toUpperCase() + L.html.slice(1) : L.html;
    const tp = dock.querySelector('.tampon-boite');
    tp.textContent = L.tampon ? L.tampon.txt : ''; tp.classList.toggle('vert', !!(L.tampon && L.tampon.vert));
    if (L.tampon && anime) rejouer(tp, 'frappe', 400);
    // qui parle : sa pose, un repère au-dessus de sa tête, un petit saut
    poses(L);
    scene.querySelectorAll('.parle').forEach(x => x.classList.remove('parle'));
    if (parle && L.qui) {
      const B = (window.BOITES || {})[nomImage(L.qui.querySelector('img').getAttribute('src'))] || [0, 1, 0, 1];
      L.qui.style.setProperty('--tete', (B[2] * 100).toFixed(1) + '%'); L.qui.classList.add('parle');
      if (anime) rejouer(L.qui, 'saute', 500);
    }
    if (window.espacesFr) espacesFr(dock);
    prec.disabled = cur === 0 && l === 0;
    suiv.firstChild.nodeValue = l === LIGNES.length - 1 && cur === CFG.etapes.length - 1 ? 'À retenir ' : 'Suivant ';
    [...prog.children].forEach((b, i) => b.style.setProperty('--avance', i === cur ? (l + 1) / LIGNES.length : 1));
  }

  function aller(k, finEtape) {
    cur = Math.max(-1, Math.min(RECAP, k));
    const surEcran = cur < 0 || cur === RECAP;
    if (cur < 0) ecranTitre(); if (cur === RECAP) ecranRecap();
    ecran.classList.toggle('cache', !surEcran);
    dock.classList.toggle('cache', surEcran);
    CFG.monde(Math.min(Math.max(cur, 0), CFG.etapes.length - 1), cur);
    // la pose que l'étape donne à chaque personnage (une réplique peut la changer le temps de la réplique)
    for (const p of scene.children) if (p._pied) p._poseMonde = nomImage(p.querySelector('img').getAttribute('src'));
    // typographie française partout : fiches, étiquettes, écrans
    if (window.espacesFr) { espacesFr(scene); espacesFr(preuve); espacesFr(ecran); }
    if (surEcran) {
      preuve.classList.add('cache');
      scene.querySelectorAll('.parle').forEach(x => x.classList.remove('parle'));
    } else {
      const e = CFG.etapes[cur];
      dock.querySelector('.num').textContent = String(cur + 1).padStart(2, '0') + ' / ' + String(CFG.etapes.length).padStart(2, '0');
      dock.querySelector('.nom').textContent = e.nom;
      LIGNES = lignesEtape(e);
      montrerLigne(finEtape ? LIGNES.length - 1 : 0);
      encart();
    }
    [...prog.children].forEach((b, i) => { b.classList.toggle('fait', i < cur); b.classList.toggle('ici', i === cur); });
    camera(surEcran ? (CFG.camTitre || [0, 0, 1900, 1069]) : cadreAuto());
  }

  function lancer(cfg) {
    CFG = cfg; RECAP = cfg.etapes.length;
    // les fiches de données quittent le monde : elles s'affichent en grand, au-dessus de la scène (on déplace l'élément : ses boutons restent actifs)
    scene.querySelectorAll('.fiche').forEach(f => preuve.appendChild(f));
    document.title = cfg.titre + ' · La cuisine de l’IA';
    prog.style.gridTemplateColumns = `repeat(${RECAP + 1}, 1fr)`;
    for (let i = 0; i <= RECAP; i++) { const b = document.createElement('button'); b.title = i < RECAP ? cfg.etapes[i].nom : 'À retenir'; b.onclick = () => { anime = false; aller(i); anime = true; }; prog.appendChild(b); }
    ecran.addEventListener('click', e => { const b = e.target.closest('[data-go]'); if (b) aller(+b.dataset.go); });
    // « Suivant » déroule les lignes de l'étape, puis passe à l'étape suivante ; « Retour » remonte ligne par ligne
    // un clic dans la scène fait avancer, comme dans un roman visuel (pas sur une fiche ou un bouton du chapitre)
    scene.addEventListener('click', e => { if (!e.target.closest('button, input, a, .fiche') && cur >= 0 && cur < RECAP) avancer(); });
    const avancer = () => { if (cur >= 0 && cur < RECAP && ligne < LIGNES.length - 1) montrerLigne(ligne + 1); else aller(cur + 1); };
    const reculer = () => { if (cur >= 0 && cur < RECAP && ligne > 0) montrerLigne(ligne - 1); else aller(cur - 1, true); };
    suiv.onclick = avancer;
    prec.onclick = reculer;
    document.addEventListener('keydown', e => {
      if (e.target.closest && e.target.closest('input')) return;
      if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'Enter') { e.preventDefault(); if (cur < RECAP) avancer(); }
      if (e.key === 'ArrowLeft') reculer();
    });
    // la caméra suit toute variation de taille (fenêtre, polices chargées qui changent la hauteur de la boîte)
    // si la FENÊTRE change de taille, la caméra saute (pas d'animation) ; sinon elle glisse
    let taille = innerWidth + 'x' + innerHeight;
    const recadrer = () => {
      const t = innerWidth + 'x' + innerHeight;
      if (t !== taille) { taille = t; scene.style.transition = 'none'; camera(); void scene.offsetWidth; scene.style.transition = ''; }
      else camera();
      if (cur >= 0 && cur < RECAP && dock.classList.contains('avec-portrait')) cadrerPortrait(LIGNES[ligne].src);
      if (cur >= 0 && cur < RECAP) encart();
    };
    addEventListener('resize', recadrer);
    if (window.ResizeObserver) { new ResizeObserver(recadrer).observe(document.documentElement); new ResizeObserver(recadrer).observe(dock); }
    if (document.fonts) document.fonts.ready.then(recadrer);
    // premier affichage sans animation ; #3 : l'étape 3 ; #3.2 : sa 3e ligne ; #fin : le récapitulatif
    scene.style.transition = 'none'; document.querySelectorAll('.o, .fiche').forEach(o => o.style.transition = 'none');
    const h = location.hash.slice(1), [hk, hl] = h.split('.');
    aller(h === 'fin' ? RECAP : h === '' ? -1 : +hk);
    if (hl && cur >= 0 && cur < RECAP) montrerLigne(Math.min(+hl, LIGNES.length - 1));
    void scene.offsetWidth;
    setTimeout(() => { scene.style.transition = ''; document.querySelectorAll('.o, .fiche').forEach(o => o.style.transition = ''); anime = true; }, 50);
  }

  // le fond utile d'un plateau (mesuré sur plateau.png : fond plat entre 8 % et 94 % de la largeur, 21 % et 47 % de la largeur en hauteur)
  const solPlateau = (x, y, w) => ({ x0: x + .08 * w, x1: x + .94 * w, y0: y + .214 * w, y1: y + .469 * w });
  // poser un objet par le milieu de sa base : l'image a ses marges, on les mesure (fractions de la boîte visible)
  const BOITES_BASE = { bocal: [.209, .779, .102, .907], de: [.211, .771, .223, .781] };
  function poserBase(id, type, largeur, cx, bas, s = 1, vis = true, delai = 0) {
    const [x0, x1, , y1] = BOITES_BASE[type], w = largeur * s, h = w * (type === 'bocal' ? 900 / 890 : 900 / 878);
    poser(id, cx - (x0 + x1) / 2 * w, bas - y1 * h, s, vis, delai);
  }
  // poser n'importe quel objet par le MILIEU DE SA BASE (silhouette mesurée dans tailles.js : BOITES)
  // largeur = largeur de l'image à l'échelle 1 (sinon celle déjà donnée à l'objet) ; s = échelle
  function poserSur(id, cx, bas, s = 1, vis = true, delai = 0) {
    const src = nomImage(O[id].querySelector('img').getAttribute('src'));
    const [x0, x1, , y1] = window.BOITES[src], [W, H] = TAILLES[src];
    const w = parseFloat(O[id].style.width) * s, h = w * H / W;
    poser(id, cx - (x0 + x1) / 2 * w, bas - y1 * h, s, vis, delai);
  }
  // un personnage : même hauteur pour toutes ses poses, posé par les pieds (on s'en souvient pour changer sa pose pendant une réplique)
  function perso(id, src, cx, pieds, vis = true, delai = 0) {
    const haut = src.startsWith('chef') ? 370 : 330;
    image(id, src, haut);
    O[id]._pied = { cx, pieds, haut };
    poserSur(id, cx, pieds, 1, vis, delai);
  }
  return { construire, objet, element, poser, poserBase, poserSur, perso, solPlateau, image, placer, lancer, aller, A, fr, pct, O, get scene() { return scene; },
    // pour les outils de contrôle (outils/controle/dump-lignes.html)
    get lignes() { return LIGNES.map(l => ({ type: l.type, qui: l.nom || '', pose: l.src || '', texte: l.html.replace(/<[^>]+>/g, ''), tampon: l.tampon ? l.tampon.txt : '' })); },
    get fiche() { const f = [...preuve.querySelectorAll('.fiche')].find(x => !x.classList.contains('cache')); return f ? f.textContent.replace(/\s+/g, ' ').trim() : ''; } };
})();
