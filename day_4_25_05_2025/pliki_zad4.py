import glob

folder_path = "katalog/"

# wczytuje nazwy dla plików z rozszerzeniem .txt
txt_files = glob.glob(f"{folder_path}*.txt")
print(f"Znalezione pliki .txt: {txt_files}")
# Znalezione pliki .txt: ['katalog/nowy.txt', 'katalog/results.txt']

# pliki z wzorcem
pattern_files = glob.glob(f"{folder_path}file_[0-2].txt")
print(f"Znalezione pliki  wzorzec .txt: {pattern_files}")
# Znalezione pliki  wzorzec .txt: ['katalog/file_1.txt']

all_txt_recursive = glob.glob("**/*.txt", recursive=True)
print(f"Znalezione pliki  rekursywnie .txt: {all_txt_recursive}")
