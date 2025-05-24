# instrukcje warunkowe
# instrukcje sterowania przepływem programu
# if - sterowana warunkiem
# if warunek:
#   komenda(blok) wykonywanay gdy warunek spełniony

odp = True
print(bool(odp))  # True
odp = False
# debug - tryb do uruchamiania programu linijka po linijce
# daje możliwość weryfikacji wartości zmiennych i parametrów pythona
if odp:
    # blok wykonywany gdy warunek spełniony
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")

print("Dalsza częśc programu")
# True
# Dalsza część programu

odp = "Radek"
if odp:
    print("ok")  # ok

odp = "Tomek"
if odp == "Radek":
    print("Radek")
else:  # w przeciwnym przypadku
    print("Inny pacjent")  # Inny pacjent

# podatek = 0.9
# zarobki = int(input("Podaj dochód"))
# # pop ierwszym spełnionym warunku wychodzi z drzewka
# # kolejnośc warunków ma znaczenie
# # elif - używamy po to by sprawdzić dokładnie jeden warunek
# if zarobki < 10000:
#     podatek = 0.0
# elif zarobki < 30_000:
#     podatek = 0.2
# elif zarobki < 100_000:
#     podatek = 0.4
# else:  # działannie domyślne
#     podatek = 0.9
#
# print(f"Płacisz {zarobki * podatek} podatek")
#
# # tu ostatni nadpisze poprzednie jesli będzie spełniony
# if zarobki < 10000:
#     podatek = 0
#
# if zarobki < 1999:
#     podatek = 0.4
# # Przerwa do 11:20

suma_zam = 250
if suma_zam > 150:
    rabacik = 25
else:
    rabacik = 0

print(f"Rabat wynosi {rabacik}")  # Rabat wynosi 25

rabat = 25 if suma_zam > 150 else 0
print(f"Rabat wynosi {rabat}")  # Rabat wynosi 25

# zasymuluj system zbierania logów
# w zmiennej otrzymamy typ systemu: console, email, inny
# w zależności od zawartości zmiennej:
# console -> "Stało się coś strasznego"
# email -> "System email"
# jezeli będzie to system email to należy do listy błedów dodać opis
# druga zmienna przechowuje typ błedu
# error, medium, inny
alert_system = "email"
error = "error"
lista_b = []

if alert_system == "console":
    print("Stało się coś strasznego")
elif alert_system == "email":
    print("System email")
    if error == "error":
        lista_b.append("Krytyczny")
    elif error == "medium":
        lista_b.append("Ostrzeżenie")
    else:
        lista_b.append('Inny')
else:
    print('Inny system')
print(lista_b)  # ['Krytyczny']
# Stało się coś strasznego
# []

alert_dict = {'console': "Coś poszło nie tak",
              'email': {'error': "Krytyczny", "medium": "Ostrzeżenie"}}

if alert_system in alert_dict:
    if alert_system == 'console':
        print(alert_dict.get(alert_system))
    elif alert_system == 'email':
        print("System email")
        print(alert_dict.get(alert_system))
        if error in alert_dict[alert_system]:
            errors = alert_dict[alert_system]  # {'error': 'Krytyczny', 'medium': 'Ostrzeżenie'}
            print(errors[error])
else:
    print("Inny system")
# Krytyczny
