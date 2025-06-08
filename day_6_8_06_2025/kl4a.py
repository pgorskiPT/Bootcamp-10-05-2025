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
