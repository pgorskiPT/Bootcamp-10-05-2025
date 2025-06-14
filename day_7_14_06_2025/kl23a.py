class MyNumber:
    def __init__(self, value):
        self.value = value


num1 = MyNumber(5)
num2 = MyNumber(15)

print(5 < 15)  # True
# print(num1 < num2)
# TypeError: '<' not supported between instances of 'MyNumber' and 'MyNumber'
print(num1.value < num2.value)  # True


class MyNumber2:
    def __init__(self, value):
        self.value = value

    # ta metoda wykona się przy porównaniu "<"
    def __lt__(self, other):
        return self.value < other.value

    # wykona się dla "==
    def __eq__(self, other):
        return self.value == other.value


num3 = MyNumber2(5)
num4 = MyNumber2(15)
print(num3 < num4)  # True

num5 = MyNumber2(15)
print(num4 == num5)  # False - porównał referencje
# Po nadpisaniu metody __eq__ be∂zie prawidłowe porównanie
print(num4 == num5)  # True
