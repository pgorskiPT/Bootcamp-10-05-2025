import datetime

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client['przykaldowa_baza']
kolekcja = db['uzytkownicy']

# kolekcja.insert_one(
#     {'imie': "Jan", "nazwisko": "Kowalski", 'wiek': 30}
# )

kolekcja.insert_many(
    [
        {'imie': "Anna", "nazwisko": "Nowak", 'wiek': 27},
        {'imie': "Paweł", "nazwisko": "Wiśniewski", 'wiek': 19, 'czas': datetime.datetime.now().strftime("%d/%m/%Y")},
    ]
)
for uzytkownik in kolekcja.find():
    print(
        uzytkownik)  # {'_id': ObjectId('68738fe16504593c49a6942b'), 'imie': 'Jan', 'nazwisko': 'Kowalski', 'wiek': 30}

# print(kolekcja.find_one({"imie": "Jan"}))
# {'_id': ObjectId('68738fe16504593c49a6942b'), 'imie': 'Jan', 'nazwisko': 'Kowalski', 'wiek': 30}

client.close()
# {'_id': ObjectId('68738fe16504593c49a6942b'), 'imie': 'Jan', 'nazwisko': 'Kowalski', 'wiek': 30}
# {'_id': ObjectId('68738fecbf82b1d57e32f509'), 'imie': 'Jan', 'nazwisko': 'Kowalski', 'wiek': 30}
# {'_id': ObjectId('68739011d7bcb04a45ff7b97'), 'imie': 'Jan', 'nazwisko': 'Kowalski', 'wiek': 30}
# {'_id': ObjectId('687391303f7284532cdd7170'), 'imie': 'Anna', 'nazwisko': 'Nowak', 'wiek': 27}
# {'_id': ObjectId('687391303f7284532cdd7171'), 'imie': 'Paweł', 'nazwisko': 'Wiśniewski', 'wiek': 19, 'czas': '13/07/2025'}