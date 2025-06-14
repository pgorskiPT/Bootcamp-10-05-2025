# stworzyć słownik
# zapisać słownik do pliku i odczytac za pomocą pickle
# odczytac wartość klucza ze słownika
# snake_case, PascalCase, UpperCamelCase
import pickle

slownik = {"name": "Radek", "age": 78}
print(type(slownik))  # <class 'dict'>
print(slownik)  # {'name': 'Radek', 'age': 78}

with open("../dickt1.pkl", "wb") as f:
    pickle.dump(slownik, f)

with open("../dickt1.pkl", "rb") as file:
    data = pickle.load(file)

print(data)  # {'name': 'Radek', 'age': 78}
print(type(data))  # <class 'dict'>
print(data['name'])  # Radek
