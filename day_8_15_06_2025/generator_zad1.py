# generatory - generuje wartość dla danego argumentu
import time


def kwadrat(n):
    for x in range(n):
        print(x ** 2)


kwadrat(5)


def kwadrat2(n):
    for x in range(n):
        yield x ** 2  # zwraca wynik, zapamiętuje aktualny stan, kolejne wywołania zwracają kolejny wynik


kwa = kwadrat2(5)
print(kwa)  # <generator object kwadrat2 at 0x100d1aa80>
print(next(kwa))  # 0
print(next(kwa))  # 1
print(next(kwa))  # 4

print("Zrób cokolwiek")
lista = []
lista.append("123456")
print(lista)
# Zrób cokolwiek
# ['123456']

print(next(kwa))  # 9
print(next(kwa))  # 16

# print(next(kwa))  # StopIteration - gdy wyczerpiemy dane z generatora

kwa2 = kwadrat2(10)
kwa3 = kwadrat2(20)

print(next(kwa2))  # 0
print(next(kwa3))  # 0
print(next(kwa2))  # 1
print(next(kwa3))  # 1
print(next(kwa2))  # 4

print(list(kwa3))
# [4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361]

for i in kwadrat2(10):
    print(i)
    time.sleep(1)  # symuluje długotrwałe zadanie
