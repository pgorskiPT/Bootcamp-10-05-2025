class Human:
    """
    Klasa Human opisująca człowieka w pythonie
    """

    def __init__(self, imie, wiek, wzrost, plec="k"):
        """
        Metoda inicjalizująca (konstruktor)
        :param imie:
        :param wiek:
        :param wzrost:
        :param plec:
        """

        self.imie = imie
        self.wiek = wiek
        self.wzrost = wzrost
        self.plec = plec

    def powitnie(self):
        # print(f"Nazywam się {cz1.imie}")
        print(f"Nazywam się {self.imie}")

    # wypisz_wiek()
    def wypisz_wiek(self):
        print(f"Mam {self.wiek} lat.")

    def ruszaj(self):

        if self.plec == "m":
            print("Ruszyłem w drogę")
        elif self.plec == "k":
            print("Ruszyłam w drogę")


# cz1 = Human()  # TypeError: Human.__init__() missing 3 required positional arguments: 'imie', 'wiek', and 'wzrost'
cz1 = Human("Radek", 56, 189, "m")
print(cz1.imie)  # Radek
print(cz1.wiek)  # 56
print(cz1.wzrost)  # 189
print(cz1.plec)  # m
cz1.wypisz_wiek()
cz1.powitnie()
# Mam 56 lat.
# Nazywam się Radek
print(cz1.__doc__)  # Klasa Human opisująca człowieka w pythonie

cz2 = Human("Ania", 32, 156)
print(cz2.imie)  # Ania
print(cz2.wiek)  # 32
print(cz2.wzrost)  # 156
print(cz2.plec)  # k

cz1.ruszaj()
cz2.ruszaj()
# Ruszyłem w drogę
# Ruszyłam w drogę
