# {"name": "Radek", "wiek": 90}
# __missing__ - metoda wykonywana gdy nie ma klucza w słowniku

class DefaultDict(dict):
    def __missing__(self, key):
        return "default"


d_python = {}  # pusty słownik
print(type(d_python))  # <class 'dict'>
print(d_python)  # {}
# print(d_python['name'])  # KeyError: 'name'
d_python['name'] = "Radek"
print(d_python['name'])  # Radek

d1 = DefaultDict()
print(d1['name'])  # default - metoda __missing__ zwróciłą słówko "default"


# zrobić słownik, który gdy nie ma klucza
# dopisze ten klucz  z wartością 0
class AutoDict(dict):
    def __missing__(self, key):
        self[key] = 0
        return key


d2 = AutoDict()
print(d2)  # {}
print(d2['name'])  # name
print(d2)  # {'name': 0}
print(d2['name'])  # 0
d2['name'] = "Radek"
print(d2)  # {'name': 'Radek'}


class CaseInsensitiveDict(dict):
    def __missing__(self, key):
        if isinstance(key, str):  # sprawdza czy klucz jest typu str
            return self.get(key.casefold())
        return None


d3 = CaseInsensitiveDict()
d3['name'] = "Radek"
print(d3['NAme'])  # Radek
d3[1] = "Radek"
print(d3)  # {'name': 'Radek', 1: 'Radek'}
print(d3[2])  # AttributeError: 'int' object has no attribute 'casefold'
# po dodaniu sprawdzania typu
# None
