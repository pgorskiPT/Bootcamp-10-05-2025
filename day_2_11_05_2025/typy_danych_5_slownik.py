# słownik - para klucz wartosc
# {'klucz' : 'wartosc'}
# klucze nie mogą sie powtarzać
# słownik jest odpowiednikiem jsona w pythonie
from ctypes.wintypes import PWORD

my_dict = {"A": "one", 'B': 'two', "C": 'three', "D": 'four'}
print(my_dict)  # {'A': 'one', 'B': 'two', 'C': 'three', 'D': 'four'}
print(type(my_dict))  # <class 'dict'>

empty_dict = dict()  # tworzenie pustego słownika
print(empty_dict)  # {} - pusty słownik

empty_dict_2 = {}
print(type(empty_dict_2))  # <class 'dict'>
print(empty_dict_2)  # {} - pusty słownik

dict_with_integer = {1: 'one', 2: "two", 3: 'three'}
print(dict_with_integer)  # {1: 'one', 2: 'two', 3: 'three'}

dict_mixed = {1: 'one', 'A': "two", 3: "three"}
print(dict_mixed)  # {1: 'one', 'A': 'two', 3: 'three'}

# klucz, wartośc, para
print(dict_mixed.keys())  # dict_keys([1, 'A', 3]) -> klucze
print(dict_mixed.values())  # dict_values(['one', 'two', 'three']) -> wartości
print(dict_mixed.items())  # dict_items([(1, 'one'), ('A', 'two'), (3, 'three')]) -> pary

print(dict_with_integer.keys())  # dict_keys([1, 2, 3]) - lista kluczy

dict_with_list = {1: "one", 2: 'two', "A": ['asif', 'jhon', 'maria']}
print(dict_with_list)  # {1: 'one', 2: 'two', 'A': ['asif', 'jhon', 'maria']}

dict_with_list_and_tuple = {
    1: 'one',
    2: 'two',
    "A": ['asif', 'jhon', 'maria'],
    "B": ('Bat', 'cat', 'hat')
}
print(dict_with_list_and_tuple)
# {1: 'one', 2: 'two', 'A': ['asif', 'jhon', 'maria'], 'B': ('Bat', 'cat', 'hat')}

dict_with_all = {
    1: 'one',
    2: 'two',
    'A': ['asif', 'jhon', 'maria'],
    "B": ('Bat', 'cat', 'hat'),
    "C": {"Name", 'age', 10}
}

print(dict_with_all)
# {1: 'one', 2: 'two', 'A': ['asif', 'jhon', 'maria'], 'B': ('Bat', 'cat', 'hat'), 'C': {'Name', 10, 'age'}}

dict_with_dict = {
    1: 'one',
    2: 'two',
    'A': ['asif', 'jhon', 'maria'],
    "B": ('Bat', 'cat', 'hat'),
    "C": {"Name", 'age', 10},
    "D": {"Name": "Radek", "age": 76}
}
print(dict_with_dict)
# {1: 'one',
# 2: 'two',
# 'A': ['asif', 'jhon', 'maria'],
#  'B': ('Bat', 'cat', 'hat'),
#  'C': {'Name', 10, 'age'},
#  'D': {'Name': 'Radek', 'age': 76}}

# tworzenie słownika z sekwencji kluczy
keys = {'a', 'b', 'c', 'd'}
my_dict_from_keys = dict.fromkeys(keys)
print(my_dict_from_keys)  # {'c': None, 'b': None, 'a': None, 'd': None}
# domyślnie jako wartość przyjmuje None

value = 10
my_dict_3 = dict.fromkeys(keys, value)
print(my_dict_3)  # {'d': 10, 'a': 10, 'c': 10, 'b': 10}
# jako wartość podstawi wartość ze zmiennej value

value = [10, 20, 30]
my_dict_4 = dict.fromkeys(keys, value)
print(my_dict_4)
# {'a': [10, 20, 30], 'd': [10, 20, 30], 'c': [10, 20, 30], 'b': [10, 20, 30]}

# zastosowanie fromkeys() do usunięcia duplikatów z listy
# od pythona 3.7 można ząlożyć, ze zachowa kolejność
keys = [1, 2, 2, 3, 4, 4, 5]  # lista z duplikatami
dict_unique = dict.fromkeys(keys)
print(dict_unique)  # {1: None, 2: None, 3: None, 4: None, 5: None}
list_unique = list(dict_unique)
print(list_unique)  # [1, 2, 3, 4, 5]

print(list(dict.fromkeys(keys)))  # [1, 2, 3, 4, 5], w jedej linijce

# wypisanie wartości dla kluczy ze słownika
print(dict_with_dict['A'])  # ['asif', 'john', 'maria']

print(my_dict)  # {'A': 'one', 'B': 'two', 'C': 'three', 'D': 'four'}
print(my_dict["A"])  # one

print(dict_with_integer[1])  # one
print(dict_with_all['C'])  # {10, 'Name', 'age'}

# print(my_dict_4['e']) # KeyError: 'e'

print(my_dict_4.get('a'))  # dla klucza 'a' -> [10, 20, 30]
print(my_dict_4.get('e'))  # None - oznacza brak klucza w słowniku
# możemy ustawić wartość domyślną jaka będzie zwracana gdy nie ma klucza w słowniku
print(my_dict_4.get('e', "Nie ma"))  # Nie ma - brak klucza
print(my_dict_4.get('a', "Nie ma"))  # [10, 20, 30]

my_dict5 = {"Name": "Radek", "ID": 12345, "DDB": 1991, 'Address': "Warsaw"}
print(my_dict5)  # {'Name': 'Radek', 'ID': 12345, 'DDB': 1991, 'Address': 'Warsaw'}
print(my_dict5['DDB'])  # 1991
print(my_dict5.get("DDB"))  # 1991

# nadpisanie wartości dla klucza
my_dict5['DDB'] = '1980'  # nadpisanie str
print(my_dict5)
# {'Name': 'Radek', 'ID': 12345, 'DDB': '1980', 'Address': 'Warsaw'}
print(type(my_dict5['DDB']))  # <class 'str'>

my_dict5['Address'] = "Warsaw Centrum"
print(my_dict5)  # {'Name': 'Radek', 'ID': 12345, 'DDB': '1980', 'Address': 'Warsaw Centrum'}

dict1 = {"DDB": 1995}
print(dict1)  # {'DDB': 1995}
print(type(dict1))  # <class 'dict'>

# update słownik innym słownikiem
my_dict5.update(dict1)
print(my_dict5)  # {'Name': 'Radek', 'ID': 12345, 'DDB': 1995, 'Address': 'Warsaw Centrum'}

# dodanie klucza do słownika
my_dict5['Job'] = "Developer"
print(my_dict5)
# {'Name': 'Radek', 'ID': 12345, 'DDB': 1995, 'Address': 'Warsaw Centrum', 'Job': 'Developer'}

dict2 = {'cpi': 3.41}  # float, liczby zmiennoprzecinkowe
print(dict2)  # {'cpi': 3.41}

# update słownika
# jesli klucz w docelowym słowniku nie istnieje zostanie dodany
# docelowy słownik my_dict5
my_dict5.update(dict2)
print(my_dict5)
# {'Name': 'Radek', 'ID': 12345, 'DDB': 1995, 'Address': 'Warsaw Centrum', 'Job': 'Developer', 'cpi': 3.41}

# usnięcie elementu ze słownika
print(my_dict5.pop("cpi"))  # 3.41
print(my_dict5)
# {'Name': 'Radek', 'ID': 12345, 'DDB': 1995, 'Address': 'Warsaw Centrum', 'Job': 'Developer'}

# usunięcie ostatniego elemntu ze słownika
print(my_dict5.popitem())  # ('Job', 'Developer')
print(my_dict5)
# {'Name': 'Radek', 'ID': 12345, 'DDB': 1995, 'Address': 'Warsaw Centrum'}

# usunięcie po kluczu
del my_dict5['ID']
print(my_dict5)
# {'Name': 'Radek', 'DDB': 1995, 'Address': 'Warsaw Centrum'}

# usunięcie wszystkich elementów ze słownika
my_dict5.clear()
print(my_dict5)  # {}

# usunięcie z pamięci
del my_dict5
# my_dict5 nie istnieje - został usuniety z pamięci
# print(my_dict5) # NameError: name 'my_dict5' is not defined. Did you mean: 'my_dict'?

# zamiana klucza w słowniku
slownik = {"stary_klucz": "wartosc"}
slownik['nowy_klucz'] = slownik.pop('stary_klucz')
print(slownik)  # {'nowy_klucz': 'wartosc'}

# kopiowanie słownika
my_dict5 = {'Name': 'Radek', 'ID': 12345, 'DDB': 1995, 'Address': 'Warsaw Centrum', 'Job': 'Developer', 'cpi': 3.41}
# kopia referencji
my_dict5_copy_ref = my_dict5
print(id(my_dict5_copy_ref))  # 4350392640
print(id(my_dict5))  # 4350392640

# kopia elementów słownika do drugiego słownika
my_dict5_copy = my_dict5.copy()
my_dict5.clear()
print(my_dict5_copy)
# {'Name': 'Radek', 'ID': 12345, 'DDB': 1995, 'Address': 'Warsaw Centrum', 'Job': 'Developer', 'cpi': 3.41}
print(my_dict5)  # {}
print(my_dict5_copy_ref)  # {}

print(f"{id(my_dict5)}")  # 4310759744
print(f"{id(my_dict5_copy_ref)}")  # 4310759744
print(f"{id(my_dict5_copy)}")  # 4310759616 - inny adres, kopia elementów nie referencji

dict_small = {"x": 3}
dict_small.update([('y', 3), ("z", 7)])
# [('y',3), ("z",7)] -> lista krotek
print(dict_small)  # {'x': 3, 'y': 3, 'z': 7}
print(dict_small.items())  # dict_items([('x', 3), ('y', 3), ('z', 7)])

# napisac program, który będzie działąl jak słownik angielsko-polski
# wyświetla dostępne słowa
# pobiera słowo od użytkownika
# wyświetla tłumaczenie

# input() - pobiera dane od użytkownika
# odp = input("Podaj imię")
# print(odp)
# Podaj imięradek
# radek

ang_pol = {'name': 'imie', "cat": "kot", 'water': "woda"}
print('-------- Słownik pol-ang --------')
print("Mamy takie słowka w słowniku", ang_pol.keys())
odp = input("Podaj słowko do przetłumaczenia")
# print(f"{odp.strip()} to: {ang_pol[odp.strip()]}")
# print(f"{odp.strip().lower()} to: {ang_pol[odp.strip().lower()]}")
# Podaj słowko do przetłumaczeniaCat
# cat to: kot

# ß
word1 = "gross"
word2 = "Groß"
print(word1.lower() == word2.lower())  # False
""" Return a version of the string suitable for caseless comparisons. """
# Przekształca wszystkie duże litery na małe
# dostosowuje tekst zgodnie z zasadami językowymi Unicode
# znaki specjalne, takie jak ß w języku niemieckim, zamieni na ss.
# Znaki z akcentami mogą być uproszczone w zależności od kontekstu
# https://www.unicode.org/Public/12.1.0/ucd/CaseFolding.txt
print(word1.casefold() == word2.casefold())  # True

# print(f"{odp.strip().casefold()} to: {ang_pol[odp.strip().casefold()]}")
# Podaj słowko do przetłumaczenia Cat
# False
# True
# cat to: kot
print(f"{odp.strip().casefold()} to: {ang_pol.get(odp.strip().casefold())}")
print(f"{odp.strip().casefold()} to: {ang_pol.get(odp.strip().casefold(), "Nie ma w słowniku")}")
# Podaj słowko do przetłumaczeniaCot
# False
# True
# cot to: None
# cot to: Nie ma w słowniku
