class MyClass:
    counter = 0

    @classmethod
    def increment_counter(cls):
        cls.counter += 1
        return cls.counter


print(MyClass.increment_counter())
print(MyClass.increment_counter())
print(MyClass.increment_counter())
c = MyClass()
print(c.counter)  # 3
print(c.increment_counter())  # 4
c.counter = 0  # nadpiszemy
print(c.counter)  # 0
c.increment_counter()
print(c.counter)
print(MyClass.counter)  # 5

c2 = MyClass()
print(c2.increment_counter())  # 6


class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    @classmethod
    def z_nazwy_pelnej(cls, nazwa_pelna):
        imie, nazwisko = nazwa_pelna.split()
        return cls(imie, nazwisko)


osoba1 = Osoba("Jan", "Kowalski")
print(osoba1.imie, osoba1.nazwisko)
# Jan Kowalski
print("Jan Kowalski".split())  # ['Jan', 'Kowalski'] standardowo dzieli spacja
imie, nazwisko = "Jan Kowalski".split()
print(imie, ":", nazwisko)  # Jan : Kowalski
print(" Jan : Kowalski".split(":"))  # [' Jan ', ' Kowalski']

osoba2 = Osoba(imie, nazwisko)
print(f"{osoba2.imie}, {osoba2.nazwisko}")  # Jan, Kowalski

osoba3 = Osoba.z_nazwy_pelnej("Anna Nowak")
print(f"{osoba3.imie}, {osoba3.nazwisko}")  # Anna, Nowak
