# dziedziczenie diamentowe

class A:
    def method(self):
        print("Metoda z klasy A")


class B(A):
    def method(self):
        print("Metoda z klasy B")


class C(A):
    def method(self):
        print("Metoda z kalsy C")


class D(B, C):
    """
    Klqsa dziedziczy
    """


d = D()
d.method()  # Metoda z klasy B

print(D.__mro__)


# class E(A, D):
#     pass
# Traceback (most recent call last):
#   File "/Users/radoslawjaniak/PycharmProjects/Bootcamp-10-05-2025/day_7_14_06_2025/kl8a.py", line 30, in <module>
#     class E(A, D):
#         pass
# TypeError: Cannot create a consistent method resolution order (MRO) for bases A, D
# E A D B C A

class F(D, A):
    pass


print(F.__mro__)
# (<class '__main__.F'>,
# <class '__main__.D'>,
# <class '__main__.B'>,
# <class '__main__.C'>,
# <class '__main__.A'>,
# <class 'object'>)
