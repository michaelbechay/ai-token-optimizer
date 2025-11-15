# 📉 AI Token Optimizer Toolkit

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/)

Une suite d'outils en ligne de commande (CLI) conçue pour le **Prompt Engineering** et l'optimisation des coûts liés aux LLMs (GPT-4, Claude, Mistral, etc.).

Ce dépôt contient deux scripts distincts pour transformer vos fichiers de données (`.json`) et réduire drastiquement la consommation de tokens :

1.  **`token_optimizer.py`** : Convertit en **YAML Flow** ou **JSON Minifié** (Garde la structure, haute compatibilité).
2.  **`json_flattener.py`** : Convertit en **Texte Compact** (Supprime la syntaxe, économie maximale).

## 💡 Pourquoi ces outils ?

Les modèles de langage (LLM) facturent au token. La structure JSON standard est verbeuse (guillemets, accolades, sauts de ligne). Ces scripts nettoient vos données pour ne garder que l'essentiel.

### Comparatif des Gains

Pour l'entrée : `{"utilisateur": {"nom": "Alice", "id": 101}, "roles": ["admin"]}`

| Format | Script | Contenu Résultant | Tokens (est.) |
| :--- | :--- | :--- | :--- |
| **JSON Standard** | *(Original)* | `{"utilisateur": { "nom": ...` | **~22** |
| **JSON Minifié** | `token_optimizer.py` | `{"utilisateur":{"nom":"Alice"...` | **~18** |
| **YAML Flow** | `token_optimizer.py` | `{utilisateur: {nom: Alice...` | **~14** |
| **Flat Text** 🚀 | `json_flattener.py` | `utilisateur:nom:Alice, id:101...` | **~10** |

> **Résultat :** Vous pouvez économiser **30% à 50%** de tokens sur des gros fichiers de contexte.

---

## 🛠️ Installation

1. Clonez ce dépôt :
   ```bash
   git clone [https://github.com/votre-nom/ai-token-optimizer.git](https://github.com/votre-nom/ai-token-optimizer.git)
   cd ai-token-optimizer
