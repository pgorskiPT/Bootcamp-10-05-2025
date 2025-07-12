import mysql.connector
from mysql.connector import Error

# mariadb - fork mysql

# pip list - lista zainstalowanych pakietów pythona
# pip install mysql-connector-python

try:
    connection = mysql.connector.connect(
        host='',
        port=3306,  # standartowy port dla mysql=3306
        database='',
        user='',
        password=''
    )

    if connection.is_connected():
        # db_info = connection.get_server_info()
        db_info = connection.server_info  # nowsze podejście
        print("Połączono z serwers MySql w wersji:", db_info)

        cursor = connection.cursor()
        cursor.execute("select database();")

        record = cursor.fetchone()
        print('Połaczenie z bazą danych:', record)
except Error as e:
    print("Bład podczas połaczenia do bazy danych MySQL:", e)
finally:
    if connection.is_connected():
        connection.close()
        print("Połączenie z MySQL zostało zamknięte")
# Połączono z serwers MySql w wersji: 8.0.33-25
# Połaczenie z bazą danych: ('37970432_dane_mysql',)
# Połączenie z MySQL zostało zamknięte
