import os
import re

def clean_filename(name):
    # Rimuove caratteri non validi per i nomi dei file
    return re.sub(r'[^\w\-_\. ]', '_', name)

def split_latex_file(input_file, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # Estrai il preambolo
    preambolo_match = re.search(r'%%iniziopreambolo.*?%%finepreambolo', content, re.DOTALL)
    if preambolo_match:
        preambolo = preambolo_match.group()
        with open(os.path.join(output_dir, '0-preambolo.tex'), 'w', encoding='utf-8') as f:
            f.write(preambolo)
        
        # Rimuovi il preambolo dal contenuto principale
        content = content[preambolo_match.end():]

    # Trova tutte le sezioni
    sections = re.split(r'(\\section\*?{.*?})', content, flags=re.DOTALL)

    # Il primo elemento sarà il contenuto prima della prima sezione
    if sections[0].strip():
        with open(os.path.join(output_dir, '1-introduzione.tex'), 'w', encoding='utf-8') as f:
            f.write(sections[0])

    # Processa le sezioni
    for i in range(1, len(sections), 2):
        if i+1 < len(sections):
            section_title = re.search(r'{(.*?)}', sections[i]).group(1)
            filename = f"{(i+1)//2+1}-{clean_filename(section_title)}.tex"
            with open(os.path.join(output_dir, filename), 'w', encoding='utf-8') as f:
                f.write(sections[i] + sections[i+1])

if __name__ == "__main__":
    input_file = "appunti.tex"
    output_dir = "sezioni"
    split_latex_file(input_file, output_dir)
    print(f"File suddiviso in sezioni nella cartella '{output_dir}'")
