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

# decimal - typ liczbowy pozwalający zarządzać zaokrągleniami
# w taki sposób, aby wyeliminować problem zaokrągleń jaki występuje przy liczbach float
# decimal wymaga więcej pamięci, obliczania są wolniejsze
from decimal import Decimal, ROUND_HALF_UP, getcontext

# tworzenie liczb decimal
decimal_1 = Decimal("0.1")
decimal_2 = Decimal(0.1)
decimal_3 = Decimal(1)

# wypisywanie
print(decimal_1)  # 0.1
print(decimal_2)  # 0.1000000000000000055511151231257827021181583404541015625
print(decimal_3)  # 1

# porównanie
print(f"Decimal('0.1') == Decimal(0.1)? {Decimal('0.1') == Decimal(0.1)}")  # Decimal('0.1') == Decimal(0.1)? False
print(f"Decimal('0.1') == Decimal('0.1')? {Decimal('0.1') == Decimal('0.1')}")  # Decimal('0.1') == Decimal('0.1')? True
print(f"Decimal(1) == Decimal('1')? {Decimal(1) == Decimal('1')}")  # Decimal(1) == Decimal('1')? True

# operacje matematyczne decimal
a = Decimal('10.345')
b = Decimal("3.2")

add = a + b
print("Dodawanie:", add)  # Dodawanie: 13.545

substract = a - b
print("Odejmowanie:", substract)  # Odejmowanie: 7.145

multiply = a * b
print("Mnożenie:", multiply)  # Mnożenie: 33.1040

divide = a / b
print("Dzielenie:", divide)  # Dzielenie: 3.2328125

print("Liczba zaokrąglona do dwóch miejsc po przecinku:")
add = add.quantize(Decimal('0.01'))
print("Dodawanie:", add)  # Dodawanie: 13.54

substract = substract.quantize(Decimal('0.01'))
print("Odejmowanie:", substract)  # Odejmowanie: 7.14

multiply = multiply.quantize(Decimal('0.01'))
print("Mnożenie:", multiply)  # Mnożenie: 33.10

divide = divide.quantize(Decimal('0.01'))
print("Dzielenie:", divide)  # Dzielenie: 3.23

print("Dodawanie zaokrąglone ROUND_HALF_UP:")
add = a + b
add = add.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
print(add)
# Dodawanie zaokrąglone ROUND_HALF_UP:
# 13.55
# ROUND_DOWN: Final[str]
# ROUND_HALF_UP: Final[str]
# ROUND_HALF_EVEN: Final[str]
# ROUND_CEILING: Final[str]
# ROUND_FLOOR: Final[str]
# ROUND_UP: Final[str]
# ROUND_HALF_DOWN: Final[str]
# ROUND_05UP: Final[str]

multiply = a * b
multiply = multiply.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
print("Mnożenie ROUND_HALF_UP:", multiply)  # 33.1040 -> Mnożenie ROUND_HALF_UP: 33.10

value = Decimal("5.456")
rounding_nearest_005 = (
                               value / Decimal('0.05')
                       ).quantize(Decimal("1"), rounding=ROUND_HALF_UP) * Decimal("0.05")
print(rounding_nearest_005)  # 5.45

print(Decimal("1.01") + 9)  # 10.01

# ustawienie długosci liczby na 3 cyfry (nie po przecinku!!!)
getcontext().prec = 3
add = a + b
print("Dodawanie", add)
substract = a - b
print("Odejmowanie", substract)
miltiplay = a * b
print("Mnożenie", miltiplay)
divide = a / b
print("Dzielenie", divide)
# Dodawanie 13.5
# Odejmowanie 7.14
# Mnożenie 33.1
# Dzielenie 3.23
