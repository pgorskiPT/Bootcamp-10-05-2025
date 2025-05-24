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

podatek = 0.9
zarobki = int(input("Podaj dochód"))
# pop ierwszym spełnionym warunku wychodzi z drzewka
# kolejnośc warunków ma znaczenie
# elif - używamy po to by sprawdzić dokładnie jeden warunek
if zarobki < 10000:
    podatek = 0.0
elif zarobki < 30_000:
    podatek = 0.2
elif zarobki < 100_000:
    podatek = 0.4
else:  # działannie domyślne
    podatek = 0.9

print(f"Płacisz {zarobki * podatek} podatek")

# tu ostatni nadpisze poprzednie jesli będzie spełniony
if zarobki < 10000:
    podatek = 0

if zarobki < 1999:
    podatek = 0.4
# Przerwa do 11:20
