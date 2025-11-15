📉 AI Token Optimizer Toolkit

Une suite d'outils en ligne de commande (CLI) conçue pour le Prompt Engineering et l'optimisation des coûts liés aux LLMs (GPT-4, Claude, Mistral, etc.).

Ce dépôt contient deux scripts distincts pour transformer vos fichiers de données (.json) et réduire drastiquement la consommation de tokens :

    token_optimizer.py : Convertit en YAML Flow ou JSON Minifié (Garde la structure, haute compatibilité).

    json_flattener.py : Convertit en Texte Compact (Supprime la syntaxe, économie maximale).

💡 Pourquoi ces outils ?

Les modèles de langage (LLM) facturent au token. La structure JSON standard est verbeuse (guillemets, accolades, sauts de ligne). Ces scripts nettoient vos données pour ne garder que l'essentiel.

Comparatif des Gains

Pour l'entrée : {"utilisateur": {"nom": "Alice", "id": 101}, "roles": ["admin"]}
Format	Script	Contenu Résultant	Tokens (est.)
JSON Standard	(Original)	{"utilisateur": { "nom": ...	~22
JSON Minifié	token_optimizer.py	{"utilisateur":{"nom":"Alice"...	~18
YAML Flow	token_optimizer.py	{utilisateur: {nom: Alice...	~14
Flat Text 🚀	json_flattener.py	utilisateur:nom:Alice, id:101...	~10

    Résultat : Vous pouvez économiser 30% à 50% de tokens sur des gros fichiers de contexte.

🛠️ Installation

    Clonez ce dépôt :
    Bash

git clone https://github.com/votre-nom/ai-token-optimizer.git
cd ai-token-optimizer

Installez les dépendances requises :
Bash

    pip install -r requirements.txt

    (Nécessite pyyaml et tiktoken)

🚀 Outil 1 : Token Optimizer (Structure Conservée)

Fichier : token_optimizer.py

Utilisez ce script si vous avez besoin que le LLM comprenne parfaitement la structure hiérarchique (objets imbriqués complexes) mais que vous voulez réduire le bruit. Le format YAML est recommandé.

Utilisation

Bash

# 1. Optimiser un fichier (Affiche les stats seulement)
python token_optimizer.py data/mon_fichier.json

# 2. Sauvegarder le résultat (Crée un .yaml ou .min.json)
python token_optimizer.py data/mon_fichier.json --save

# 3. Choisir le format (YAML par défaut, JSON minifié optionnel)
python token_optimizer.py data/mon_fichier.json --format json --save

🚀 Outil 2 : JSON Flattener (Économie Maximale)

Fichier : json_flattener.py

Utilisez ce script pour injecter de la "Data brute" dans un prompt. Il supprime les { } et les " pour créer une chaîne clé:valeur. Idéal pour donner du contexte (RAG, historique) où la syntaxe stricte importe peu.

Utilisation

Bash

# 1. Aplatir un fichier et voir le gain
python json_flattener.py data/gros_fichier.json

# 2. Sauvegarder le résultat (Crée un fichier .txt)
python json_flattener.py data/gros_fichier.json --save

Exemple de sortie (Flattener) :
Plaintext

🔧 Aplatissement de : user_data.json
========================================
Tokens Original : 450
Tokens Compacts : 210
Gain net        : 240 (53.3%)
Aperçu Résultat : id:4821, name:Jean Dupont, roles:[admin, editor], history:login:2023-10-01
✅ Fichier généré  : user_data_flat.txt

⚡ Traitement par dossier

Les deux scripts supportent le traitement de masse. Pointez simplement vers un dossier :
Bash

# Optimise tous les JSON du dossier en YAML
python token_optimizer.py ./mes_donnees --save

# Aplatit tous les JSON du dossier en Texte
python json_flattener.py ./mes_donnees --save

📦 Dépendances Techniques

    Tiktoken : Utilisé pour calculer l'économie exacte de tokens (basé sur l'encodeur cl100k_base de GPT-4).

    PyYAML : Pour la génération du format YAML Flow fiable.

🤝 Contribution

Les contributions sont les bienvenues !

    Forkez le projet

    Créez votre branche (git checkout -b feature/AmazingFeature)

    Committez vos changements (git commit -m 'Add some AmazingFeature')

    Ouvrez une Pull Request

📄 Licence

Distribué sous la licence MIT. Voir LICENSE pour plus d'informations.
