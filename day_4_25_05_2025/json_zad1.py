# json - typ danych para klucz - watość
# {"name":"John", "age":30, "car":null}
# podwójne cudzysłowia
# None -> null
# wykorzystywane w plikach kunfiguracyjnych
# wykorzystywany do komunikacji pomiedzy systemami
# odpowiednik jsona w pythonie jest słownik
import json

person_dict = {'name': 'Radek', 'age': 40, 'czy_pali': None}
print(type(person_dict))  # <class 'dict'>

with open('nasze_dane.json', "w") as f:
    json.dump(person_dict, f)

# beautify - upiększanie
with open("nasze_dane_b.json", "w") as file:
    json.dump(person_dict, file, indent=4)
# {
#     "name": "Radek",
#     "age": 40,
#     "czy_pali": null
# }

# posortowanie po kluczach
with open('nasze_dane_sort.json', "w") as f:
    json.dump(person_dict, f, indent=4, sort_keys=True)
# {
#     "age": 40,
#     "czy_pali": null,
#     "name": "Radek"
# }

with open('nasze_dane.json', "r") as f:
    data = json.load(f)

print(data)  # {'name': 'Radek', 'age': 40, 'czy_pali': None}
print(type(data))  # <class 'dict'>
print(data['name'])  # Radek

# zamiana słownika na json - odpowiadający mu str
json_text = json.dumps(data)
print(json_text)  # {"name": "Radek", "age": 40, "czy_pali": null}
print(type(json_text))  # <class 'str'>

# zamiana jsona na słownik
dict_json = json.loads(json_text)
print(dict_json)  # {'name': 'Radek', 'age': 40, 'czy_pali': None}
print(type(dict_json))  # <class 'dict'>
print(dict_json['name'])  # Radek
