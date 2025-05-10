wiek = 47  # int
rok = 2025  # int
temp = 36.6  # float

print(temp)  # 36.6
print(type(temp))  # <class 'float'>

print(wiek + rok)  # 2072
print(wiek - rok)  # -1978
print(wiek * rok)  # 95175
print(wiek / rok)  # 0.023209876543209877 -> float

print(rok // wiek)  # częśc całkowita z dzielenia, 43
print(10 // 3)  # 3

print(rok % wiek)  # modulo, reszta z dzielenia, 4
print(10 % 3)  # reszta 1, bo 3 * 3 + 1 = 10

wynik = wiek ** rok
print(wynik)
print(f"Wiek do potęgi rok: {wynik:,}")

print(f"Długośc: {len(str(wynik))}")  # Długośc: 3386

# print(wynik ** 2)
# ValueError: Exceeds
# the
# limit(4300
# digits) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit

print(74 - 8 * 45 + 8 / 2 + 8 / 2)  # -278.0
print(74 - (8 * 45) + 8 / 2 + 8 / 2)  # -278.0
print(74 - (8 * 45) + (8 / 2 + 8) / 2)  # -280.0

# liczby float
# bład zaokrąglenia
print(0.2 + 0.8)  # 1.0
print(0.2 + 0.7)  # 0.8999999999999999
print(0.1 + 0.2)  # 0.30000000000000004
# zapamietuje w postaci wykładniczej
# x=SMB^E
#  S (ang. sign) – znak liczby, 1 lub −1,
#  M (ang. mantissa) – znormalizowana mantysa, liczba ułamkowa[1],
#  B (ang. base) – podstawa systemu liczbowego[1] (2 dla systemów komputerowych),
#  E (ang. exponent) – wykładnik, cecha, liczba całkowita[1].
#  the sum 12.345 + 1.0001 = 13.3451 might be rounded to 13.345.