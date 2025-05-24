# while - sterowana warunkiem

# pętla nieskończona
# while True:
#     print("Komunikat !!!")

licznik = 0
while True:
    print("Komunikat 1 !!")
    licznik += 1
    if licznik > 15:
        break  # przerywa pętlę

print(licznik)  # 16
licznik = 0
while licznik < 15:
    licznik += 1
    print("Komunikat 2 !!!")

# password = input("Podaj hasło")
# while password != 'secret':
#     password = input("Błędne hasło. podaj ponownie")
# print("Hasło prawidłowe")
# Podaj hasłosadfa
# Błędne hasło. podaj ponownieasdasfa
# Błędne hasło. podaj ponownieeafafa
# Błędne hasło. podaj ponowniesecret
# Hasło prawidłowe

lista = []
lista_int = []
while True:
    wej = input("Podaj liczbę")
    # A string is numeric if all characters in the string are numeric
    if not wej.isnumeric():
        break
    lista.append(wej)
    lista_int.append(int(wej))

print(lista)  # ['1', '2', '3', '4', '5', '6']
print(lista_int)  # [1, 2, 3, 4, 5, 6]

my_list = [1, 5, 2, 3, 5, 4, 5, 6, 5]
element_to_remove = 5
while element_to_remove in my_list:
    my_list.remove(element_to_remove)

print(my_list)  # [1, 2, 3, 4, 6]
