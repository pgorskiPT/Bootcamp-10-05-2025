# dziedziczenie wielopoziomowe

class Animal:

    def __init__(self, name):
        self.name = name

    def info(self):
        print(f"Imię: {self.name}")


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def info(self):
        super().info()
        print(f"Kolor: {self.color}")


class Tiger(Cat):
    def __init__(self, name, color, liczba_paskow):
        super().__init__(name, color)
        self.liczba_paskow = liczba_paskow

    def info(self):
        super().info()
        print(f"Liczba pasków: {self.liczba_paskow}")


animal = Animal("Bezimienny")
animal.info()
# Imię: Bezimienny

cat1 = Cat("Fielmon", "Biały w ciapy")
cat1.info()
# Imię: Fielmon
# Kolor: Biały w ciapy

tiger1 = Tiger("Tygrysek", "Pomarańczowy", 15)
tiger1.info()
# Imię: Tygrysek
# Kolor: Pomarańczowy
# Liczba pasków: 15
