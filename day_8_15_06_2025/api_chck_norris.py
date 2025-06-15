# skorzystac z api chuck norris
# https://api.chucknorris.io

import requests
from pydantic import BaseModel, HttpUrl

url = "https://api.chucknorris.io/jokes/random"

response = requests.get(url)

data = response.json()

print(data)
print(data.keys())


# dict_keys(['categories', 'created_at', 'icon_url', 'id', 'updated_at', 'url', 'value'])
# {'categories': [],
# 'created_at': '2020-01-05 13:42:26.991637',
#  'icon_url': 'https://api.chucknorris.io/img/avatar/chuck-norris.png',
#  'id': 'T4emNDAXTq-r7fGRn0qsYA',
#  'updated_at': '2020-01-05 13:42:26.991637',
#  'url': 'https://api.chucknorris.io/jokes/T4emNDAXTq-r7fGRn0qsYA',
#  'value': 'Some people like to eat frog legs. Chuck Norris likes to eat lizard legs.'}

# dict_keys(['categories', 'created_at', 'icon_url', 'id', 'updated_at', 'url', 'value'])

class Joke(BaseModel):
    categories: list
    created_at: str
    icon_url: HttpUrl
    id: str
    updated_at: str
    url: HttpUrl
    value: str


joke = Joke(**data)

print(joke)
print(joke.value)  # Chuck Norris puts the G in G-spot.
print(joke.url)
