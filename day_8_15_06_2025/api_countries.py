from typing import List

import requests as re
from pydantic import BaseModel

url = "https://restcountries.com/v3.1/name/Poland"

response = re.get(url)
# print(response.text)

data = response.json()
print(type(data))  # <class 'list'>

country = data[0]
# nazwa kraju, nazwa głowna, nazwa oficjalna
print(f"Nazwa kraju: {country['name']}")
# Nazwa
# kraju: {'common': 'Poland', 'official': 'Republic of Poland',
#         'nativeName': {'pol': {'official': 'Rzeczpospolita Polska', 'common': 'Polska'}}}
print(f"Nazwa główna: {country['name']['common']}")  # Nazwa główna: Poland
print(f"Nazwa oficjalna: {country['name']['official']}")  # Nazwa oficjalna: Republic of Poland

print(f"Stolica kraju: {country['capital']}")  # Stolica kraju: ['Warsaw'] -> lista
print(f"Stolica kraju: {country['capital'][0]}")  # Stolica kraju: Warsaw

print(f"Liczba ludności: {country['population']}")  # Liczba ludności: 37950802


class Pol(BaseModel):
    official: str
    common: str


class NativeName(BaseModel):
    pol: Pol


class Name(BaseModel):
    common: str
    official: str
    nativeName: NativeName
    # nativeName: dict


class CountryInfo(BaseModel):
    name: Name
    capital: List[str]
    population: int


# TypeError: __main__.CountryInfo() argument after ** must be a mapping, not list
# country_data = CountryInfo(**data)
country_data = [CountryInfo(**data) for data in response.json()]

for country in country_data:
    print(country)
# Nazwa kraju: {'common': 'Poland', 'official': 'Republic of Poland', 'nativeName': {'pol': {'official': 'Rzeczpospolita Polska', 'common': 'Polska'}}}
# Nazwa główna: Poland
# Nazwa oficjalna: Republic of Poland
# Stolica kraju: ['Warsaw']
# Stolica kraju: Warsaw
# Liczba ludności: 37950802
# name=Name(common='Poland', official='Republic of Poland', nativeName={'pol': {'official': 'Rzeczpospolita Polska', 'common': 'Polska'}}) capital=['Warsaw'] population=37950802

print(type(country))  # <class '__main__.CountryInfo'>
print(country.name)
# common='Poland' official='Republic of Poland' nativeName={'pol': {'official': 'Rzeczpospolita Polska', 'common': 'Polska'}}
print(country.name.common)  # Poland
print(country.name.official)  # Republic of Poland

print(country.population)  # 37950802

print(country.capital)  # ['Warsaw']
print(country.capital[0])  # Warsaw
