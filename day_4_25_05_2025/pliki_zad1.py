# praca z plikami
# ========= ===============================================================
#     Character Meaning
#     --------- ---------------------------------------------------------------
#     'r'       open for reading (default)
#     'w'       open for writing, truncating the file first
#     'x'       create a new file and open it for writing
#     'a'       open for writing, appending to the end of the file if it exists
#     'b'       binary mode
#     't'       text mode (default)
#     '+'       open a disk file for updating (reading and writing)
#     ========= ===============================================================
fh = open("test_fh.txt", "w", encoding="utf-8")
fh.write("Radek\n")
fh.close()
# context manager - pozwala na bezpieczniejsza pracę z plikami
# with - conext manager w pythonie
# dba o zmaknięcie pliku
with open("test.log", "w", encoding="utf-8") as file:
    file.write('Radek\n')
    file.write('Kolejna\n')
    file.write('Jescze jedna\n')
# file.write("")  # ValueError: I/O operation on closed file.

# plik w nadrzędnym katalogu
with open("../test.log", "w", encoding="utf-8") as fh:
    fh.write("Plik w innym miejscu")

# w - jesli plik istnieje zostanie skasowany
with open("../test.log", "w", encoding="utf-8") as fh:
    fh.write("Nadpisane\n")

# x  -gdy plik istnieje otrzymamy błąd
# FileExistsError: [Errno 17] File exists: '../test.log'
# with open("../test.log", "x") as f:
#     f.write("Powitanie\n")
# gdy nie istnieje zostanie utworzony
# with open("../test2.log", "x") as f:
#     f.write("Powitanie\n")

# a - dopisuje na końcu istniejącego pliku
with open("test.log", "a", encoding="utf-8") as file:
    file.write("Dodane\n")
    file.write("Dodane\n")
    file.write("Dodane\n")
    file.write("Dodane\n")
    file.write("Dśćąźodane\n")

with open("test.log", "r", encoding="utf-8") as f:
    lines = f.read()

print(lines)

with open("linie.txt", "w") as f:
    f.write('Pierwsza linia\n')
    f.write('Druga linia\n')
    f.write('Trzecia linia\n')

with open("linie.txt", "r") as fh:
    tekst = fh.read()
print(tekst)
print(repr(tekst))
# 'Pierwsza linia\nDruga linia\nTrzecia linia\n'

print(50 * "-")
with open('linie.txt', "r") as fh:
    linie = fh.readlines()

print(linie)  # ['Pierwsza linia\n', 'Druga linia\n', 'Trzecia linia\n']
print(50 * "-")
print(repr(linie))
# ['Pierwsza linia\n', 'Druga linia\n', 'Trzecia linia\n']
# ['Pierwsza linia\n', 'Druga linia\n', 'Trzecia linia\n']

print(50 * "-")
with open('linie.txt', "r") as f:
    pierwsza_linia = f.readline()
print(pierwsza_linia)  # Pierwsza linia

print(50 * "-")
with open('linie.txt', "r") as file:
    for linia in file:
        print(linia.strip())
# --------------------------------------------------
# Pierwsza linia
# Druga linia
# Trzecia linia

print(50 * "-")
# plik musi istniec
with open("linie.txt", "r+") as f:
    lines = f.readlines()
    f.seek(0)  # wróc na początek pliku
    f.write("Nowa \n")
    f.writelines(lines[1:])  # pozostałe linie
    f.truncate()  # jesli nowa linia ma mniej danych niż dotychczasowa usunie zbędne dane
print(lines)  # ['Pierwsza linia\n', 'Druga linia\n', 'Trzecia linia\n']

print(50 * "-")
# w+ - tworzy nowy plik
# pozwala na odczyt
with open("plik.txt", "w+") as f:
    f.write("Nowa linia\n")
    f.seek(0)  # wraca na początek, bez tego wczyta pusty wiersz
    print(f.read())  # odczyt tego co zapisaliśmy
# Nowa linia
