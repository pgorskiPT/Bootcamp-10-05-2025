from pandas.core.ops import kleene_and


class Matematyka:

    @staticmethod
    def dodaj(a, b):
        return a + b

    @staticmethod
    def odejmij(a, b):
        return a - b


wynik = Matematyka.dodaj(5, 6)
print(wynik)  # 11

wynik = Matematyka.odejmij(65, 89)
print(wynik)  # -24


# klasa z metotodami statycznymi
# celcjusz na farenheit
# farenheit na celcjusz
# Kalkulator Temperatur


class KalkulatorTemperatur:

    @staticmethod
    def celcius_to_farenheit(celcius):
        return celcius * 9 / 5 + 32

    @staticmethod
    def farenheit_to_celcius(farenheit):
        return (farenheit - 32) * 5 / 9


print(KalkulatorTemperatur.farenheit_to_celcius(100))
# 37.77777777777778
print(KalkulatorTemperatur.celcius_to_farenheit(37.77777777777778))
# 100.0
print(KalkulatorTemperatur.celcius_to_farenheit(36.6))
# 97.88000000000001
assert 100.0 == KalkulatorTemperatur.celcius_to_farenheit(37.77777777777778)
# assert 100.0 == KalkulatorTemperatur.celcius_to_farenheit(37.7777777777777)
# Traceback (most recent call last):
#   File "/Users/radoslawjaniak/PycharmProjects/Bootcamp-10-05-2025/day_7_14_06_2025/kl12a.py", line 46, in <module>
#     assert 100.0 == KalkulatorTemperatur.celcius_to_farenheit(37.7777777777777)
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# AssertionError
