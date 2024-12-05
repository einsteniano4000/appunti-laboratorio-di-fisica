import re
import os
import shutil
from pathlib import Path

def extract_image_paths(tex_file):
    with open(tex_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern per vari comandi di immagini in LaTeX
    patterns = [
        r'\\includegraphics(?:\[.*?\])?{([^}]+)}',  # \includegraphics
        r'\\import{([^}]+)}{([^}]+)}',              # \import
        r'\\figure{([^}]+)}',                       # \figure
        r'\\input{([^}]+)}',                        # \input
        r'\\pgfimage{([^}]+)}',                     # \pgfimage
        r'\\epsfig{[^{}]*file=([^,}]+)[^}]*}'      # \epsfig
    ]
    
    paths = []
    for pattern in patterns:
        matches = re.finditer(pattern, content)
        for match in matches:
            # Gestisce gruppi multipli (es. \import ha path e filename)
            groups = match.groups()
            if len(groups) > 1:
                paths.append(os.path.join(*groups))
            else:
                paths.append(groups[0])
    
    # Risolvi estensioni mancanti
    resolved_paths = []
    extensions = ['.png', '.jpg', '.jpeg', '.pdf', '.eps', '.tikz', '.pgf']
    
    for path in paths:
        if os.path.splitext(path)[1]:
            resolved_paths.append(path)
        else:
            for ext in extensions:
                if os.path.exists(os.path.join('.', path + ext)):
                    resolved_paths.append(path + ext)
                    break
    
    return list(set(resolved_paths))  # Rimuovi duplicati

def copy_images(source_dir, target_dir, image_paths):
    copied = []
    not_found = []
    
    for img_path in image_paths:
        source_path = Path(source_dir) / img_path
        target_path = Path(target_dir) / img_path
        
        target_path.parent.mkdir(parents=True, exist_ok=True)
        
        try:
            shutil.copy2(source_path, target_path)
            copied.append(img_path)
        except FileNotFoundError:
            not_found.append(img_path)
            print(f"Non trovato: {img_path}")
            # Prova a cercare in sottocartelle
            for root, dirs, files in os.walk(source_dir):
                filename = os.path.basename(img_path)
                if filename in files:
                    found_path = os.path.join(root, filename)
                    shutil.copy2(found_path, target_path)
                    copied.append(img_path)
                    not_found.remove(img_path)
                    print(f"Trovato in: {found_path}")
                    break

    return copied, not_found

def main():
    source_dir = '.'
    target_dir = '/home/antonio/presentazioni'
    
    Path(target_dir).mkdir(parents=True, exist_ok=True)
    
    print("Cercando immagini...")
    image_paths = extract_image_paths('appunti.tex')
    print(f"Trovati {len(image_paths)} riferimenti a immagini")
    
    copied, not_found = copy_images(source_dir, target_dir, image_paths)
    
    print(f"\nRiepilogo:")
    print(f"Immagini copiate con successo: {len(copied)}")
    if not_found:
        print("\nImmagini non trovate:")
        for path in not_found:
            print(f"- {path}")

if __name__ == '__main__':
    main()
