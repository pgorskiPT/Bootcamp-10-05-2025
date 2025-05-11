# słownik - para klucz wartosc
# {'klucz' : 'wartosc'}
# klucze nie mogą sie powtarzać
# słownik jest odpowiednikiem jsona w pythonie

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
print(dict_with_dict['A'])  # ['asif', 'jhon', 'maria']

print(my_dict)  # {'A': 'one', 'B': 'two', 'C': 'three', 'D': 'four'}
print(my_dict["A"])  # one

print(dict_with_integer[1])  # one
print(dict_with_all['C'])  # {10, 'Name', 'age'}

# print(my_dict_4['e']) # KeyError: 'e'

print(my_dict_4.get('a'))  # dla klucza 'a' -> [10, 20, 30]
print(my_dict_4.get('e'))  # None - oznacza brak klucza w słowniku
# możemy ustawić wartość domyśłną jaka będzie zwracana gdy nie ma klucza w słowniku
print(my_dict_4.get('e', "Nie ma"))  # Nie ma - brak klucza
print(my_dict_4.get('a', "Nie ma"))  # [10, 20, 30]
