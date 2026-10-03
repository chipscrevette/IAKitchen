// Vrais embeddings (multilingual-e5-small, 384 dimensions) pour la scène cuisine : fiches + question.
import { pipeline } from '@huggingface/transformers';
import fs from 'fs';

const FICHES = [
  'Pâte sablée pour la tarte de la maison : farine, beurre demi-sel, sucre, un jaune d’œuf.',
  'Crème d’amande de la grand-mère : beurre, sucre, poudre d’amande, œufs, un trait de rhum.',
  'Poires pochées au vin rouge et à la cannelle, pour la tarte de la maison.',
  'Fond brun de veau : os rôtis, carottes, oignons, concentré de tomate, réduit huit heures.',
  'Vinaigrette maison : moutarde, vinaigre de xérès, huile de noix, sel, poivre.',
  'Velouté de potiron : potiron, oignon, crème fraîche, une pointe de muscade.',
  'Beurre blanc : échalotes, vin blanc, beurre froid monté au fouet.',
  'Coulis de framboise : framboises, sucre, un filet de citron.',
];
const QUESTION = 'Table 4 : la tarte de la maison, celle de la grand-mère du patron.';

const f = await pipeline('feature-extraction', 'Xenova/multilingual-e5-small', { dtype: 'fp32' });
const emb = async (t) => Array.from((await f(t, { pooling: 'mean', normalize: true })).data);
const vf = [];
for (const t of FICHES) vf.push(await emb('passage: ' + t));
const vq = await emb('query: ' + QUESTION);
const cos = (a, b) => a.reduce((s, x, i) => s + x * b[i], 0);
const scores = vf.map(v => cos(v, vq));

// projection 2D (ACP) des 9 vecteurs : deux premières composantes
const X = [...vf, vq], n = X.length, d = X[0].length;
const moy = Array(d).fill(0); X.forEach(v => v.forEach((x, i) => moy[i] += x / n));
const C = X.map(v => v.map((x, i) => x - moy[i]));
function composante(C, exclure) {
  let w = Array.from({ length: d }, (_, i) => Math.sin(i + 1));
  for (let it = 0; it < 300; it++) {
    const s = C.map(v => v.reduce((a, x, i) => a + x * w[i], 0));
    let nw = Array(d).fill(0); C.forEach((v, k) => v.forEach((x, i) => nw[i] += x * s[k]));
    if (exclure) { const p = nw.reduce((a, x, i) => a + x * exclure[i], 0); nw = nw.map((x, i) => x - p * exclure[i]); }
    const no = Math.hypot(...nw); w = nw.map(x => x / no);
  }
  return w;
}
const w1 = composante(C), w2 = composante(C, w1);
const proj = C.map(v => [v.reduce((a, x, i) => a + x * w1[i], 0), v.reduce((a, x, i) => a + x * w2[i], 0)]);

const r = (x, k = 4) => +x.toFixed(k);
fs.writeFileSync('cuisine-embeddings-2.json', JSON.stringify({
  modele: 'Xenova/multilingual-e5-small (384 dimensions, normalisés)',
  fiches: FICHES.map((t, i) => ({ t, v: vf[i].map(x => r(x)), score: r(scores[i]), xy: proj[i].map(x => r(x)) })),
  question: { t: QUESTION, v: vq.map(x => r(x)), xy: proj[n - 1].map(x => r(x)) },
}));
console.log(scores.map((s, i) => s.toFixed(3) + '  ' + FICHES[i].slice(0, 40)).join('\n'));
console.log('q', vq.slice(0, 6).map(x => x.toFixed(3)));
