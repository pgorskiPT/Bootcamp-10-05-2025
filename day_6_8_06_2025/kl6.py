# stworzyc klasę Pracownik
# imie, nazwisko, pensja
# przedstaw_sie(), oblicz_pensje()
# Zrobić kalsę Manager dziedziczącą po Pracownik
# zastanowić sie co może dziedziczyć a co musi nadpisać ta klasa

class Pracownik:

    def __init__(self, imie, nazwisko, pensja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pensja = pensja

    def przedstaw_sie(self):
        print(f"Cześć, jestem {self.imie} {self.nazwisko}")

    def oblicz_penja(self):
        return self.pensja


class Manager(Pracownik):
    """
    Klasa Manaer
    """

    def __init__(self, imie, nazwisko, pensja, premia):
        super().__init__(imie, nazwisko, pensja)  # uruchomienie konstruktora z klasy wyższej (Pracownik)
        self.premia = premia

    def oblicz_penja(self):
        return self.pensja + self.premia

    pracownik = Pracownik("Jan", "Kowalski", 8000)
    pracownik.przedstaw_sie()
    wynagrodzenie_pracownika = pracownik.oblicz_penja()
    print(f"Wynagrodzenie dla pracownika {pracownik.imie} {pracownik.nazwisko}: {wynagrodzenie_pracownika}")


# Cześć, jestem Jan Kowalski
# Wynagrodzenie dla pracownika Jan Kowalski: 8000

manago = Manager("Anna", "Nowak", 12000, 3000)
manago.przedstaw_sie()
wynagrodzenie_manago = manago.oblicz_penja()
print(f"Wynagrodzenie dla managera {manago.imie} {manago.nazwisko}: {wynagrodzenie_manago}")
# Cześć, jestem Anna Nowak
# Wynagrodzenie dla managera Anna Nowak: 15000
