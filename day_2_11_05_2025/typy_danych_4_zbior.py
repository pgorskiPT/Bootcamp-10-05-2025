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
