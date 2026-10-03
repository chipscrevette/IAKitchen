// Le mot suivant : probabilité de chaque ingrédient COMPLET après le début de la recette, avec Qwen2.5-0.5B-Instruct (fp16).
// À chaque tour, on ajoute l'ingrédient le plus probable et on recalcule (génération autorégressive).
import { AutoTokenizer, AutoModelForCausalLM, Tensor } from '@huggingface/transformers';
import fs from 'fs';
const ID = 'onnx-community/Qwen2.5-0.5B-Instruct';
const tok = await AutoTokenizer.from_pretrained(ID);
const model = await AutoModelForCausalLM.from_pretrained(ID, { dtype: 'fp16' });
const CANDIDATS = ['lait', 'sucre', 'beurre', 'sel', 'huile', 'eau', 'vanille', 'levure'];
const logsoftmax = row => { let m = -Infinity; for (const x of row) if (x > m) m = x; let z = 0; for (const x of row) z += Math.exp(x - m); return row.map(x => x - m - Math.log(z)); };
async function probas(debut) {
  const base = Array.from(tok(debut).input_ids.data).map(Number);
  const res = [];
  for (const mot of CANDIDATS) {
    const ids = Array.from(tok(debut + ' ' + mot).input_ids.data).map(Number), suite = ids.slice(base.length);
    const input_ids = new Tensor('int64', BigInt64Array.from(ids.map(BigInt)), [1, ids.length]);
    const attention_mask = new Tensor('int64', BigInt64Array.from(ids.map(() => 1n)), [1, ids.length]);
    const { logits } = await model({ input_ids, attention_mask });
    const V = logits.dims[2]; let lp = 0;
    suite.forEach((t, j) => { const pos = base.length - 1 + j; lp += logsoftmax(Array.from(logits.data.slice(pos * V, (pos + 1) * V)))[t]; });
    res.push({ mot, logp: +lp.toFixed(4), p: +Math.exp(lp).toFixed(6) });
  }
  return res.sort((a, b) => b.p - a.p);
}
let debut = 'Recette de la pâte à crêpes. Ingrédients : farine, œufs,';
const tours = [];
for (let t = 0; t < 3; t++) {
  const r = await probas(debut);
  tours.push({ debut, candidats: r });
  console.log(debut); r.forEach(x => console.log('   ', x.mot, x.p));
  debut += ' ' + r[0].mot + ',';
}
fs.writeFileSync('motsuivant.json', JSON.stringify({ modele: ID + ' (fp16)', tours }));
