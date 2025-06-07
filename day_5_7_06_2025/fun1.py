# funkcje - wydzielony fragment programu, który można wykonac w dowolnym momencie
# funkcja musi być zadeklarowana przed użyciem
# w miejscu definicji (deklaracji) funkcję się nie wykonuje
# aby uruchomić funkcję należy ją wywołać
a = 8
b = 6


# PEP8 zaleca by ciało funkcji oddzielać dwoma linijkami od ciała programu
# deklaracja (definicja) funkcji
def dodaj():
    print(a + b)


print(dodaj)  # <function dodaj at 0x1029cf7e0> adres funkcji
print(type(dodaj))  # <function dodaj at 0x1029cf7e0>
# jesli zmienna przechowuje adres funkcji
# można wykonać funkcję z tego adresu
# nazwa funkcji i ()
dodaj()  # uruchomienie funkcji, 14
