# liczby float
# bład zaokrąglenia
# print(0.2 + 0.8)  # 1.0
# print(0.2 + 0.7)  # 0.8999999999999999
# print(0.1 + 0.2)  # 0.30000000000000004
# zapamietuje w postaci wykładniczej
# x=SMB^E
#  S (ang. sign) – znak liczby, 1 lub −1,
#  M (ang. mantissa) – znormalizowana mantysa, liczba ułamkowa[1],
#  B (ang. base) – podstawa systemu liczbowego[1] (2 dla systemów komputerowych),
#  E (ang. exponent) – wykładnik, cecha, liczba całkowita[1].
#  the sum 12.345 + 1.0001 = 13.3451 might be rounded to 13.345.
# float zapamiętuje najbliższe przybliżenie

# decimal pozwala ominąc bład zaokrąglęnia
from decimal import Decimal, ROUND_HALF_UP

# tworzenie liczb
decimal_1 = Decimal("0.1")
decimal_2 = Decimal(0.1)
decimal_3 = Decimal(1)

# wypisywanie
print(decimal_1)
print(decimal_2)
print(decimal_3)
# 0.1
# 0.1000000000000000055511151231257827021181583404541015625
# 1

# porównanie
# # liczby float
print(f"{decimal_1 == decimal_2 = }")  # decimal_1 == decimal_2 = False
print(f"{decimal_1 == Decimal("0.1") = }")  # decimal_1 == Decimal("0.1") = True
print(f"Decimal(1) == Decimal(1) {decimal_3 == Decimal("1")}")  # Decimal(1) == Decimal(1) True

# operacje matematyczne
a = Decimal('10.345')
b = Decimal("3.2")

add = a + b
print("Dodawanie:", add)  # Dodawanie: 13.545
substract = a - b
print("Odejmowanie:", substract)
multiply = a * b
print("Mnożenie:", multiply)
divide = a / b
print("Dzielenie:", divide)
# Dodawanie: 13.545
# Odejmowanie: 7.145
# Mnożenie: 33.1040
# Dzielenie: 3.2328125

precyzja = Decimal("0.01")
# zaokrąglanie np.: do dwóch miejsc po przecinku
print("Liczby zaokrąglone do dwóch miejsc po przecinku")
add = add.quantize(precyzja)
print("Dodawanie:", add)  # Dodawanie: 13.54
substract = substract.quantize(precyzja)
print("Odejmowanie:", substract)  # Odejmowanie: 7.14
multiply = multiply.quantize(precyzja)
print("Mnożenie:", multiply)  # Mnożenie: 33.10
divide = divide.quantize(precyzja)
print("Dzielenie:", divide)  # Dzielenie: 3.23

divide = a / b
print("Dzielenie z ustawieniem zaokrąglenia", divide.quantize(precyzja, rounding=ROUND_HALF_UP))
# Dzielenie z ustawieniem zaokrąglenia 3.23

value = Decimal("5.456")
rounding_nearest_005 = (value / Decimal("0.05")).quantize(Decimal("1"), rounding=ROUND_HALF_UP) * Decimal("0.05")
print(rounding_nearest_005)  # 5.45
print(Decimal("1.01") + 9)  # 10.01
