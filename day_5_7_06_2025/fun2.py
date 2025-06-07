# funkcje zwracające wynik
# muszą być zakończone return

def odejmij(a, b):
    return a - b  # funkcja zwraca wynik


def odejmi2(a=0, b=0, c=0):
    return a - b - c


def oblicz_vat(cena, vat=23):
    return cena * (100 + vat) / 100


print(odejmij(6, 90))  # -84
wynik = odejmij(6, 9)
print("Wynik:", wynik)  # Wynik: -3

print(odejmi2())  # 0
print(odejmi2(5, 6))  # -1
print(odejmi2(5, 6, 4))  # -5
print(odejmi2(b=8, a=9))  # 1
print(odejmi2(1, c=8, b=5))  # -12

print(odejmi2(6, 9) + odejmi2(100, 23, 6))  # 68

print(oblicz_vat(1000))  # 1230.0
print(oblicz_vat(1000, 8))  # 1080.0
print(oblicz_vat(vat=15, cena=1000))  # 1150.0

vat1 = oblicz_vat(1000)
print(type(vat1))  # <class 'float'>
print(vat1)  # 1230.0

if vat1 == 1230:
    print("Działa")  # Działa
