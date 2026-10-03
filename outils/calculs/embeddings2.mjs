// Embeddings : une question SANS mot en commun avec les préparations, et ce que trouvent (1) les mots en commun, (2) le sens.
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
const QUESTIONS = ['Un dessert léger aux fruits rouges', 'Une sauce pour accompagner un poisson', 'De quoi assaisonner une salade'];
const MODELE = process.argv[2] || 'Xenova/multilingual-e5-small', DT = process.argv[3] || 'fp32', PREFIXE = MODELE.includes('e5');
const f = await pipeline('feature-extraction', MODELE, { dtype: DT });
const POOL = MODELE.includes('bge') ? 'cls' : 'mean';
const emb = async t => Array.from((await f(t, { pooling: POOL, normalize: true })).data);
const cos = (a, b) => a.reduce((s, x, i) => s + x * b[i], 0);
const VIDES = new Set('un une des de du la le les l d au aux à et pour en avec'.split(' '));
const mots = t => new Set(t.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/[^a-z ]/g, ' ').split(/\s+/).filter(m => m.length > 1 && !VIDES.has(m)));
const vf = []; for (const t of FICHES) vf.push(await emb((PREFIXE ? 'passage: ' : '') + t));
const out = { modele: MODELE + ' (' + DT + ')', fiches: FICHES, questions: [] };
for (const q of QUESTIONS) {
  const vq = await emb((PREFIXE ? 'query: ' : '') + q), mq = mots(q);
  const r = FICHES.map((t, i) => ({ i, cos: +cos(vq, vf[i]).toFixed(4), communs: [...mots(t)].filter(m => mq.has(m)) }));
  out.questions.push({ q, r });
  console.log(q); [...r].sort((a, b) => b.cos - a.cos).forEach(x => console.log('  ', x.cos, x.communs.join(',') || '-', FICHES[x.i].slice(0, 30)));
}
fs.writeFileSync('embeddings2-' + MODELE.split('/')[1] + '.json', JSON.stringify(out));
