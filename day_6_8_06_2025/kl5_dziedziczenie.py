# dziedziczenie
class Pojazd:
    def __init__(self, kolor):
        self.kolor = kolor

    def info(self):
        print(f"Kolor: {self.kolor}")


class Samochod(Pojazd):
    """
    Klasa Samochód, dziedziczy po klasie  Pojazd
    """

    def __init__(self, kolor, marka="Fiat"):
        """
        Metoda inicjalizująca
        :param kolor:
        :param marka:
        """
        super().__init__(kolor)  # obowiązkowo musimy wywołąć konstruktor z klasy wyższej
        self.marka = marka

    def info(self):
        super().info()  # mozęmy wywołąć metodę z klasy wyższej
        print(f"Marka: {self.marka}")


class Rower(Pojazd):
    """
    Klasa Rower, dziedziczy po klasie Pojazd
    """


poj = Pojazd("czerwone")
poj.info()  # Kolor: czerwone

sam = Samochod("Biały")
sam.info()
# Kolor: Biały
# Marka: Fiat
sam2 = Samochod("zielony", "Jaguar")
sam2.info()
# Kolor: zielony
# Marka: Jaguar

rower = Rower("Żółty")
rower.info()  # Kolor: Żółty

lista = [poj, sam, rower]
print(lista)
# [<__main__.Pojazd object at 0x1004bef90>,
# <__main__.Samochod object at 0x1004bf0e0>,
# <__main__.Rower object at 0x1004bf230>]
