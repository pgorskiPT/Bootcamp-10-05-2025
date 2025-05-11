# krotka (tupla) - kolekcja niemutowalna
# lepsze wykorzystanie pamięci
# przechowanie konfiguracji
# jednoelementowa krotka traktowan często jako stała - wypełnia znamiona zmiennej

tupla1 = "Radek"
print(type(tupla1))  # <class 'str'>

tupla2 = ("Radek")
print(type(tupla2))  # <class 'str'>

# PEP8 zaleca tworzenie tupli jedoelementowych z nawiasami ()
# czytelniejszy zapis
tupla3 = ("Radek",)
print(type(tupla3))  # <class 'tuple'>
print(tupla3)  # ('Radek',)

tupla4 = "Radek",
print(type(tupla4))  # <class 'tuple'>
print(tupla4)  # ('Radek',)

tupla_names = "Radek", "Tomek", "Zenek", "Bartek"
print(type(tupla_names))  # <class 'tuple'>
print(tupla_names)  # ('Radek', 'Tomek', 'Zenek', 'Bartek')

temp = 36, 6
print(type(temp))  # <class 'tuple'>
print(temp)  # (36, 6)

tupla_liczby = 43, 55, 22.34, 11, 200
tupla_liczby = (43, 55, 22.34, 11, 200)
print(type(tupla_liczby))
print(tupla_liczby)

# tupla jest niemutowalna - nie mozna dokonac w niej zmian
# temp[0] = 1  # TypeError: 'tuple' object does not support item assignment
# ctrl / - automatyczny komentarz

# nie da się usunąc jednego elementu z krotki
# del temp[0] # TypeError: 'tuple' object doesn't support item deletion

# można usunąć całą tuple z pamięci
del temp
# print(temp) # NameError: name 'temp' is not defined
# przerwa do 13:45

print(tupla_liczby)  # (43, 55, 22.34, 11, 200)
# spróbujcuie czy na tupli działa slicowanie
print(tupla_liczby[:3])  # (43, 55, 22.34)
print(tupla_liczby[0:3])  # (43, 55, 22.34)
print(tupla_liczby[1:3])  # (55, 22.34)
print(tupla_liczby[2:])  # (22.34, 11, 200)

print(tupla_liczby[-1])  # 200
print(tupla_liczby[::-1])  # (200, 11, 22.34, 55, 43)
print(tupla_liczby[-1::-1])  # (200, 11, 22.34, 55, 43)
# [start:stop:krok] krok -1 oznacza krok do tyłu
print(tupla_liczby[1:4:2])  # (55, 11) co drugi element
print(tupla_liczby[:])  # (43, 55, 22.34, 11, 200)


