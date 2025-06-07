def connect(**opcje):  # ** argumenty nazwane, argumenty słownikowe
    print(opcje)
    print(type(opcje))  # <class 'dict'>
    param = {
        'host': '127.0.0.1',
        'port': '8080'
    }
    param.update(opcje)
    print(param)  # {'host': '127.0.0.1', 'port': '8080', 'a': 9, 'name': 'Radek'}
    param['pwd'] = opcje
    print(param)
    # {'host': '127.0.0.1', 'port': '8080', 'a': 9, 'name': 'Radek', 'pwd': {'a': 9, 'name': 'Radek'}}


connect()  # {}
connect(z=9)  # {'z': 9}
connect(a=9, name="Radek")  # {'a': 9, 'name': 'Radek'}
