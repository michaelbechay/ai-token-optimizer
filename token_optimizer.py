import json
import yaml
import sys
import os
import argparse
import tiktoken
from typing import Any, Tuple

# --- Configuration ---
# Modèle d'encodage pour l'estimation (cl100k_base est utilisé par GPT-4 et GPT-3.5-turbo)
ENCODING_MODEL = "cl100k_base"

class TokenOptimizer:
    def __init__(self):
        try:
            self.encoder = tiktoken.get_encoding(ENCODING_MODEL)
            self.has_tiktoken = True
        except Exception as e:
            print(f"Attention: Impossible de charger tiktoken ({e}). Estimation approximative (char/4).")
            self.has_tiktoken = False

    def count_tokens(self, text: str) -> int:
        """Compte les tokens d'une chaîne de caractères."""
        if not text:
            return 0
        if self.has_tiktoken:
            return len(self.encoder.encode(text))
        else:
            # Estimation grossière si tiktoken échoue
            return len(text) // 4

    def load_json(self, file_path: str) -> Any:
        """Charge un fichier JSON."""
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def to_minified_json(self, data: Any) -> str:
        """Convertit en JSON minifié (suppression espaces/sauts de ligne)."""
        # separators=(',', ':') supprime l'espace après la virgule et les deux-points
        return json.dumps(data, separators=(',', ':'), ensure_ascii=False)

    def to_flow_yaml(self, data: Any) -> str:
        """Convertit en YAML style 'flow' (similaire à JSON mais sans guillemets superflus)."""
        # default_flow_style=True active le mode compact
        # width=float("inf") empêche le retour à la ligne automatique
        return yaml.dump(
            data, 
            default_flow_style=True, 
            width=float("inf"), 
            allow_unicode=True,
            sort_keys=False
        ).strip()

    def process_file(self, input_path: str, output_format: str, save: bool = False):
        """Traite un fichier spécifique et affiche les stats."""
        try:
            # 1. Lecture du fichier original (Texte brut pour le compte initial)
            with open(input_path, 'r', encoding='utf-8') as f:
                original_text = f.read()
            
            # 2. Parsing des données
            try:
                data = json.loads(original_text)
            except json.JSONDecodeError:
                print(f"❌ Erreur : '{input_path}' n'est pas un JSON valide.")
                return

            # 3. Transformation
            if output_format == 'yaml':
                optimized_text = self.to_flow_yaml(data)
                ext = ".yaml"
            else:
                optimized_text = self.to_minified_json(data)
                ext = ".min.json"

            # 4. Calcul des tokens
            tokens_before = self.count_tokens(original_text)
            tokens_after = self.count_tokens(optimized_text)
            saved_tokens = tokens_before - tokens_after
            percent_saved = (saved_tokens / tokens_before * 100) if tokens_before > 0 else 0

            # 5. Affichage des résultats
            print(f"\n📄 Traitement de : {os.path.basename(input_path)}")
            print("-" * 40)
            print(f"Format Cible   : {output_format.upper()}")
            print(f"Tokens Avant   : {tokens_before}")
            print(f"Tokens Après   : {tokens_after}")
            print(f"Économie       : {saved_tokens} tokens ({percent_saved:.2f}%)")
            
            # Aperçu visuel
            preview = optimized_text[:100] + "..." if len(optimized_text) > 100 else optimized_text
            print(f"Aperçu         : {preview}")

            # 6. Sauvegarde (Optionnel)
            if save:
                base_name = os.path.splitext(input_path)[0]
                out_path = f"{base_name}_opt{ext}"
                with open(out_path, 'w', encoding='utf-8') as f:
                    f.write(optimized_text)
                print(f"💾 Sauvegardé sous : {out_path}")

        except Exception as e:
            print(f"❌ Erreur inattendue sur {input_path}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Optimiseur de Tokens pour contextes IA (JSON -> Minified JSON / Flow YAML)")
    
    parser.add_argument("path", help="Chemin vers le fichier .json ou le dossier contenant les jsons")
    parser.add_argument("--format", choices=['json', 'yaml'], default='yaml', help="Format de sortie : 'json' (minifié) ou 'yaml' (flow style). Le YAML est souvent plus économe.")
    parser.add_argument("--save", action="store_true", help="Sauvegarder le résultat dans un nouveau fichier")

    args = parser.parse_args()

    optimizer = TokenOptimizer()
    
    # Vérification chemin
    if os.path.isfile(args.path):
        optimizer.process_file(args.path, args.format, args.save)
    elif os.path.isdir(args.path):
        print(f"📂 Analyse du dossier : {args.path}")
        for filename in os.listdir(args.path):
            if filename.lower().endswith('.json'):
                optimizer.process_file(os.path.join(args.path, filename), args.format, args.save)
    else:
        print("❌ Le chemin spécifié n'existe pas.")

if __name__ == "__main__":
    main()
