class Pojazd:
    def serwis(self):
        print("Serwisowanie pojazdu")


class SamochodOsobowy(Pojazd):
    def serwis(self):
        print("Serwisowanie samochodu osobowego")


class SamochodDostawczy(Pojazd):
    def serwis(self):
        print("Serwis samochodu dostawczego")


class PojazdSluzbowy(Pojazd):
    def rejestracja_sluzbowa(self):
        print("Rejestracja pojazdu służbowego")


class SamochodSluzbowyOsobowy(SamochodOsobowy, PojazdSluzbowy):
    pass


car1 = SamochodSluzbowyOsobowy()
car1.serwis()
car1.rejestracja_sluzbowa()
# Serwisowanie samochodu osobowego
# Rejestracja pojazdu służbowego
