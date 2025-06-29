# https://sqlite.org/download.html

# sqlite3 --version
# sqlite3 test.db - utworzenie/otworzenie bazy danych

# tworzenie tabeli w bazie danych
# create table users (id INT PRIMARY KEY, name VARCHAR(100), age INT);

# wypisanie dostępnych tabel
# .tables

# dodanie rekordu do bazy danych
# insert into users (id, name, age) values (1, 'Jan Kowalski', 30);

# odczyt rekordu z bazy danych
# select * from users;
# 1|Jan Kowalski|30

# ziana wartości w rekordzie
# update users set age=31 where id=1;
# sqlite> select * from users;
# 1|Jan Kowalski|31
# sqlite>

# usunięcie rekordu o id=1
#  delete from users where id=1;

# wypisze posortowane rosnącą po wieku
# select * from users order by age;
# 2|Anna Nowak|28
# 1|Jan Kowalski|30
# 3|Radek Nowak|35

# malejąco
# select * from users order by age desc;
# 3|Radek Nowak|35
# 1|Jan Kowalski|30
# 2|Anna Nowak|28

# pobierz uzytkownik dla których wiek > 29
# select * from users where age > 29;
# 1|Jan Kowalski|30
# 3|Radek Nowak|35
# sqlite>

# zmiana anazwy tabeli
# alter table age rename to ege;

# zmiana nazwy kolumny
# alter table users rename column ege to age;

# dodanie tabeli person dla danych z pliku csv
# id,imie,nazwisko,wiek,miasto
# create table person (id INTEGER PRIMARY KEY, imie TEXT, nazwisko TEXT,  wiek INTEGER, miasto TEXT);

# .mode csv - tryb csv
# usuniecie danych z tabeli i sprzątanie
# sqlite> delete from person;
# sqlite> vacuum;
# sqlite>

# usunięcie tabeli
#  drop table if exists person;

#  .exit

# zaimportowanie danych do tabeli .import dane_person.csv person
#  select * from person where wiek > 60;
# select * from person where wiek < 25;
# select * from person where wiek BETWEEN 30 AND 40;
# sqlite> select * from person WHERE miasto = 'Lublin';
# 69|Inga|Sajda|61|Lublin
# 80|Aniela|Tomalak|24|Lublin

# select * from person WHERE miasto != 'Warszawa';
# select * from person order by nazwisko DESC;

# sqlite> select * from person order by wiek ASC;
# 36|Damian|Melka|18|Tychy
# 39|Rafał|Kafel|18|Mysłowice
# 40|Jan|Pusz|18|Olkusz

# sqlite> select avg(wiek) as sredni_wiek from person;
# 42.04

# sqlite> select count(*) as liczba_osob from person;
# 100

# liczba unikalnych miast w zbiorze
# sqlite> select count(DISTINCT miasto) as liczba_miast from person;
# 79

# srednia wieku dla każdego miasta
# sqlite> select miasto, AVG(wiek) as srednia from person group by miasto;
# Biała Podlaska|49.0
# Białystok|23.0
# Bielsko-Biała|36.5

# sqlite> select miasto, COUNT(*) as liczba from person group by miasto order by liczba DESC;
# Olkusz|3
# Gniezno|3
# Ząbki|2

# sqlite> SELECT miasto, ROUND(AVG(wiek), 2) AS srednia
#    ...> FROM person
#    ...> GROUP BY miasto;
# Biała Podlaska|49.0
# Białystok|23.0

# miasta, gdzie średnia wieku > 50
# sqlite> select miasto from person GROUP BY miasto HAVING AVG(wiek) > 50;
# Chorzów
# Cieszyn
# Dzierżoniów

# imiona zaczynajace sie na literkę S
# sqlite> select * from person where imie LIKE 'S%';
# 7|Sylwia|Lipowicz|67|Wejherowo
# 28|Szymon|Piestrzeniewicz|66|Cieszyn
# 52|Sonia|Maciejuk|56|Lubartów
# 59|Szymon|Niemira|62|Malbork
# 78|Sebastian|Pyć|19|Kędzierzyn-Koźle

# sqlite> select * from person where nazwisko like '%ow%';
# 5|Fryderyk|Kłosowicz|48|Gliwice
# 7|Sylwia|Lipowicz|67|Wejherowo

#  sqlite> select * from person where miasto like 'p%';
# 34|Liwia|Barłóg|37|Płock
# 53|Tola|Chojak|51|Puławy
# 58|Robert|Kopciuch|33|Pabianice
# 71|Maciej|Męcik|37|Poznań
# 86|Marianna|Rutowicz|18|Płońsk

# sqlite> select imie, wiek from person;
# Fabian|58
# Marcin|54

# 5 najstarszych osób
# sqlite> select * from person order by wiek DESC LIMIt 5;
# 6|Monika|Szkoda|70|Tychy
# 13|Nicole|Grzywnowicz|70|Tczew
# 65|Ida|Pleskot|70|Kętrzyn
# 15|Antoni|Wiekiera|68|Jaworzno
# 18|Kacper|Kuban|68|Lubin

# najmłodsze osoby z lublinia - limit 5
# sqlite> select * from person where miasto = 'Lublin' order by wiek ASC LIMIT 5;
# 80|Aniela|Tomalak|24|Lublin
# 69|Inga|Sajda|61|Lublin

import sqlite3

sql_connection = None

try:
    # sql_connection = sqlite3.connect(":memory:") # baza umieszczona w pamięci
    sql_connection = sqlite3.connect("sqlite_python.db")  # baza umieszczona w pamięci
    cursor = sql_connection.cursor()
    print("Baza danych została podłączona")
except sqlite3.Error as e:
    print("Bład bazy danych:", e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza danych została zamknięta")

# Baza danych została podłączona
# Baza danych została zamknięta
