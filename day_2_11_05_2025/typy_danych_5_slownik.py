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
