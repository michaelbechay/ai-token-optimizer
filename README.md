# 📉 AI Token Optimizer

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/)

Un outil en ligne de commande (CLI) conçu pour le **Prompt Engineering** et l'optimisation des coûts liés aux LLMs (GPT-4, Claude, etc.).

Ce script prend vos fichiers de données (`.json`) et les transforme en formats densifiés (**YAML Flow Style** ou **JSON Minifié**) afin de réduire drastiquement la consommation de tokens dans vos prompts, sans perdre en lisibilité pour l'IA.

## 💡 Pourquoi cet outil ?

Les modèles de langage (LLM) facturent au token. La structure JSON standard est verbeuse :
- Beaucoup de guillemets `"clé": "valeur"`
- Beaucoup d'accolades `{ }` et de retours à la ligne.

**AI Token Optimizer** résout ce problème en convertissant vos données vers le format **YAML Flow**, qui supprime les guillemets superflus et condense la structure.

### Exemple de Gain

| Format | Contenu | Tokens (est.) |
| :--- | :--- | :--- |
| **JSON Standard** | `{"nom": "Alice", "statut": "admin"}` | **11** |
| **JSON Minifié** | `{"nom":"Alice","statut":"admin"}` | **9** |
| **YAML Flow (Gagnant)** | `{nom: Alice, statut: admin}` | **7** |

> **Résultat :** Sur de gros fichiers, vous pouvez économiser **20% à 40%** de tokens, augmentant ainsi votre fenêtre de contexte disponible et réduisant vos factures.

## ⚡ Fonctionnalités

- **Précision Tiktoken** : Utilise l'encodeur officiel d'OpenAI (`cl100k_base`) pour calculer l'économie exacte de tokens avant/après.
- **Mode YAML Flow** : La compression la plus efficace pour les LLMs modernes.
- **Mode JSON Minified** : Suppression de tous les espaces blancs inutiles (`whitespace stripping`).
- **Traitement par Lot** : Fonctionne sur un fichier unique ou scanne un dossier entier.
- **Support Unicode** : Préserve les accents (é, à, ç) pour éviter l'explosion des tokens due à l'encodage ASCII (`\u00e9`).

## 🛠️ Installation

1. Clonez ce dépôt :
   ```bash
   git clone [https://github.com/votre-nom/ai-token-optimizer.git](https://github.com/votre-nom/ai-token-optimizer.git)
   cd ai-token-optimizer

    Installez les dépendances requises :
    Bash

    pip install -r requirements.txt

    (Si vous n'avez pas de fichier requirements.txt, installez simplement : pip install pyyaml tiktoken)

🚀 Utilisation

1. Optimiser un seul fichier

Affiche les statistiques d'économie sans sauvegarder :
Bash

python token_optimizer.py data/mon_fichier.json

2. Optimiser et Sauvegarder

Génère un fichier optimisé (ex: mon_fichier_opt.yaml) :
Bash

python token_optimizer.py data/mon_fichier.json --save

3. Choisir le format de sortie

Par défaut, l'outil utilise yaml. Vous pouvez forcer le JSON minifié :
Bash

python token_optimizer.py data/mon_fichier.json --format json --save

4. Traiter tout un dossier

Optimise tous les fichiers .json présents dans un répertoire :
Bash

python token_optimizer.py ./mes_donnees --save

📊 Exemple de Sortie

Plaintext

📄 Traitement de : user_profile.json
----------------------------------------
Format Cible   : YAML
Tokens Avant   : 450
Tokens Après   : 310
Économie       : 140 tokens (31.11%)
Aperçu         : {id: 4821, name: Jean Dupont, roles: [admin, editor], history: {login: 2023-10-01, ...}}
💾 Sauvegardé sous : user_profile_opt.yaml

📦 Dépendances

    PyYAML : Pour la génération du format YAML compact.

    tiktoken : Pour le comptage précis des tokens (le même que celui utilisé par OpenAI).

🤝 Contribution

Les contributions sont les bienvenues ! Si vous avez des idées pour optimiser encore plus les données (ex: suppression automatique des clés vides), n'hésitez pas à ouvrir une Pull Request.

    Forkez le projet

    Créez votre branche (git checkout -b feature/AmazingFeature)

    Committez vos changements (git commit -m 'Add some AmazingFeature')

    Pushez vers la branche (git push origin feature/AmazingFeature)

    Ouvrez une Pull Request

📄 Licence

Distribué sous la licence MIT. Voir LICENSE pour plus d'informations.


### Petite astuce supplémentaire pour toi
Pour que le README soit complet, n'oublie pas de créer un fichier `requirements.txt` à la racine de ton projet avec ce contenu :

```text
pyyaml
tiktoken
