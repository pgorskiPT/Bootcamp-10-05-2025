# zbiór (set) - przechowują unikalne wartości (brak duplikatów)
# nie posiada indesku
# nie zachowuje kolejności przy dodawaniu elementów

lista = [44, 55, 66, 777, 33, 22, 11, 33, 11]
print(type(lista))  # <class 'list'>, posiada duplikaty
zbior = set(lista)
print(zbior)  # {33, 66, 777, 11, 44, 22, 55}, usunięte duplikaty, zmieniona kolejność

lista2 = list(zbior)
print(lista2)  # [33, 66, 777, 11, 44, 22, 55]
lista2.remove(33)
print(lista2)  # [66, 777, 11, 44, 22, 55]

# utworzenie pustego zbioru (seta)
# tylko za pomocą metody set()
zb2 = set()
print(zb2)  # set() - pusty zbiór
print(type(zb2))  # <class 'set'>

# dodanie elementów do zbiór
zb2.add(2)
zb2.add(3)
zb2.add(5)
zb2.add(5)
zb2.add(3)
print(zb2)  # {2, 3, 5}

print(zbior)  # {33, 66, 777, 11, 44, 22, 55}
zbior.add(33)
zbior.add(18)
zbior.add(18)
print(zbior)  # {33, 66, 777, 11, 44, 18, 22, 55}
# kolejnośc zostaje zmieniona

# pop() - usnięcie pierwszego eleemntu
print(zbior.pop())  # 33
print(zbior)  # {66, 777, 11, 44, 18, 22, 55}

print(zbior.pop())  # 66
zbior.pop()
zbior.pop()
print(zbior)  # {44, 18, 22, 55}

# uzycie sorted() na zbiorze
# zwróci nam listę posortowanych elemntó∑
print(sorted(zbior))  # [18, 22, 44, 55]

# usunięcie elementu ze zbioru
zbior.remove(55)
zbior.remove(18)
print(f"Zbiór po usunięciu: {zbior=}")  # Zbiór po usunięciu: zbior={44, 22}
print(f"Zbiór po usunięciu: {zbior}")  # Zbiór po usunięciu: {44, 22}

# tworzenie zbioru z konkretnymi wartościami
zbior2 = {667, 11, 44, 18, 52, 22, 667, 62, 999}
print(zbior2)  # {999, 11, 44, 18, 52, 22, 667, 62}

zbior3 = {667, 11, 44, 18, 667, 62, 999}
print(zbior3)  # {18, 999, 11, 44, 667, 62}

# suma zbiorów - wszystkie lementy, ktore znajdują się w jednym i drugim zbiorze
# tworzy nowy zbiór
print(zbior | zbior3)  # {999, 11, 44, 18, 22, 667, 62}
print(zbior.union(zbior3))  # {999, 11, 44, 18, 22, 667, 62}
# zbiory bazowe nie zmieniły się
print(zbior)  # {44, 22}
print(zbior3)  # {18, 999, 11, 44, 667, 62}

zbior4 = {8, 9, 10}
print(zbior.union(zbior3, zbior4))
# {999, 8, 9, 10, 11, 44, 18, 22, 667, 62} - suma trzech zbiorów
print(zbior | zbior3 | zbior4)
# {999, 8, 9, 10, 11, 44, 18, 22, 667, 62}

# część wspólna - zwraca nowy zbiór
print(zbior & zbior3)  # {44}
print(zbior.intersection(zbior3))  # {44}

# róznica zbiorów - zwróci nowy zbiór
print(zbior - zbior3)  # {22}
print(zbior.difference(zbior3))  # {22}
print(zbior3.difference(zbior))  # {999, 11, 18, 667, 62}

# suma zbiorów
# zmienia zbiór bazowy !!!
# wynik pojawi się w zbiorze a
a = {1, 2}
b = {2, 3}
a.update(b)
print(f"{a=}")  # a={1, 2, 3}, zbiór a uległ zmiannie

a = {1, 2, 3}
b = {2, 3, 4}
a.intersection_update(b)  # część wspólna zbiorów, wynik zapisany do zbioru a
print(f"{a=}")  # a={2, 3}, zbiór a został nadpisany

