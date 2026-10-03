// Catalogue des notions : 5 familles, 25 notions.
// open = rédigée pour la première vague ; seule « hallucination » a son contenu dans la maquette.
window.CATALOGUE = {
  familles: [
    { id: 'moteur',    nom: 'Le moteur',              couleur: '#D8432B' },
    { id: 'memoire',   nom: 'La mémoire de travail',  couleur: '#2B5FB3' },
    { id: 'mains',     nom: 'Les mains',              couleur: '#E0A21B' },
    { id: 'agents',    nom: 'Les agents',             couleur: '#23915A' },
    { id: 'confiance', nom: 'La confiance',           couleur: '#7A4BA8' },
  ],
  notions: [
    { id: 'mot-suivant',   famille: 'moteur',    nom: 'Le mot suivant',             court: 'Mot suivant',            question: 'Un LLM, c’est quoi vraiment ?' },
    { id: 'token',         famille: 'moteur',    nom: 'Le token',                   court: 'Token',                  question: 'Pourquoi l’IA compte-t-elle en morceaux ?', open: true },
    { id: 'temperature',   famille: 'moteur',    nom: 'La température',             court: 'Température',            question: 'Pourquoi la même question donne deux réponses ?', open: true },
    { id: 'hallucination', famille: 'moteur',    nom: 'L’hallucination',            court: 'Hallucination',          question: 'Pourquoi l’IA invente-t-elle ?', open: true },
    { id: 'entrainement',  famille: 'moteur',    nom: 'L’entraînement',             court: 'Entraînement',           question: 'D’où vient ce qu’elle sait ?' },
    { id: 'fine-tuning',   famille: 'moteur',    nom: 'Le fine-tuning',             court: 'Fine-tuning',            question: 'Peut-on lui apprendre nos habitudes ?', open: true },

    { id: 'contexte',      famille: 'memoire',   nom: 'La fenêtre de contexte',     court: 'Fenêtre de contexte',    question: 'Que voit l’IA quand elle répond ?', open: true },
    { id: 'lost',          famille: 'memoire',   nom: 'Lost in the middle',         court: 'Lost in the middle',     question: 'Pourquoi ne pas tout lui donner ?' },
    { id: 'embeddings',    famille: 'memoire',   nom: 'Les embeddings',             court: 'Embeddings',             question: 'Comment l’IA range-t-elle le sens ?' },
    { id: 'rag',           famille: 'memoire',   nom: 'Le RAG',                     court: 'RAG',                    question: 'Comment lui faire lire nos documents ?', open: true },
    { id: 'context-eng',   famille: 'memoire',   nom: 'Le context engineering',     court: 'Context engineering',    question: 'Que poser sur son bureau ?' },

    { id: 'rag-ou-outil',  famille: 'mains',     nom: 'RAG ou outil ?',             court: 'RAG ou outil ?',         question: 'Lire ou calculer ?' },
    { id: 'appel-outil',   famille: 'mains',     nom: 'L’appel d’outil',            court: 'Appel d’outil',          question: 'L’IA agit-elle vraiment ?' },
    { id: 'mcp',           famille: 'mains',     nom: 'MCP',                        court: 'MCP',                    question: 'Comment brancher un outil ?', open: true },
    { id: 'trop-outils',   famille: 'mains',     nom: 'Trop d’outils',              court: 'Trop d’outils',          question: 'Faut-il tout brancher ?' },

    { id: 'boucle',        famille: 'agents',    nom: 'La boucle',                  court: 'La boucle',              question: 'Comment un agent avance-t-il ?' },
    { id: 'workflow',      famille: 'agents',    nom: 'Workflow ou agent',          court: 'Workflow ou agent',      question: 'Qui choisit le chemin ?' },
    { id: 'memoire-longue',famille: 'agents',    nom: 'La mémoire longue',          court: 'Mémoire longue',         question: 'Comment se souvient-il de moi ?' },
    { id: 'multi',         famille: 'agents',    nom: 'Multi-agents et A2A',        court: 'Multi-agents · A2A',     question: 'Et à plusieurs ?' },
    { id: 'humain',        famille: 'agents',    nom: 'L’humain dans la boucle',    court: 'Humain dans la boucle',  question: 'Qui valide à la fin ?' },

    { id: 'evaluation',    famille: 'confiance', nom: 'L’évaluation',               court: 'Évaluation',             question: 'Comment savoir si elle a raison ?' },
    { id: 'temoin',        famille: 'confiance', nom: 'Le groupe témoin',           court: 'Groupe témoin',          question: 'Le gain vient-il vraiment de l’IA ?' },
    { id: 'cout',          famille: 'confiance', nom: 'Coût et délai',              court: 'Coût et délai',          question: 'Combien ça coûte vraiment ?' },
    { id: 'injection',     famille: 'confiance', nom: 'L’injection de prompt',      court: 'Injection de prompt',    question: 'Peut-on la manipuler ?' },
    { id: 'donnees',       famille: 'confiance', nom: 'Les données confidentielles',court: 'Données confidentielles',question: 'Où part ce que je tape ?' },
  ],
};
CATALOGUE.famille = id => CATALOGUE.familles.find(f => f.id === id);
CATALOGUE.notion = id => CATALOGUE.notions.find(n => n.id === id);

// Espaces fines insécables avant ? ! : ; et « » — typographie française.
window.espacesFr = function (root) {
  const w = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
  const nodes = [];
  while (w.nextNode()) nodes.push(w.currentNode);
  for (const t of nodes) {
    if (t.parentElement && t.parentElement.closest('textarea, script, style')) continue;
    t.nodeValue = t.nodeValue
      .replace(/ ([?!;:»])/g, ' $1')
      .replace(/« /g, '« ')
      .replace(/(\d) %/g, '$1 %')              // « 2 % » ne se coupe jamais
      .replace(/(\d) (\d{3})(?!\d)/g, '$1 $2');   // « 128 000 » non plus
  }
};
