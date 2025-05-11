# Kolekcje

# lista - kolekcja przechowująca dowolną ilość danych, dowolnego typu w jedej kolekcji
# może w jedej liści eprzechowywac np.: str, int, bytes
# lista zachowuje kolejnośc przy dodawaniu eleemntów

# tworzenie pustej listy
lista = []
print(lista)  # []
print(type(lista))  # <class 'list'>
print(bool(lista))  # False

pusta_lista = list()
print(type(pusta_lista))  # <class 'list'>
print(pusta_lista)  # []

# deklaracja listy i wypełnienie danymi w miejscu deklaracji
lista_2 = [10, 20, 30]
print(type(lista_2))  # <class 'list'>
print(lista_2)  # [10, 20, 30]

lista_3 = [10.77, 30.66, 67, 15]
print(type(lista_3))  # <class 'list'>
print(lista_3)  # [10.77, 30.66, 67, 15]

# lista mieszana
lista_mieszane = [10, 5.2, "Oko", "Radek"]
print(type(lista_mieszane))  # <class 'list'>
print(lista_mieszane)  # [10, 5.2, 'Oko', 'Radek']

# sprawdzenie ile elementów znajduje się w kolekcji
print(len(lista_mieszane))  # długośc 4

# [10, 5.2, 'Oko', 'Radek']
#   0   1     2       3

# dodawanie elementów do listy
lista.append("Radek")
lista.append("Maciek")
lista.append("Tomek")
lista.append("Zenek")
lista.append("Marta")
lista.append("Anna")
print(lista)  # ['Radek', 'Maciek', 'Tomek', 'Zenek', 'Marta', 'Anna']
print(type(lista))  # <class 'list'>
print(len(lista))  # długośc 6 elementów

# ['Radek', 'Maciek', 'Tomek', 'Zenek', 'Marta', 'Anna']
#     0        1         2        3        4        5
#     -6       -5        -4       -3       -2       -1

print(lista[1])  # Maciek
print(lista[3])  # Zenek
print(lista[5])  # Anna

print(lista[len(lista) - 1])
print(lista[-1])  # Anna, ostatni element z listy
print(lista[-2])  # Marta
print(lista[-3])  # Zenek
print(lista[-4])  # Tomek
print(lista[-5])  # Maciek
print(lista[-6])  # Radek

# print(lista[10])  # IndexError: list index out of range

# wypisywanie wielu elementów z listy (slicowanie)
# ['Radek', 'Maciek', 'Tomek', 'Zenek', 'Marta', 'Anna']
#     0        1         2        3        4        5
#     -6       -5        -4       -3       -2       -1

print(lista[0:3])  # ['Radek', 'Maciek', 'Tomek']
print(lista[:3])  # ['Radek', 'Maciek', 'Tomek']
print(lista[1:3])  # ['Maciek', 'Tomek']
print(lista[:2])  # ['Radek', 'Maciek']
print(lista[-3:])  # ['Zenek', 'Marta', 'Anna']
print(lista[-2:])  # ['Marta', 'Anna']
print(lista[-1:])  # ['Anna']
print(lista[-1:][0])  # ['Anna'] lista, jeden element, indeks 0 -> 'Anna'
print(lista[-1][0])  # 'Anna', -> A
print(lista[:])  # ['Radek', 'Maciek', 'Tomek', 'Zenek', 'Marta', 'Anna']
print(lista[2:5])  # ['Tomek', 'Zenek', 'Marta']
print(lista[2:])  # ['Tomek', 'Zenek', 'Marta', 'Anna']

print(lista[-3:0])  # [] -> [3:0]
print(lista[0:-3])  # ['Radek', 'Maciek', 'Tomek'] -> [0:3]

print(lista[2:2])  # []
print(lista[2:3])  # ['Tomek']
print(lista[4:10])  # ['Marta', 'Anna']
print(lista[7:12])  # []
# Przerwa do 11:15

# nadpisanie elementu w liście na wskazanym indeksie
lista[2] = 'Mikołaj'
print(lista)  # ['Radek', 'Maciek', 'Mikołaj', 'Zenek', 'Marta', 'Anna']
print(len(lista))  # długość 6

# rozszerzenie listy, wstawienie lementu we wslazanym indeksie
lista.insert(1, "Karolina")
print(lista)  # ['Radek', 'Karolina', 'Maciek', 'Mikołaj', 'Zenek', 'Marta', 'Anna']
print(len(lista))  # długość 7

# usunięcie elementu z listy
# 1. usunięcie po indeksie -> pop()
# 2. usunięcie po elemencie -> remove()

# po indeksie pop()
print(lista.pop(0))  # Radek
print(lista)  # ['Karolina', 'Maciek', 'Mikołaj', 'Zenek', 'Marta', 'Anna']
ind = lista.index("Zenek")
print("Numer indeksu dla Zenka:", ind)  # Numer indeksu dla Zenka: 3, pierwszy napotkany
lista.append("Zenek")
print(lista)  # ['Karolina', 'Maciek', 'Mikołaj', 'Zenek', 'Marta', 'Anna', 'Zenek']
print("Numer indeksu dla Zenka:", ind)  # Numer indeksu dla Zenka: 3
print(lista.pop(ind))  # Zenek
print(lista)  # ['Karolina', 'Maciek', 'Mikołaj', 'Marta', 'Anna', 'Zenek']

# usunięcie po elemencie
lista.append("Maciek")
print(lista)  # ['Karolina', 'Maciek', 'Mikołaj', 'Marta', 'Anna', 'Zenek', 'Maciek']
lista.remove("Maciek")  # usunęło pierwszy napotkany
print(lista)  # ['Karolina', 'Mikołaj', 'Marta', 'Anna', 'Zenek', 'Maciek']

# lista.remove("Natasza") # ValueError: list.remove(x): x not in list
print("Marta" in lista)  # True
print("Marcin" in lista)  # False

print(lista.remove("Marta"))  # None
print(lista)  # ['Karolina', 'Mikołaj', 'Anna', 'Zenek', 'Maciek']

lista.append("Marta")
lista.append("Marta")
lista.append("Marcin")
print(lista)  # ['Karolina', 'Mikołaj', 'Anna', 'Zenek', 'Maciek', 'Marta', 'Marta', 'Marcin']
print(lista.index("Marta"))  # indeks numer 5

a = 1
b = 3
print(f"{a=}, {b=}")  # a=1, b=3
a = b
print(f"{a=}, {b=}")  # a=3, b=3
b = 7
print(f"{a=}, {b=}")  # a=3, b=7

lista_4 = lista  # -> a = b, przypiasnie referencji, adresu w pamięci
print(f"{lista}")
print(f"{lista_4}")
# ['Karolina', 'Mikołaj', 'Anna', 'Zenek', 'Maciek', 'Marta', 'Marta', 'Marcin']
# ['Karolina', 'Mikołaj', 'Anna', 'Zenek', 'Maciek', 'Marta', 'Marta', 'Marcin']
lista_copy = lista.copy()  # kopia elementów listy do nowej listy (nowy adres listy)
lista.clear()  # usunie elementy listy
print(f"{lista}")  # []
print(f"{lista_4}")  # []
print(f"{lista_copy}")  # ['Karolina', 'Mikołaj', 'Anna', 'Zenek', 'Maciek', 'Marta', 'Marta', 'Marcin']
# id() - wskazuje na adres pamięci listy
print(f"adres: {id(lista)=}")
print(f"adres: {id(lista_4)=}")
print(f"adres: {id(lista_copy)=}")
# adres: id(lista)=4372691072
# adres: id(lista_4)=4372691072
# adres: id(lista_copy)=4373300672
