# zasięg zmiennych

a = 10
b = 10


def dodaj():
    a = 6  # argumenty lokalne
    b = 8
    print(a + b)


def dodaj2():
    print(a + b)  # uzyje wartości globalnych


def dodaj3():
    global a  # użyj zmiennej globalnej
    a = 5  # zamieni wartość zmiennej globalnej a
    b = 67
    print(a + b)


print(f"Zmienne a i b z góry {a=}, {b=}")  # Zmienne a i b z góry a=10, b=10
dodaj()  # 14
print(f"Zmienne a i b z góry {a=}, {b=}")  # Zmienne a i b z góry a=10, b=10
dodaj2()  # 20
print(f"Zmienne a i b z góry {a=}, {b=}")  # Zmienne a i b z góry a=10, b=10
# a=5
dodaj3()  # 72
print(f"Zmienne a i b z góry {a=}, {b=}")  # Zmienne a i b z góry a=5, b=10
dodaj2()  # 15
