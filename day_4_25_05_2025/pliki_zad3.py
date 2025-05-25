import os
import shutil

root_dir = "katalog"
target_name = "results.txt"
dest_dir = "zebrane"

if not os.path.exists(root_dir):
    os.makedirs(root_dir)

source_path = os.path.join(root_dir, target_name)
with open(source_path, "w", encoding="utf-8") as src:
    src.write("Treść\n")

if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

output_path = os.path.join(dest_dir, target_name)

with open(output_path, "w", encoding='utf-8') as out:
    for dirpath, _, filenames in os.walk(root_dir):
        for fname in filenames:
            if fname == target_name:
                src_path = os.path.join(dirpath, fname)
                out.write(f"\n Plik z: {src_path}\n")
                with open(src_path, encoding='utf-8') as f:
                    # kopiuje zawartoś jedego pliku do drugiego
                    shutil.copyfileobj(f, out)

print("Połaczone pliki:", output_path)
