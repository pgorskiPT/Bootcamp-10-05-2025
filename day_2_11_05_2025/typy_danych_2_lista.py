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
