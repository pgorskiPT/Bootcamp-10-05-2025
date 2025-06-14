# dziedziczenie po wielu klasach

class A:
    def method(self):
        print("Metoda z klasy A")


class B:
    def method(self):
        print("Metoda z kalsy B")


a = A()
a.method()  # Metoda z klasy A

b = B()
b.method()  # Metoda z kalsy B


class C(B, A):
    """
    Klasa C dziedziczy po dwóch klasach
    """


c = C()
c.method()  # Metoda z kalsy B

# kolejnośc rozwiązywania nazw metod
print(C.__mro__)


# (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)

class D(A, B):
    """
    Klasa dziedziczy po A i B
    """


d = D()
d.method()  # Metoda z klasy A
print(D.__mro__)


# (<class '__main__.D'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)

class E(A, B):
    def method(self):
        print("Metoda z klasy E")


e = E()
e.method()  # Metoda z klasy E


class F(B, A):
    """
    Klasa dziedziczy po kalsie B i A
    """

    def method(self):
        A.method(self)  # jawnie wskazane użycie metody z klasy A


f = F()
f.method()  # Metoda z klasy A


class G(A, B):
    """
    Dziedziczy po A i B
    """

    def method(self):
        super().method()  # super() - użycie klasy nadrzędnej
        print("Dopisane")


g = G()
g.method()


# Metoda z klasy A
# Dopisane

class H(A, B):

    def method(self):
        B.method(self) # jawne wywołanie
        super().method() # A
        print("Dopisane w klasie H")


h = H()
h.method()
# Metoda z kalsy B
# Metoda z klasy A
# Dopisane w klasie H
print(H.__mro__)
# (<class '__main__.H'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
