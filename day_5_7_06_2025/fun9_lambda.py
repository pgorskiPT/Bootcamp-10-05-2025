# funkcja lambda
# skrócony zapis funkcji
# lambda zwraca wynik - return
# funkcja anonimowa - deklaracja w miejscu wykonania
from math import lgamma

odejmij = lambda a, b: a - b  # return
print(odejmij(6, 8))  # -2
print(odejmij(b=8, a=87))  # 79

addition = lambda a, b: a + b
print(addition(6, 7))  # 13
res = addition(7, 8)
print(f"Wynik dodawania {res}")  # Wynik dodawania 15

res = lambda *args: sum(args)
print(res(10, 20))  # 30

res = lambda **kwargs: sum(kwargs.values())
print(res(a=10, b=20))  # 30

product = lambda a, b: a * b
print(product(4, 5))  # 20


def product1(nums):
    total = 1
    for i in nums:
        total *= i
    return total


res1 = lambda **kwargs: product1(kwargs.values())
print(res1(a=10, b=90))  # 900


def my_func(n):
    return lambda a: a + n


add10 = my_func(10)
add20 = my_func(20)
add30 = my_func(30)

print(add10(5))  # 15
print(add20(5))  # 25
print(add30(5))  # 35

oblicz_vat = lambda cena, vat=23: cena * (100 + vat) / 100
print(oblicz_vat(1000))
print(oblicz_vat(1000, 8))

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosły")
print(wiek(9))  # dziecko
print(wiek(10))  # nastolatek
print(wiek(17))  # nastolatek
print(wiek(18))  # dorosły
print(wiek(25))  # dorosły

# mapowanie - zmiana danych
lista = [1, 2, 3, 45, 67, 78, 100, 200, 300]

lista_wyn = []
for i in lista:
    lista_wyn.append(i * 2)
print(lista_wyn)  # [2, 4, 6, 90, 134, 156, 200, 400, 600]

print([i * 2 for i in lista])  # [2, 4, 6, 90, 134, 156, 200, 400, 600]


def zmien(x):
    return x * 2


lista_wyn_f = []
for i in lista:
    lista_wyn_f.append(zmien(i))
print(lista_wyn_f)  # [2, 4, 6, 90, 134, 156, 200, 400, 600]

# funkcje wyższego rzędu
# map() - mapowanie, zmienia dane wg zadanej funkcji
print(f"Zastosowanie map(): {list(map(zmien, lista))}")  # Zastosowanie map(): [2, 4, 6, 90, 134, 156, 200, 400, 600]

# Lambda jako funkcja anonimowa - nie posiada nazwy
# uzycie w miejscu deklaracji
print(f"Zastosowanie map(): {list(map(lambda x: x * 2, lista))}")
# Zastosowanie map(): [2, 4, 6, 90, 134, 156, 200, 400, 600]
print(f"Zastosowanie map(): {list(map(lambda x: x * 4, lista))}")
# Zastosowanie map(): [4, 8, 12, 180, 268, 312, 400, 800, 1200]
print(f"Zastosowanie map(): {list(map(lambda x: x * 3.67, lista))}")
# Zastosowanie map(): [3.67, 7.34, 11.01, 165.15, 245.89, 286.26, 367.0, 734.0, 1101.0]

# filtrowanie danych
# wyciagniecie elemntów spełniających warunek

lista_parzyste = []
for i in lista:
    if i % 2 == 0:
        lista_parzyste.append(i)

print(lista_parzyste)

# filter()
print(f"Zastosowanie filter(): {list(filter(lambda x: x < 3, lista))}")  # Zastosowanie filter(): [1, 2]
print(f"Zastosowanie filter(): {list(filter(lambda x: x > 15, lista))}")
# Zastosowanie filter(): [45, 67, 78, 100, 200, 300]
# x > 5 i x < 200
print(f"Zastosowanie filter(): {list(filter(lambda x: x > 5 and x < 200, lista))}")
# Zastosowanie filter(): [45, 67, 78, 100]
print(f"Zastosowanie filter(): {list(filter(lambda x: 5 < x < 200, lista))}")
# Zastosowanie filter(): [45, 67, 78, 100]
print(f"Zastosowanie filter(): {list(filter(lambda x: x % 2 == 0, lista))}")
# Zastosowanie filter(): [2, 78, 100, 200, 300]

list3 = ['one', 'TWO', 'three', "FOUR"]
print(f"Filter: {list(filter(lambda x: x.isupper(), list3))}")  # Filter: ['TWO', 'FOUR']
print(f"Filter: {list(filter(lambda x: x.islower(), list3))}")  # Filter: ['one', 'three']

list4 = ['one', 'two2', 'three3', '88', '99', '102', '1.23']
numeric = list(filter(lambda x: x.isnumeric(), list4))
print(f"Numeric: {numeric}")  # Numeric: ['88', '99', '102']

alpha = list(filter(lambda x: x.isalpha(), list4))
print(f"Alpha: {alpha}")  # Alpha: ['one']

alphanum = list(filter(lambda x: x.isalnum(), list4))
print(f"Alphanumeric: {alphanum}")  # Alphanumeric: ['one', 'two2', 'three3', '88', '99', '102']

mix = list(filter(lambda x: x.isnumeric() and not x.isalpha(), list4))
print(f"Mix: {mix}")  # Mix: ['88', '99', '102']
# przerwa 13:35
