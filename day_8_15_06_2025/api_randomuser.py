import requests as re
from pydantic import BaseModel, HttpUrl, EmailStr

# pip install email-validator

url = "https://randomuser.me/api/"

response = re.get(url)
print(response)  # <Response [200]>
print(response.text)

data = response.json()

user = data['results'][0]
# print(user)
# {'gender': 'female', 'name': {'title': 'Ms', 'first': 'Isabella', 'last': 'Clarke'},
#  'location': {'street': {'number': 9861, 'name': 'Anglesea Street'}, 'city': 'Timaru', 'state': 'Auckland',
#               'country': 'New Zealand', 'postcode': 19500,
#               'coordinates': {'latitude': '55.5545', 'longitude': '99.7173'},
#               'timezone': {'offset': '-8:00', 'description': 'Pacific Time (US & Canada)'}},
#  'email': 'isabella.clarke@example.com',
#  'login': {'uuid': '71a2f0c0-17f4-412e-83a3-1af800a3f651', 'username': 'brownbutterfly718', 'password': 'ne1469',
#            'salt': 'D9pei3Vn', 'md5': '656639a9e73adb6293f79b7247a2cc7c',
#            'sha1': 'be13d636bc3cb95b3338d986a6b008b79961a58a',
#            'sha256': 'c01b0810c0226bf9cf2f048991ab69d433f7c78f0e7124f77124a04ee0b062b0'},
#  'dob': {'date': '1998-09-27T13:09:58.800Z', 'age': 26}, 'registered': {'date': '2012-11-26T14:06:46.586Z', 'age': 12},
#  'phone': '(061)-943-0421', 'cell': '(740)-167-3755', 'id': {'name': '', 'value': None},
#  'picture': {'large': 'https://randomuser.me/api/portraits/women/1.jpg',
#              'medium': 'https://randomuser.me/api/portraits/med/women/1.jpg',
#              'thumbnail': 'https://randomuser.me/api/portraits/thumb/women/1.jpg'}, 'nat': 'NZ'}

print(f"Osoba: {user['name']}")
# Osoba: {'title': 'Miss', 'first': 'Miriam', 'last': 'Diaz'}
print(f"Imie: {user['name']['first']}")  # Imie: Bella
print(f"Nazwisko: {user['name']['last']}")  # Nazwisko: Hall

print(f"Numer telefonu: {user['phone']}")  # Numer telefonu: 022-6086-946

#   "picture": {
#         "large": "https://randomuser.me/api/portraits/men/43.jpg",
#         "medium": "https://randomuser.me/api/portraits/med/men/43.jpg",
#         "thumbnail": "https://randomuser.me/api/portraits/thumb/men/43.jpg"
#       },

user_name = user['name']['first']
user_last_name = user['name']['last']

photo_url = user['picture']['large']
print(f"Link do zdjęcia: {photo_url}")

response_photo = re.get(photo_url)
print(response_photo)  # <Response [200]>

filename = f"{user_name.lower()}_{user_last_name.lower()}.jpg"
with open(filename, "wb") as f:
    f.write(response_photo.content)

print("Zdjęcie zostało zapisane")


class Name(BaseModel):
    title: str
    first: str
    last: str


class Picture(BaseModel):
    large: HttpUrl
    medium: HttpUrl
    thumbnail: HttpUrl


class UserInfo(BaseModel):
    name: Name
    email: str
    email: EmailStr
    picture: Picture


user = data['results'][0]
user_info = UserInfo(**user)
print(user_info)

print(f"Imie: {user_info.name.first}")  # Imie: Bella
print(f"Nazwisko: {user_info.name.last}")  # Nazwisko: Hall

print(f"email: {user_info.email}")
# Imie: Ross
# Nazwisko: Romero
# email: ross.romero@example.com
# pip install email-validator

photo_url_pydantic = user_info.picture.large
print(f"Link do zdjęcia: {photo_url_pydantic}")
# Link do zdjęcia: https://randomuser.me/api/portraits/men/24.jpg

response_photo_pydantic = re.get(str(photo_url_pydantic))  # <Response [200]>
print(response_photo_pydantic)

filename = f"{user_name.lower()}_{user_last_name.lower()}.jpg"
with open(filename, "wb") as f:
    f.write(response_photo_pydantic.content)

print("Zdjęcie zostało zapisane")
