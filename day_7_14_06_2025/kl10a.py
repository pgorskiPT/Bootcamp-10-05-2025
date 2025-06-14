from abc import ABC, abstractmethod


# klasa abstrakcyjna
# nie można stworzyc obiektu tej klasy
class Counter(ABC):
    def __init__(self, values=0):
        self.values = values

    def increment(self, by=1):
        self.values += by  # values = values + by

    @abstractmethod
    def drukuj(self):
        pass

    @classmethod
    def from_counter(cls, counter):
        # Counter(bc.values)
        # zwracamy obiekt klasy
        return cls(counter.values)

    @staticmethod
    def from_string():
        print("Metoda statyczna")


# TypeError: Can't instantiate abstract class Counter without an implementation for abstract method 'drukuj'
# c1 = Counter()

class NewCounter(Counter):
    """
    Licznik bez metody drukuj
    """


# TypeError: Can't instantiate abstract class NewCounter without an implementation for abstract method 'drukuj'
# nc = NewCounter()

class BoundedCounter(Counter):
    """
    Klasa musi nadpisac metodę drukuj()
    """

    MAX = 100

    def __init__(self, values=0):
        if values > self.MAX:
            raise ValueError(f"Wartość nie może byc większa od {self.MAX}")
        super().__init__(values)

    def drukuj(self):
        print("Drukuj...", self.values)


bc = BoundedCounter()
bc.drukuj()  # Drukuj... 0
bc.increment()
bc.drukuj()  # Drukuj... 1
bc.increment(5)
bc.drukuj()  # Drukuj... 6

# bc2 = BoundedCounter(101) # ValueError: Wartość nie może byc większa od 100

bc2 = BoundedCounter(bc.values)
bc2.drukuj()  # Drukuj... 6

bc3 = BoundedCounter.from_counter(bc)
bc3.drukuj()  # Drukuj... 6
bc4 = bc2.from_counter(bc3)
bc4.drukuj()  # Drukuj... 6

# użycie metody statyznej
# nie tworzy obiektu
# wywołujemy bezpośrednio na klasie
# nie potrzebujemy obiektu
Counter.from_string()
# Metoda statyczna
