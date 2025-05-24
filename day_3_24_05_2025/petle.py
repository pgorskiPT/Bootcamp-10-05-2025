# pętla - możliwośź wykonannia tego samego fragmentu kodu wielokrotnie
# for - pętla iteracyjna
import random
from itertools import zip_longest

for i in range(10):  # od 0 do 9
    print(i)

for i in range(10):
    print(i, i, sep=":")  # 1:1
    print(i, i)  # 4 4
#  sep
#         string inserted between values, default a space.
#       end
#         string appended after the last value, default a newline.

for i in range(10):
    print(i, end="")  # pusty znak końca linii, 0123456789 wszystko w jednej linii bo ie zmienia na nową

print()
print("Koniec pętli, nowa linia")
# 0123456789
# Koniec pętli, nowa linia

for i in range(1, 20):  # od 1 do 19
    print(i)

# Gdy wartośc zmiennej nie jest nam potrzeban, lub jest nieistotna możemy użyc niemej zmiennej
for i in range(5):
    print("komunikat")

for _ in range(1, 5):  # _ niema zmienna
    print("Komunikat")
    # print(_) # to jest poprawna nazwa zmiennej, przyjmie wartość

my_string = "Radek"
for i in my_string:  # itracja po kolekcji, działa aż dojdzie do ostatniego elementu
    print(i)

for i in range(len(my_string)):
    print(my_string[i])

print(30 * "-")
# przerobic lotto na pętle
lista_wynik = []
lista_kule = list(range(1, 50))
for _ in range(6):
    wyn = random.choice(lista_kule)  # losuje jeden element
    # print(wyn)
    lista_wynik.append(wyn)
    lista_kule.remove(wyn)

print(lista_wynik)  # [13, 35, 44, 48, 25, 46]
lista_wynik.sort()
print("Posrtowany wynik:", lista_wynik)  # Posrtowany wynik: [3, 11, 23, 32, 46, 48]

for i in range(10):
    if i % 2 == 0:  # % modulo, reszta z dzielenia
        print(i, "parzysta")
# 0 parzysta
# 2 parzysta
# 4 parzysta
# 6 parzysta
# 8 parzysta

# list comprehensions
list3 = [j for j in range(1, 10) if j % 2 == 0]
print(list3)  # [2, 4, 6, 8]

for c in list3:
    if c == 2:
        c += 1  # c = c + 1
        print("Tylko jeśli c=2")
    print('Przy każdym przejsciu pętli', c)
# Tylko jeśli c=2
# Przy każdym przejsciu pętli 3
# Przy każdym przejsciu pętli 4
# Przy każdym przejsciu pętli 6
# Przy każdym przejsciu pętli 8

imiona = ['Radek', "Tomek", 'Zenek', "Zbyszek"]
for p in imiona:
    print(p)
# Radek
# Tomek
# Zenek
# Zbyszek

# 0 Radek
for i in range(len(imiona)):  # range(4) 0 do 3
    print(i, imiona[i])

for p in imiona:
    print(imiona.index(p), p)
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Zbyszek

# enumerate() - numeruje kolekcje i zwraca indeks i element kolekcji
for i in enumerate(imiona):
    print(i)
# (0, 'Radek')
# (1, 'Tomek')
# (2, 'Zenek')
# (3, 'Zbyszek')
a, b = (3, 'Zbyszek')  # rozpakowanie krotki
print(a, b)

for i, o in enumerate(imiona):
    print(i, o)
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Zbyszek

for i, o in enumerate(imiona, start=1):  # numeruje od 1
    print(i, o)
# 1 Radek
# 2 Tomek
# 3 Zenek
# 4 Zbyszek

ludzie = ['Janek', "Radek", "Tomek", "Marek"]
wiek = [45, 40, 18, 23]

# Radek 40
for i in range(len(ludzie)):
    print(ludzie[i], wiek[i])
    # Janek 45
    # Radek 40
    # Tomek 18
    # Marek 23

ludzie = ['Janek', "Radek", "Tomek", "Marek", "Ania"]
wiek = [45, 40, 18, 23]

# for i in range(len(ludzie)):
#     print(ludzie[i], wiek[i])  # IndexError: list index out of range

# zip() - łaczy kolekcje
for i in zip(ludzie, wiek):
    print(i)
# ('Janek', 45)
# ('Radek', 40)
# ('Tomek', 18)
# ('Marek', 23)
for l, w in zip(ludzie, wiek):
    print(l, w)
# Janek 45
# Radek 40
# Tomek 18
# Marek 23

# 0 Radek 40
for i in enumerate(zip(ludzie, wiek)):
    print(i)
    # (0, ('Janek', 45))
    # (1, ('Radek', 40))
    # (2, ('Tomek', 18))
    # (3, ('Marek', 23))
a, b = (3, ('Marek', 23))
print(a, b)  # 3 ('Marek', 23)
c, d = ('Marek', 23)
print(c, d)  # Marek 23
print(a, c, d)  # 3 Marek 23
a, (c, d) = (3, ('Marek', 23))  # musimy jawnie wskazać wewnętrzną krotkę
for i, (o, w) in enumerate(zip(ludzie, wiek)):
    print(f"Numer: {i}, Imię: {o}, Wiek: {w}")
# Numer: 0, Imię: Janek, Wiek: 45
# Numer: 1, Imię: Radek, Wiek: 40
# Numer: 2, Imię: Tomek, Wiek: 18
# Numer: 3, Imię: Marek, Wiek: 23

zipped = zip_longest(ludzie, wiek, fillvalue="NONE")
print(zipped)  # <itertools.zip_longest object at 0x102702110>  # iterator
print(type(zipped))  # <class 'itertools.zip_longest'>
# iterator - pozwala sekwencyjnie odczytywac dane
for i in zipped:
    print(i)
# ('Janek', 45)
# ('Radek', 40)
# ('Tomek', 18)
# ('Marek', 23)
# ('Ania', 'NONE')

print("-" * 30)
# nic nie wyświetli
# mozna tylko raz odczytac dane
for o, w in zipped:
    print(o, w)

print("-" * 30)
zipped = zip_longest(ludzie, wiek, fillvalue="NONE")
zipped_tuple = tuple(zipped)
print(zipped_tuple)  # (('Janek', 45), ('Radek', 40), ('Tomek', 18), ('Marek', 23), ('Ania', 'NONE'))
for o, w in zipped_tuple:
    print(o, w)

print("*" * 30)
for o, w in zipped_tuple:
    print(o, w)
# ------------------------------
# ------------------------------
# (('Janek', 45), ('Radek', 40), ('Tomek', 18), ('Marek', 23), ('Ania', 'NONE'))
# Janek 45
# Radek 40
# Tomek 18
# Marek 23
# Ania NONE
# ******************************
# Janek 45
# Radek 40
# Tomek 18
# Marek 23
# Ania NONE

for i in range(0, 10, 2):  # (start, stop, krok)
    print(i)

for i in range(-10, 0, 2):
    print(i)

for i in range(10, 0, -2):  # krok ujemny
    print(i)

parzyste = [i for i in range(0, 10, 2)]
print(parzyste)  # [0, 2, 4, 6, 8]

ang_pol: dict[str, str] = {'name': 'imie', "cat": "kot", 'water': "woda"}
# dodane popowiedzi typów - to nie jest deklaracja typów
# stworzyć słownik pol-ang
pol_ang = {}
print(ang_pol.items())
# dict_items([('name', 'imie'), ('cat', 'kot'), ('water', 'woda')])
for k, v in ang_pol.items():
    pol_ang[v] = k
print(pol_ang)  # {'imie': 'name', 'kot': 'cat', 'woda': 'water'}

# to działą tak samo
print({v: k for k, v in ang_pol.items()})
# {'imie': 'name', 'kot': 'cat', 'woda': 'water'}
