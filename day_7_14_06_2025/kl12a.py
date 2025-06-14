class Matematyka:

    @staticmethod
    def dodaj(a, b):
        return a + b

    @staticmethod
    def odejmij(a, b):
        return a - b


wynik = Matematyka.dodaj(5, 6)
print(wynik)  # 11

wynik = Matematyka.odejmij(65, 89)
print(wynik)  # -24
