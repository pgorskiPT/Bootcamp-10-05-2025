# iterator - pozwala na dos†ep sekwencyjny do danych
# zapamietuje który element na m dostarczył
# oszczędność pamięci

# # 1. **Zarządzanie Pamięcią**: Iteratory są efektywne pod względem pamięci,
# # ponieważ nie wymagają wczytywania całego zbioru danych do pamięci na raz.
# # Są one szczególnie użyteczne przy przetwarzaniu dużych zbiorów danych.
# #
# # 2. **Uniwersalność**: Można je stosować do różnych typów struktur danych,
# # ułatwiając pisanie generycznego, wielokrotnego użytku kodu.
# #
# # 3. **Leniwe Wykonanie**: Iteratory realizują leniwe wykonanie,
# # co oznacza, że generują elementy na żądanie, co może być korzystne dla wydajności.

lista = [1, 2, 3, 4, 5]
print(lista)
for i in lista:
    print(i)

# print(next(lista))  # TypeError: 'list' object is not an iterator

iterator = iter(lista)
print(iterator)  # <list_iterator object at 0x10233bfa0>
print(type(iterator))  # <class 'list_iterator'>
# for i in iterator:
#     print(i)
# 1
# 2
# 3
# 4
# 5
#
print(25 * "-")
print(next(iterator))  # StopIteration - iterator nie ma już elementów do odczytania
print("Zrób coś")
print("Dalej")
print("Uczę się Pythona")
for x in range(5):
    # x\n -> x''
    print(x, sep=" | ", end="")  # 01234
print()
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))


# print(next(iterator)) # StopIteration - wyczerpałem dane z iteratora


class Count:
    """
    Klasa będąca iterator
    """

    def __init__(self, low, high):
        """
        Metoda inicjalizująca
        :param low:
        :param high:
        """
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1


print("---------")
counter = Count(1, 20)
print(next(counter))  # 1
print(next(counter))  # 2
print(next(counter))  # 3
print(next(counter))  # 4
print(next(counter))  # 5

print("-----")
while True:
    try:
        number = next(counter)
        print(number)
    except StopIteration:
        break

print(15 * "-")
counter2 = Count(1, 7)
print(next(counter2))
print(next(counter2))
print(next(counter2))
# ---------------
# 1
# 2
# 3
# 4
print(15 * "-")
counter3 = Count(5, 39)
print(next(counter3))
# ---------------
# 5
