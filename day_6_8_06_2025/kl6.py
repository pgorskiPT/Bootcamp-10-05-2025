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
