import shutil
from pathlib import Path

# base_path = Path('../ops_example')
base_path = Path('ops_example')
base_path2 = Path('ops_example/D')

if base_path.exists() and base_path.is_dir():
    # Recursively delete a directory tree
    shutil.rmtree(base_path)

base_path.mkdir()

path_b = base_path / 'A' / 'B'
path_c = base_path / 'A' / 'C'
path_d = base_path / 'A' / 'D'

# nie ma katalogu A, nie moge utworzyć B
# path_b.mkdir() # FileNotFoundError: [Errno 2] No such file or directory: 'ops_example/A/B'
path_b.mkdir(parents=True)  # parents=True - tworzy wszystkie potrzebne katalogi w drzewie

# zadziałą bo katalog A już istnieje
path_c.mkdir()

# utworzenie plików w katalogu path_b
for filename in ('ex1.txt', 'ex2.txt', 'ex3.txt'):
    with open(path_b / filename, "w", encoding='utf-8') as stream:
        stream.write(f"Jakaś tresć w pliku {filename}")

# przeniesienie plików do innego katalogu
# stworzył katalog D, usunął B
shutil.move(path_b, path_d)

# kopiowanie pliku
shutil.copy(path_d / 'ex1.txt', path_c / 'ex1.txt')

# zmiana nazwy pliku
ex1 = path_d / 'ex1.txt'
ex1.rename(ex1.parent / 'ex1renamed.log')

print(base_path.absolute())  # ścieżka absolutna do pliku
# /Users/radoslawjaniak/PycharmProjects/Bootcamp-10-05-2025/day_4_25_05_2025/ops_example
print(base_path.name)  # ops_example, nazwa głownego katalogu
# scieżka do nadrzędnego katalogu
print(base_path.parent.absolute())  # /Users/radoslawjaniak/PycharmProjects/Bootcamp-10-05-2025/day_4_25_05_2025

print("-----")
print(base_path.suffix)
print(ex1.suffix)  # .txt
print(base_path.parts)  # ('ops_example',)
print(base_path2.parts)  # ('ops_example', 'D')

path_abs = "/Users/radoslawjaniak/PycharmProjects/Bootcamp-10-05-2025/day_4_25_05_2025/ops_example/A/D/ex1renamed.log"
with open(path_abs, "r") as f:
    lines = f.read()

print(lines)  # Jakaś tresć w pliku ex1.txt
# C:\\BotPython\\2025-05-25 zajecia\\ops_example - nalezy dopisac \
# r"C:\BotPython\2025-05-25 zajecia\ops_example" -> r - raw string
