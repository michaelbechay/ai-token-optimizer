import json
import sys
import os
import argparse
import tiktoken
from typing import Any

# --- Configuration ---
ENCODING_MODEL = "cl100k_base"

class CompactStringConverter:
    """
    Classe dédiée à la conversion de structures de données en texte brut ultra-compact.
    Distincte de l'optimiseur JSON/YAML standard.
    """
    def __init__(self):
        try:
            self.encoder = tiktoken.get_encoding(ENCODING_MODEL)
            self.tiktoken_available = True
        except Exception as e:
            print(f"⚠️  Tiktoken non détecté ({e}). Mode estimation activé.")
            self.tiktoken_available = False

    def get_token_count(self, text: str) -> int:
        """Calcule le coût en tokens du texte généré."""
        if not text:
            return 0
        if self.tiktoken_available:
            return len(self.encoder.encode(text))
        return len(text) // 4

    def flatten_data(self, data: Any) -> str:
        """
        Transforme récursivement les données en chaîne de caractères "clé:valeur".
        Supprime les accolades et les guillemets de structure.
        """
        if isinstance(data, dict):
            # On concatène les paires clé:valeur avec un séparateur virgule-espace
            # Format : clé1:valeur1, clé2:valeur2
            return ", ".join(f"{k}:{self.flatten_data(v)}" for k, v in data.items())
        
        elif isinstance(data, list):
            # Pour les listes, on garde des crochets légers pour indiquer le groupe
            # Format : [item1, item2]
            items = ", ".join(self.flatten_data(x) for x in data)
            return f"[{items}]"
        
        elif data is None:
            return "null"
        
        elif isinstance(data, bool):
            return "true" if data else "false"
            
        else:
            # Pour les nombres et les chaînes, on convertit directement
            return str(data).strip()

    def execute_conversion(self, input_file: str, save_output: bool = False):
        """Orchestre la lecture, la conversion et l'affichage."""
        try:
            # 1. Lecture
            with open(input_file, 'r', encoding='utf-8') as f:
                raw_content = f.read()

            # 2. Chargement JSON
            try:
                json_obj = json.loads(raw_content)
            except json.JSONDecodeError:
                print(f"❌ Erreur de syntaxe JSON dans : {input_file}")
                return

            # 3. Conversion en chaîne compacte
            flat_text = self.flatten_data(json_obj)

            # 4. Comparaison
            tokens_in = self.get_token_count(raw_content)
            tokens_out = self.get_token_count(flat_text)
            diff = tokens_in - tokens_out
            reduction = (diff / tokens_in * 100) if tokens_in > 0 else 0

            # 5. Rapport
            print(f"\n🔧 Aplatissement de : {os.path.basename(input_file)}")
            print("=" * 40)
            print(f"Tokens Original : {tokens_in}")
            print(f"Tokens Compacts : {tokens_out}")
            print(f"Gain net        : {diff} ({reduction:.1f}%)")
            
            # Aperçu (sans sauts de ligne pour l'affichage console)
            preview = flat_text[:120].replace('\n', ' ') + "..." if len(flat_text) > 120 else flat_text
            print(f"Aperçu Résultat : {preview}")

            # 6. Sauvegarde
            if save_output:
                base, _ = os.path.splitext(input_file)
                output_filename = f"{base}_flat.txt" # Extension .txt car ce n'est plus du JSON
                with open(output_filename, 'w', encoding='utf-8') as f_out:
                    f_out.write(flat_text)
                print(f"✅ Fichier généré  : {output_filename}")

        except Exception as e:
            print(f"❌ Erreur critique sur {input_file}: {e}")

def run_script():
    parser = argparse.ArgumentParser(description="JSON Flattener - Convertisseur JSON vers Texte Compact")
    parser.add_argument("target", help="Fichier JSON cible")
    parser.add_argument("--save", action="store_true", help="Sauvegarder le résultat en .txt")

    args = parser.parse_args()
    converter = CompactStringConverter()

    if os.path.isfile(args.target):
        converter.execute_conversion(args.target, args.save)
    else:
        print("❌ Fichier introuvable.")

if __name__ == "__main__":
    run_script()
