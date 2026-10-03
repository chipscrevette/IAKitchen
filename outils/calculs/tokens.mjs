// Vrais tokens : le tokenizer de GPT-4o (o200k), via transformers.js
import { AutoTokenizer } from '@huggingface/transformers';
import fs from 'fs';
const tok = await AutoTokenizer.from_pretrained('Xenova/gpt-4o');
const PHRASES = {
  fr: 'Je voudrais la tarte de la maison, s’il vous plaît.',
  en: 'I would like the house pie, please.',
  long: 'anticonstitutionnellement',
  court: 'tarte',
};
const out = { tokenizer: 'GPT-4o (o200k_base), via Xenova/gpt-4o' };
for (const [k, t] of Object.entries(PHRASES)) {
  const ids = tok.encode(t, { add_special_tokens: false });
  out[k] = { texte: t, ids, morceaux: ids.map(i => tok.decode([i])) };
  console.log(k, ids.length, JSON.stringify(out[k].morceaux));
}
out.taille_vocabulaire = tok.model.vocab ? tok.model.vocab.length : null;
fs.writeFileSync('tokens.json', JSON.stringify(out));
console.log('vocab', out.taille_vocabulaire);
