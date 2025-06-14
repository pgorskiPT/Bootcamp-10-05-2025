# wyjątki
# możemy dziedziczyć po klasie Exception i tworzyć swoje wyjątki
class MyException(Exception):
    def __init__(self, message):
        super().__init__(message)


# print(2 / 0) # ZeroDivisionError: division by zero
# raise ZeroDivisionError("Nie dziel przez zero") # ZeroDivisionError: Nie dziel przez zero

# raise MyException("Wyjątek od Radka")
# Traceback (most recent call last):
#   File "/Users/radoslawjaniak/PycharmProjects/Bootcamp-10-05-2025/day_7_14_06_2025/kl17a.py", line 11, in <module>
#     raise MyException("Wyjątek od Radka")
# MyException: Wyjątek od Radka

try:
    x = int(input("Podaj lizcbę cąlkowitą dodatnią"))
    if x < 0:
        print("Liczba ma być większa od zera")
        raise MyException("Liczba musi być dodatnia")
except MyException:
    print("Wystąpił wyjątek MyException")
except ValueError:
    print("Wystąpił błąd wartości")
except Exception as e:
    print("Bład inny", e)
else:  # wykonuje się zawsze
    print("Wprowadziłęś poprawną wartośc x:", x)
finally:  # wykonuje się zawsze
    print("Wprowadź kolejne dane")

# Podaj lizcbę cąlkowitą dodatnią4
# Wprowadziłęś poprawną wartośc x: 4
# Wprowadź kolejne dane
# Podaj lizcbę cąlkowitą dodatniąa
# Wystąpił błąd wartości
# Wprowadź kolejne dane
# Podaj lizcbę cąlkowitą dodatnią-1
# Liczba ma być większa od zera
# Wystąpił wyjątek MyException
# Wprowadź kolejne dane
