# klasa - szablon, przepis
# paradygmaty programowania obiektowego
# enkapsulacja, hermetyzacja, abstrakcja, dziedziczenie, polimorfizm
# obiekt - zbudowany wg przepisu, instancja
# pola - zmienne
# metody - funkcje
# klasa musi być najpierw zadeklarowana
# tworzenie obiektu uruchamia metodę __init__

# deklaracja klasy
# PascalCase
class Human:
    """
    Klasa Human opisujaca człowieka w Pythonie
    """

    imie = ""
    wiek = None
    plec = "k"

    # self - obiekt klasy
    def powitnie(self):
        # print(f"Nazywam się {cz1.imie}")
        print(f"Nazywam się {self.imie}")

    # wypisz_wiek()
    def wypisz_wiek(self):
        print(f"Mam {self.wiek} lat.")


# tworzymy obiekt klasy
cz1 = Human()
print(Human.__doc__)  # Klasa Human opisujaca człowieka w Pythonie

# pydoc -b
# pydoc -w kl1
print(cz1.plec)  #
print(cz1.wiek)  # k
print(cz1.imie)  # None

cz1.plec = "m"
cz1.imie = "Radek"
cz1.wiek = 56
print(cz1.plec)  # m
print(cz1.wiek)  # 56
print(cz1.imie)  # Radek

# stworzyc obiekt klasy Human, przeciwnej płci
cz2 = Human()
cz2.imie = "Anna"
cz2.plec = "k"
cz2.wiek = 34
print(cz2.plec)  # k
print(cz2.wiek)  # 34
print(cz2.imie)  # Anna

cz1.powitnie()
cz2.powitnie()
# Nazywam się Radek
# Nazywam się Anna
cz1.wypisz_wiek()
cz2.wypisz_wiek()
# Mam 56 lat.
# Mam 34 lat.
