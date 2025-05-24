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

password = input("Podaj hasło")
while password != 'secret':
    password = input("Błędne hasło. podaj ponownie")
print("Hasło prawidłowe")
# Podaj hasłosadfa
# Błędne hasło. podaj ponownieasdasfa
# Błędne hasło. podaj ponownieeafafa
# Błędne hasło. podaj ponowniesecret
# Hasło prawidłowe
