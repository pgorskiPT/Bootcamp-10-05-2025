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

liczby = [45, 999, 34, 22, 13.34, 687]
print(liczby)  # [45, 999, 34, 22, 13.34, 687]
print(type(liczby))  # <class 'list'>

liczby.sort()  # sortowanie listy
print(liczby)  # [13.34, 22, 34, 45, 687, 999]

liczby_a = [45, 999, 34, 22, 13.34, 687, "A"]
print(liczby_a)  # [45, 999, 34, 22, 13.34, 687, 'A']
print(type(liczby_a))  # <class 'list'>

# nie zawsze wszystkie metody zadziałają w kolekcjach mieszanych
# liczby_a.sort() # TypeError: '<' not supported between instances of 'str' and 'int'

lista_osoby = ['radek', 'tomek', 'zenek', 'ania', 'karolina', 'magda']
lista_osoby.sort()
print(lista_osoby)  # ['ania', 'karolina', 'magda', 'radek', 'tomek', 'zenek']

lista_alfabet = ['a', "z", "p", 'd']
lista_alfabet.sort()
print(lista_alfabet)  # ['a', 'd', 'p', 'z']

lista_alfabet_pol = ['a', "z", "ą", "p", "ń", 'd']
lista_alfabet_pol.sort()
print(lista_alfabet_pol)  # ['a', 'd', 'p', 'z', 'ą', 'ń']
print(ord("z"))  # 122, ord() - wypisuje kod ascii dla znaku
print(ord("ą"))  # 261

# sortowanie i odwrócenie w jednym kroku
liczby.sort(reverse=True)
print(liczby)  # [999, 687, 45, 34, 22, 13.34]

# wypisanie w odwrotnej kolejnosci bez zmiany bazowej listy
print(liczby[::-1])  # krok -1, [start:stop:krok], [13.34, 22, 34, 45, 687, 999]
print(liczby[0:4:2])  # [999, 45]
print(liczby)  # [999, 687, 45, 34, 22, 13.34]
print(liczby[-3:0:-1])  # [34, 45, 687]

# odwrócenie kolekcji, bez sortowania
liczby_3 = [3, 8, 5, 12, 1]
liczby_3.reverse()
print(liczby_3)  # [1, 12, 5, 8, 3]

lista_osoby.reverse()
print(lista_osoby)  # ['zenek', 'tomek', 'radek', 'magda', 'karolina', 'ania']

print(liczby)  # [999, 687, 45, 34, 22, 13.34]
# nadpiac czwarty element
# wypisac ostatni eleemnt po indeksie dodatnim i ujemnym
# zrobić slice(wycinanie) jedno dodatnie, jedno ujemne
# usunąc z listy po indeksie i wypisac usunięty
# usunąć z listy po elemencie
# wyświwetlić listę odwróconą bez zmiany listy
liczby[3] = 666
print(liczby[-1])  # 13.34
print(liczby[len(liczby) - 1])  # 13.34
print(liczby[5])  # 13.34
print(liczby[1:3])  # [687, 45]
print(liczby[-5:-2])  # [687, 45, 666]
print(liczby.pop(3))  # , 666, usunięty indeks 3
print(liczby)  # [999, 687, 45, 22, 13.34]
liczby.remove(22)  # 22 - liczba z listy, nie indeks
print(liczby)  # [999, 687, 45, 13.34]
print(liczby[::-1])  # [13.34, 45, 687, 999]
print(liczby)  # [999, 687, 45, 13.34]

# łączenie list, dostajemy nową kolekcję
print(liczby + liczby_3)  # [999, 687, 45, 34, 22, 13.34, 1, 12, 5, 8, 3]
liczby_4 = liczby + liczby_3
print(liczby_4)  # [999, 687, 45, 34, 22, 13.34, 1, 12, 5, 8, 3]

liczby_5 = [1, 2, 3, 4, 5]
liczby_6 = [6, 7, 8, 9]
# nie tworzy nowej listy
liczby_5.extend(liczby_6)
print(liczby_5)  # [1, 2, 3, 4, 5, 6, 7, 8, 9], dokłada do liczby_5 elementy z listy liczby_6

# rozpakowanie sekwencji
tekst = "Pyth on."
lista_str = list(tekst)
print(lista_str)  # ['P', 'y', 't', 'h', ' ', 'o', 'n', '.']

lista_str_pusta = []
lista_str_pusta.extend(tekst)
print(lista_str_pusta)  # ['P', 'y', 't', 'h', ' ', 'o', 'n', '.']

lista_str2 = [tekst]
print(lista_str2)  # ['Pyth on.']

lista_str_pusta = []
lista_str_pusta.append(tekst)
print(lista_str_pusta)  # ['Pyth on.']

# zamiana listy na krotkę
krotka = tuple(liczby)
print(krotka)  # (999, 687, 45, 13.34)
print(type(krotka))  # <class 'tuple'>
