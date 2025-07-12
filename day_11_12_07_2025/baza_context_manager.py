# context manager - narzędzie usprawniające pracę z np.: plikami
# with
# __enter__ - wykonuje się przy urchomieni
# __exit__ - wykonuje sie przy wyjściu
import sqlite3
from pprint import pprint


class SQLiteDBContextManager:
    def __init__(self, db_name):
        """
        Metoda inicjalizująca, konstruktor
        :param db_name:
        """
        self.db_name = db_name
        self.conn = None

    def __enter__(self):  # wykonuje się przed zadaniem
        self.conn = sqlite3.connect(self.db_name)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):  # wykonuje się zawsze
        if self.conn:
            self.conn.commit()
            self.conn.close()


db_name = "my_data.db"
lista = []

with SQLiteDBContextManager(db_name) as conn:  # __enter__ zwróci nam połaczenie
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, name TEXT);")
    cursor.execute("INSERT INTO users (name) VALUES (?);", ("John",))
    cursor.execute("INSERT INTO users (name) VALUES (?);", ("Alice",))
    cursor.execute("INSERT INTO users (name) VALUES (?);", ("Tom",))
    cursor.execute("INSERT INTO users (name) VALUES (?);", ("Radek",))

    select = cursor.execute("SELECT * FROM users;")
    for i in select:
        print(i)
        lista.append(i)

# (1, 'John')
# (2, 'Alice')
# (3, 'John')
# (4, 'Alice')
# (5, 'John')
# (6, 'Alice')
# (7, 'John')
# (8, 'Alice')
# (9, 'Tom')
# (10, 'Radek')
# (11, 'John')
# (12, 'Alice')
# (13, 'Tom')
# (14, 'Radek')
print(lista)
# [(1, 'John'), (2, 'Alice'), (3, 'John'), (4, 'Alice'), (5, 'John'), (6, 'Alice'), (7, 'John'), (8, 'Alice'),
# (9, 'Tom'), (10, 'Radek'),
# (11, 'John'), (12, 'Alice'), (13, 'Tom'), (14, 'Radek'), (15, 'John'), (16, 'Alice'), (17, 'Tom'), (18, 'Radek')]
pprint(lista)