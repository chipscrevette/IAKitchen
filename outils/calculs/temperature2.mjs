// Probabilité de chaque ingrédient COMPLET après la phrase (produit des probabilités de ses tokens),
// avec Qwen2.5-0.5B-Instruct (fp16). Sert de « logit » par mot : p(T) ∝ exp(log P / T).
import { AutoTokenizer, AutoModelForCausalLM } from '@huggingface/transformers';
import fs from 'fs';
const ID = 'onnx-community/Qwen2.5-0.5B-Instruct';
const tok = await AutoTokenizer.from_pretrained(ID);
const model = await AutoModelForCausalLM.from_pretrained(ID, { dtype: 'fp16' });
const PHRASE = 'Pour relever la sauce, le chef ajoute une pincée de';
const MOTS = ['sel', 'poivre', 'sucre', 'paprika', 'piment', 'muscade', 'curry', 'cannelle', 'thym', 'chocolat', 'café', 'vanille'];
const base = Array.from(tok(PHRASE).input_ids.data).map(Number);
const logsoftmax = (row) => { let m = -Infinity; for (const x of row) if (x > m) m = x; let z = 0; for (const x of row) z += Math.exp(x - m); return row.map(x => x - m - Math.log(z)); };
const res = [];
for (const mot of MOTS) {
  const ids = Array.from(tok(PHRASE + ' ' + mot).input_ids.data).map(Number);
  const suite = ids.slice(base.length);
  const { Tensor } = await import('@huggingface/transformers');
  const input_ids = new Tensor('int64', BigInt64Array.from(ids.map(BigInt)), [1, ids.length]);
  const attention_mask = new Tensor('int64', BigInt64Array.from(ids.map(() => 1n)), [1, ids.length]);
  const { logits } = await model({ input_ids, attention_mask });
  const V = logits.dims[2];
  let lp = 0;
  suite.forEach((t, j) => { const pos = base.length - 1 + j; const row = Array.from(logits.data.slice(pos * V, (pos + 1) * V)); lp += logsoftmax(row)[t]; });
  res.push({ mot, tokens: suite.map(t => tok.decode([t])), logp: +lp.toFixed(4), p: +Math.exp(lp).toFixed(6) });
  console.log(mot, suite.map(t => tok.decode([t])), lp.toFixed(3), Math.exp(lp).toFixed(5));
}
fs.writeFileSync('temperature2.json', JSON.stringify({ modele: ID + ' (fp16)', phrase: PHRASE, mots: res }));
