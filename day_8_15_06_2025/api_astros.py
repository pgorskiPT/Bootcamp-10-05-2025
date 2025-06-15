# REST API sposób komunikowanie się i wymiany danych pomiędzy klientem i serwer
# klient np.: przeglądarka
# serwer - tzw. backend - serwer który zawiera i przetwarza dane
# GET, POST, PUT/PATCH, DELETE - metody http
# GET - pobiera dane
# POST - do tworzenia obiektów
# PUT/PATCH - aktualizacja obiektu
# DELETE - usunięcie obiektu
# Działanie	Instrukcja  SQL	    HTTP	            DDS
# Create	            INSERT	PUT / POST	        write
# Read (Retrieve)	    SELECT	GET	                read / take
# Update	            UPDATE	POST / PUT / PATCH	write
# Delete (Destroy)	    DELETE	DELETE	            dispose
from typing import List

import requests  # klient http
from pydantic import BaseModel

# pip install requests
# pip install pydantic

url = "http://api.open-notify.org/astros.json"

response = requests.get(url)
print(response)  # <Response [200]>
# statusy odpowiedzi http
# https://pl.wikipedia.org/wiki/Kod_odpowiedzi_HTTP
# 2xx - ok
# 3xx - warningi, przekierowania
# 4xx - błedy po stronie klienta, 404 - błedny adres url, 400 Bad Request - błędy paremetrów
# 5xx - błędy serwera, 500 Interenal Server Error

# czysty json
print(response.text)
print(type(response.text))  # <class 'str'>

# zamiana jsona na słownik
response_data = response.json()
print(type(response_data))
print(response_data)  # <class 'dict'>

# wypisać wszystkie klucze ze słownika
print(response_data.keys())  # dict_keys(['people', 'number', 'message'])

for k in response_data:
    print(k)
# people
# number
# message

# wypisac liste people
people_list = response_data['people']
print(type(people_list))  # <class 'list'>
for i in people_list:
    print(i)
# {'craft': 'ISS', 'name': 'Oleg Kononenko'}
# {'craft': 'ISS', 'name': 'Nikolai Chub'}
# {'craft': 'ISS', 'name': 'Tracy Caldwell Dyson'}
# {'craft': 'ISS', 'name': 'Matthew Dominick'}
# {'craft': 'ISS', 'name': 'Michael Barratt'}
# {'craft': 'ISS', 'name': 'Jeanette Epps'}
# {'craft': 'ISS', 'name': 'Alexander Grebenkin'}
# {'craft': 'ISS', 'name': 'Butch Wilmore'}
# {'craft': 'ISS', 'name': 'Sunita Williams'}
# {'craft': 'Tiangong', 'name': 'Li Guangsu'}
# {'craft': 'Tiangong', 'name': 'Li Cong'}
# {'craft': 'Tiangong', 'name': 'Ye Guangfu'}

alexander = people_list[6]['name']
print(alexander)  # Alexander Grebenkin


class Astros(BaseModel):
    craft: str
    name: str


class AstroData(BaseModel):
    # people: list
    people: List[Astros]
    number: int
    # number: str #  1 validation error for AstroData
    message: str


data = AstroData(**response_data)
print(data)
# people=[
# {'craft': 'ISS', 'name': 'Oleg Kononenko'},
# {'craft': 'ISS', 'name': 'Nikolai Chub'},
# {'craft': 'ISS', 'name': 'Tracy Caldwell Dyson'},
# {'craft': 'ISS', 'name': 'Matthew Dominick'},
# {'craft': 'ISS', 'name': 'Michael Barratt'},
# {'craft': 'ISS', 'name': 'Jeanette Epps'},
# {'craft': 'ISS', 'name': 'Alexander Grebenkin'},
# {'craft': 'ISS', 'name': 'Butch Wilmore'},
# {'craft': 'ISS', 'name': 'Sunita Williams'},
# {'craft': 'Tiangong', 'name': 'Li Guangsu'},
# {'craft': 'Tiangong', 'name': 'Li Cong'},
# {'craft': 'Tiangong', 'name': 'Ye Guangfu'}]
# number=12
# message='success'

print(data.number)  # 12
print(data.message)  # success
# print(data.people)

# musimy użyć List[Astros]
for p in data.people:
    print(p)
    # print(type(p))
    print(p.__class__.__name__)
    print(f"{p.name=} {p.craft=}") # p.name='Li Guangsu' p.craft='Tiangong'
# craft='ISS' name='Oleg Kononenko'
# Astros
# craft='ISS' name='Nikolai Chub'
# Astros
# craft='ISS' name='Tracy Caldwell Dyson'
# Astros
# craft='ISS' name='Matthew Dominick'
# Astros
# craft='ISS' name='Michael Barratt'
# Astros
# craft='ISS' name='Jeanette Epps'
# Astros
# craft='ISS' name='Alexander Grebenkin'
# Astros
# craft='ISS' name='Butch Wilmore'
# Astros
# craft='ISS' name='Sunita Williams'
# Astros
# craft='Tiangong' name='Li Guangsu'
# Astros
# craft='Tiangong' name='Li Cong'
# Astros
# craft='Tiangong' name='Ye Guangfu'
# Astros
