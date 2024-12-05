import re
import os
import shutil
from pathlib import Path

def extract_image_paths(tex_file):
    with open(tex_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Trova tutte le occorrenze di \includegraphics
    image_paths = re.findall(r'\\includegraphics(?:\[.*?\])?{([^}]+)}', content)
    return image_paths

def copy_images(source_dir, target_dir, image_paths):
    for img_path in image_paths:
        source_path = Path(source_dir) / img_path
        target_path = Path(target_dir) / img_path
        
        # Crea le sottodirectory necessarie
        target_path.parent.mkdir(parents=True, exist_ok=True)
        
        try:
            shutil.copy2(source_path, target_path)
            print(f"Copiato: {img_path}")
        except FileNotFoundError:
            print(f"Non trovato: {img_path}")

def main():
    source_dir = '.'
    target_dir = '/home/antonio/presentazioni'
    
    # Crea la directory target se non esiste
    Path(target_dir).mkdir(parents=True, exist_ok=True)
    
    # Estrai i percorsi delle immagini
    image_paths = extract_image_paths('appunti.tex')
    
    # Copia le immagini
    copy_images(source_dir, target_dir, image_paths)

if __name__ == '__main__':
    main()
