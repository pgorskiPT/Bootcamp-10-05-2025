import random

# random - działania na liczbach pseudolosowych

# """Return random integer in range [a, b], including both end points."""
print(random.randint(1, 100))  # int od 1 do 100
# z prawej zbiór otwarty
print(random.randrange(1, 100))  # int od 1 do 99
print(random.randrange(6))  # od 0 do 5
print(random.random())  # 0.8378956828319916 float od 0 do 0.9999999
print(random.random() * 7)  # float od 0 do 6.999999 4.571956324439835

lista = [5, 7, 45, 34, 56]

index = random.randrange(len(lista))
print(index, lista[index])  # 2 45

print(random.choice(lista))  # 56 - wylosowany element

print("-" * 20)
# bęben maszyny -> lista
# losowanie kul -> random
# usunięcie kuli z bębna -> remove
# wyswietlenie w tv -> print

lista_kule = list(range(1, 50))  # od 1 do 49
# print(lista_kule)

wyn = random.choice(lista_kule)  # losuje jeden element
print(wyn)
lista_kule.remove(wyn)

print(random.choices(lista_kule, k=6))  # [14, 9, 3, 22, 9, 9], losuje z powtórzeniami
print(random.sample(lista_kule, k=6))  # [11, 9, 46, 35, 8, 21], losuje bez powtórzeń
print(random.sample(lista_kule, 6))  # [13, 38, 47, 27, 1, 49], losuje bez powtórzeń
