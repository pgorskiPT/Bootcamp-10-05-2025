from abc import ABC, abstractmethod


# klasa abstrakcyjna to jest taka klasa, która posiada metodę abstrakcyjną
# metoda abstrakcyjna - metoda, która ni eposiada ciała
# nie mozna tworzyć  obiektów klasy abstrakcyjnej
# TypeError: Can't instantiate abstract class Ptak without an implementation for abstract method 'wydaj_odglos'
class Ptak(ABC):
    """
    Klasa opisująca ptaka w Pythonie
    """

    def __init__(self, gatunek, szybkosc):
        """
        Metoda inicjalizujaca
        :param gatunek:
        :param szybkosc:
        """
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "Lecę z szybkością", self.szybkosc)

    # metoda abstrakcyjna
    @abstractmethod
    def wydaj_odglos(self):
        pass


class Kura(Ptak):
    """
    Klasa Kura
    """

    def __init__(self, gatunek):
        super().__init__(gatunek, 0)

    def latam(self):
        print("Tu", self.gatunek, "Ja nie latam.")

    def wydaj_odglos(self):
        print("Ko ko ko ko")

    def dziobanie(self):
        print("Tu", self.gatunek, "Idę sobie podziobać")


class Orzel(Ptak):
    """
    Klasa Orzel dziedziczy po Ptak
    """

    def wydaj_odglos(self):
        print("Kier kir kier")

    def polowanie(self):
        print("Tu", self.gatunek, "Rozpoczynam polowanie")


# TypeError: Can't instantiate abstract class Sowa without an implementation for abstract method 'wydaj_odglos'
class Sowa(Ptak):
    """
    Klasa Sowa dziedziczy po klasie Ptak
    """


# TypeError: Can't instantiate abstract class Ptak without an implementation for abstract method 'wydaj_odglos'
# or1 = Ptak("Orzeł", 45)
# or1.latam()  # Tu Orzeł Lecę z szybkością 45
# kur1 = Ptak("Kura", 0)
# kur1.latam()  # Tu Kura Lecę z szybkością 0
# kur1.wydaj_odglos()

kur2 = Kura("Kura")
kur2.latam()  # Tu Kura Ja nie latam.
kur2.wydaj_odglos()  # Ko ko ko ko
or2 = Orzel("Bielik", 50)
or2.wydaj_odglos()
or2.latam()
# Kier kir kier
# Tu Bielik Lecę z szybkością 50

# TypeError: Can't instantiate abstract class Sowa without an implementation for abstract method 'wydaj_odglos'
# sowa = Sowa("Sowa", 20)

or2.polowanie()  # Tu Bielik Rozpoczynam polowanie
# kur2.polowanie() # AttributeError: 'Kura' object has no attribute 'polowanie'
kur2.dziobanie()  # Tu Kura Idę sobie podziobać

# polimorfizm - obiekty różnych klas mają wspólne cechy
# kalsa abstrakcyjna mocniej akcentuje ten wspólny trzon
lista = [or2, kur2]
for i in lista:
    print(i.__class__.__name__)
    i.wydaj_odglos()
# Orzel
# Kier kir kier
# Kura
# Ko ko ko ko
