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
