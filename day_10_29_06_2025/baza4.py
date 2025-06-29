import sqlite3

sql_connection = None
lista = []
try:
    # sql_connection = sqlite3.connect(":memory:") # baza umieszczona w pamięci
    sql_connection = sqlite3.connect("sqlite_python.db")  # baza umieszczona w pamięci
    sql_connection.row_factory = sqlite3.Row  # baza zwróci dane jako słownik
    cursor = sql_connection.cursor()
    print("Baza danych została podłączona")

    select = """
    SELECT * FROM software;
    """

    for row in cursor.execute(select):
        print(row)  # <sqlite3.Row object at 0x102b57040>
        lista.append(dict(row))  # sqlite3.Row pozwala zrobic z danych słownik

    print(lista)
    # [{'id': 1, 'name': 'Python', 'price': 100.0}, {'id': 2, 'name': 'Java', 'price': 1000.0},
    #  {'id': 3, 'name': 'C++', 'price': 12000.0}]

    cursor.execute(select)
    rows = cursor.fetchall()
    for row in rows:
        print(dict(row))
    # {'id': 1, 'name': 'Python', 'price': 100.0}
    # {'id': 2, 'name': 'Java', 'price': 1000.0}
    # {'id': 3, 'name': 'C++', 'price': 12000.0}
except sqlite3.Error as e:
    print("Bład bazy danych:", e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza danych została zamknięta")
# Przerwa 13:40