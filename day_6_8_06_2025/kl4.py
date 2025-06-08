# napisać klasę Dom
# ma posiadać pola prywatne kolor, liczba_okien, metraz
# dodac metody do odczytu i zapisu tych pól
# dodać metodę prywatną __farba() - > zabrakło farby
class Dom:
    """
    Klasa opisująca Dom
    """

    def __init__(self, metraz, kolor, liczba_okien):
        self.__metraz = metraz
        self.__kolor = kolor
        self.__liczba_okien = liczba_okien

    def wyswietl_okna(self):
        print(f"Mam {self.__liczba_okien} okna/okien")

    def wyswietl_kolor(self):
        print(f"Mam {self.__kolor} kolor")

    def wyswietl_metraz(self):
        print(f"Mam {self.__metraz} m2 powierzchni")

    def zmien_okna(self):
        odp = int(input("Podaj liczbę okien"))
        self.__liczba_okien = odp
        self.wyswietl_okna()

    def zmien_kolor(self):
        odp = input("Podaj kolor")
        self.__kolor = odp
        self.wyswietl_kolor()
        self.__farba()

    def zmien_metraz(self):
        odp = int(input("Podaj metraz"))
        self.__metraz = odp
        self.wyswietl_metraz()

    def __farba(self):
        print("Zabrakło farby")


dom = Dom(200, "biały", 15)
dom.wyswietl_metraz()  # Mam 200 m2 powierzcni
dom.wyswietl_kolor()  # Mam biały kolor
dom.wyswietl_okna()  # Mam 15 okna/okien

dom.zmien_kolor()
# Podaj kolorczerwony
# Mam czerwony kolor
# Zabrakło farby
dom.zmien_okna()
dom.zmien_metraz()
# Podaj kolorczerwony
# Mam czerwony kolor
# Zabrakło farby
# Podaj liczbę okien14
# Mam 14 okna/okien
# Podaj metraz234
# Mam 234 m2 powierzchni
