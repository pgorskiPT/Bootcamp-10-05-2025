import sqlite3

sql_connection = None

try:
    # sql_connection = sqlite3.connect(":memory:") # baza umieszczona w pamięci
    sql_connection = sqlite3.connect("sqlite_python.db")  # baza umieszczona w pamięci
    sql_connection.row_factory = sqlite3.Row
    cursor = sql_connection.cursor()
    print("Baza danych została podłączona")

    # table_data = 'software'
    table_data = 'hardware'

    select = f"SELECT * FROM {table_data};"

    cursor.execute(select)
    rows = cursor.fetchall()
    for row in rows:
        print(dict(row))

except sqlite3.Error as e:
    print("Bład bazy danych:", e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza danych została zamknięta")
# Baza danych została podłączona
# {'id': 2, 'name': 'Java', 'price': 1000.0}
# {'id': 3, 'name': 'C++', 'price': 12000.0}
# {'id': 4, 'name': 'Scala', 'price': 5600.0}
# {'id': 5, 'name': 'Rust', 'price': 899.0}
# {'id': 6, 'name': 'Angular', 'price': 1899.0}
# {'id': 7, 'name': 'JS', 'price': 1999.0}
# Baza danych została zamknięta

# Execution finished without errors.
# Result: query executed successfully. Took 0ms, 1 rows affected
# At line 1:
# INSERT  INTO hardware (id,name,price) VALUES (1,'Samsung',1999) ;

# Baza danych została podłączona
# {'id': 1, 'name': 'Samsung', 'price': 1999.0}
# Baza danych została zamknięta

# -----
# Baza danych została podłączona
# {'id': 1, 'name': 'Samsung', 'price': 1999.0}
# {'id': 2, 'name': 'Apple', 'price': 2999.0}
# {'id': 3, 'name': 'Redmi', 'price': 999.0}
# Baza danych została zamknięta
