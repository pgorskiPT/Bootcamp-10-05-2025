import math


class MyFirstClass:
    """
    Klasa w Pythonie opisująca punkty w przestrzeni x i y
    """

    def __init__(self, x=0, y=0):
        """
        Metod ainicjalizująca
        :param x: położeniee punktu na osi x
        :param y:
        """
        # self.x = x
        # self.y = y
        self.move(x, y)

    def move(self, x: float, y: float) -> None:
        """
        Metoda przesuwa punkt we wskazane miejsce
        :param x: nowe x punktu
        :param y: nowe y punktu
        :return: None
        """
        self.x = x
        self.y = y

    def reset(self):
        self.move(0, 0)

    # math.hypot()
    def calculate(self, other: "MyFirstClass") -> float:
        """
        Metoda zwraca odległość punktów w przestrzeni euklidesowej
        :param other:
        :return:
        """
        return math.hypot(self.x - other.x, self.y - other.y)

    # opisuje obiekt w przypadku użycia na obiekcie print()
    def __str__(self):
        return f"({self.x, self.y})"

    # reprezentacja obiektu
    def __repr__(self):
        return f"Point({self.x, self.y}"


ob = MyFirstClass()
print(ob)  # <__main__.MyFirstClass object at 0x102c430e0>
# po nadpisaniu metody __str__
# ((0, 0))
print(ob.x)  # 0
print(ob.y)  # 0

ob2 = MyFirstClass(59, 34)
print(ob2)  # ((59, 34))

ob.move(23, 89)
print(ob.calculate(ob2))  # 65.73431371817918
print(ob2.calculate(ob))  # 65.73431371817918
# ob.calculate("a") # AttributeError: 'str' object has no attribute 'x'

ob.reset()
print(ob)  # ((0, 0))
print(ob2)  # ((59, 34))
print(ob.calculate(ob2))  # 68.09552114493287

lista_ob = [ob, ob2]
print(lista_ob)
# [<__main__.MyFirstClass object at 0x102b0b0e0>, <__main__.MyFirstClass object at 0x102c44f50>]
# Po dopisaniu metody __repr__
# [Point((0, 0), Point((59, 34)]
