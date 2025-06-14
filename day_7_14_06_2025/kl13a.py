# pickle - serializacja i deserializacja obiektów
import ast
import pickle

lista = [1, 2, 3, 4, 5]

# zapisac listę do pliku
# odczytac listę z pliku
# sprawdzic typ

with open('lista.txt', "w") as f:
    f.write(str(lista))

with open('lista.txt', "r") as f:
    lines = f.read()

print(lines)  # [1, 2, 3, 4, 5]
print(type(lines))  # <class 'str'>

lista_odczytane_eval = eval(lines)
print(type(lista_odczytane_eval))  # <class 'list'>
print(lista_odczytane_eval[0])  # 1

with open("lista.pickle", "wb") as f:
    pickle.dump(lista, f)  # zapis listy do pliku w postaci bajtowej

with open('lista.pickle', "rb") as fh:
    p = pickle.load(fh)

print(p)  # [1, 2, 3, 4, 5]
print(type(p))  # <class 'list'>
print(p[0])  # 1

# zamian alisty na bajty
list_ser = pickle.dumps(lista)
print(list_ser)
# b'\x80\x04\x95\x0f\x00\x00\x00\x00\x00\x00\x00]\x94(K\x01K\x02K\x03K\x04K\x05e.'

# zmiana bajtów na listę
wynik = pickle.loads(list_ser)
print("Wynik deserializacji:", wynik)  # Wynik deserializacji: [1, 2, 3, 4, 5]
print(type(wynik))  # <class 'list'>

user_input = "print('hacked')"
eval(user_input)  # hacked

lines = "[1 , 2, 3, 4]"
lista = ast.literal_eval(lines)
print(lista)
print(type(lista))
# [1, 2, 3, 4]
# <class 'list'>
