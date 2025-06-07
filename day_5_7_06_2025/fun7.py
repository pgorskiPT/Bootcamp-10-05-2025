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


def connect_all(*args, **kwargs):
    print(args, kwargs)


connect_all()  # () {}
connect_all(1, 2, 3)  # (1, 2, 3) {}
connect_all(1, 2, 3, 4, 5, 6)  # (1, 2, 3, 4, 5, 6) {}
connect_all(1, 2, 3, 4, 5, 6, "Zenek")  # (1, 2, 3, 4, 5, 6, 'Zenek') {}
connect_all(1, 2, 3, 4, 5, 6, "Zenek", a=9, b=89)  # (1, 2, 3, 4, 5, 6, 'Zenek') {'a': 9, 'b': 89}
connect_all(d=9, name="Tomek")  # () {'d': 9, 'name': 'Tomek'}
# connect_all(c=9, 1, 2, 3, 4) # SyntaxError: positional argument follows keyword argument
