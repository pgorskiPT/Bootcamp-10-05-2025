# funkcje - wydzielony fragment programu, który można wykonac w dowolnym momencie
# funkcja musi być zadeklarowana przed użyciem
# w miejscu definicji (deklaracji) funkcję się nie wykonuje
# aby uruchomić funkcję należy ją wywołać
a = 8
b = 6


# funkjce niezwracające wyniku
# PEP8 zaleca by ciało funkcji oddzielać dwoma linijkami od ciała programu
# deklaracja (definicja) funkcji
def dodaj():
    print(a + b)  # przyjeła argumenty z globalnego scope


# funkcja z argumentami a i b
def dodaj2(a, b):
    # a i b to są zmienne lokalne tej funkcji
    # musimy obowiązkowo przekazac dwa argumenty
    print(a + b)
    c = 7  # to jest tylko argumnt lokalny wewnątrz zmiennej


# c=0 - argument o wartości domyślnej
def odejmij(a, b, c=0):
    print(a - b - c)


print(dodaj)  # <function dodaj at 0x1029cf7e0> adres funkcji
print(type(dodaj))  # <function dodaj at 0x1029cf7e0>
# jesli zmienna przechowuje adres funkcji
# można wykonać funkcję z tego adresu
# nazwa funkcji i ()
dodaj()  # uruchomienie funkcji, 14
# dodaj2()  # TypeError: dodaj2() missing 2 required positional arguments: 'a' and 'b'

# argumenty pozycyjne, po kolei trafia do kolejnych argumntów w funkcji
# dla funkcji dodaj2() musimy obowiązkowo przekazać dwa argumenty
dodaj2(10, 65)  # 75
# print(c) # NameError: name 'c' is not defined, to jest tylko lokalne wewnątrz funkcji dodaj2()

# funkcja odejmij ma argument domyślny
# pozwala to ominąć brak możliwosći przeciążania funkcji liczbą argumentów
odejmij(1, 2)  # -1
odejmij(1, 2, 3)  # -4

# argumenty przekazane po nazwie
odejmij(c=9, b=8, a=65)  # 48
odejmij(b=67, a=34)  # -33
dodaj2(b=98, a=54)  # 152

# mieszane
odejmij(1, c=90, b=87)  # -176
odejmij(1, b=76)  # -75

# SyntaxError: positional argument follows keyword argument
# argumenty nazwane muszą być po pozycyjnych
# odejmij(c=90, 3, 4)

print(10 * "-")
print(dodaj())
# ----------
# 14
# None
print(print(a + b))  # None

# print(dodaj() + dodaj())  # TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
