# Redis (IPA: rɛdɪs; skrót od nazwy Remote Dictionary Server[6]) – otwartoźródłowe[3]
# oprogramowanie działające jako nierelacyjna baza danych przechowująca
# dane w strukturze klucz-wartość w pamięci operacyjnej serwera,


# docker pull redis
# docker run --name redis-server -d -p 6379:6379 redis

import redis

# połaczenie do bazy Redis, localhost, port 6379
r = redis.Redis()

# dodanie klucza i wartości
r.set('name', "Radek")

# odczytanie wartości dla klucza i zamiana z typu bajtowego na tekstowy
wartosc = r.get('name')
print(wartosc)  # b'Radek' - dostaliśmy bajty
print(wartosc.decode('utf-8'))  # Radek

# usunięcie klucza
# r.delete('name')

# sprawdzenie czy istnieje
czy_istnieje = r.exists('name')
print("Czy istnieje?", czy_istnieje)
print("Czy istnieje?", bool(czy_istnieje))
# b'Radek'
# Radek
# Czy istnieje? 0
# Czy istnieje? False
d = {
    True: "Klucz istnieje",
    False: "Klucz nieistnieje"
}
print("Czy istnieje?", d[bool(czy_istnieje)])  # Czy istnieje? Klucz nieistnieje
# gdy zakomentuje delete klucz istnieje
# b'Radek'
# Radek
# Czy istnieje? 1
# Czy istnieje? True
# Czy istnieje? Klucz istnieje
