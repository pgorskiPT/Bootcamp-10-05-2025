import pickle
from dataclasses import dataclass
from kl14a import Person

#
# @dataclass
# class Person:
#     first_name: str
#     last_name: str
#     id: int


with open("dane.pickle", "rb") as file:
    p = pickle.load(file)

print(p)
# [Person(first_name='Jan', last_name='Kowalski', id=1), Person(first_name='Maciej', last_name='Nowak', id=2)]

for person in p:
    print(person.first_name)
    person.greet()
# Jan
# Kowalski
# Maciej
# Nowak
