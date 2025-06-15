class Person:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        """Getter - umożliwia czytanie .name"""
        print("Pobieram imię")
        return self.__name

    @name.setter
    def name(self, value):
        """Setter - umożliwia ustawianie .name"""
        if not isinstance(value, str):
            raise ValueError("To musi być string")
        print("Ustawiam imię")
        self.__name = value

    @name.deleter
    def name(self):
        """Deleter - kasowane atrybutu"""
        print("Usuwam imię")
        del self.__name


p = Person("Alicja")
print(p.name)
# pobieram imię
# Alicja

p.name = "Janek"
print(p.name)
# Pobieram imię
# Janek

# p.name = 123  # ValueError: To musi być string

del p.name  # usunie pole z obiektu
# print(p.name) # AttributeError: 'Person' object has no attribute '_Person__name'
