# wyjątki - błedy podczas wykonywania programu

# print(5 / 0)
# print("Dalsza częśc programu")
# # Traceback (most recent call last):
#   File "/Users/radoslawjaniak/PycharmProjects/Bootcamp-10-05-2025/day_3_24_05_2025/wyjatki.py", line 3, in <module>
#     print(5 / 0)
#           ~~^~~
# ZeroDivisionError: division by zero
# Process finished with exit code 1 - bład działania programu

# jako programiści powinnismy przechwycic i obsłużyć wyjątek
try:
    # print(5 / 0)
    # print("a" / 2)
    print(int("A"))
    # raise KeyError("Bład klucza")
    wynik = 90 / 3
except ZeroDivisionError:
    print("Nie dziel przez zero")
except TypeError:
    print("Błąd typu")
except ValueError:
    print("Błąd wartości")
except Exception as e:
    print("Bład", e)
else:  # wykona się tylko gdy nie ma błędu
    print("Wynik:", wynik)
finally:  # wykona zawsze
    print("konniec obliczeń")

print("Dalsza częśc programu")
# Nie dziel przez zero
# Dalsza częśc programu
# Błąd typu
# Dalsza częśc programu
# Błąd wartości
# Dalsza częśc programu
# Bład 'Bład klucza'
# Dalsza częśc programu
# Wynik: 30.0
# Dalsza częśc programu
# Wynik: 30.0
# konniec obliczeń
# Dalsza częśc programu
# Błąd wartości
# koniec obliczeń
# Dalsza częśc programu
