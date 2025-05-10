user = "Tomek"  # str
wiek = 39  # int
wersja = 3.900001  # <class 'float'> liczby zmiennoprzecinkowe
print(type(wersja))  # <class 'float'>
liczba = 890123456345123  # int

print("Witaj %s masz teraz %d lat" % (user, wiek))  # Witaj Tomek masz teraz 39 lat
# Sprawdza typy danych
# print("Witaj %d masz teraz %s lat" % (user, wiek)) # TypeError: %d format: a real number is required, not str
# %d: formatowanie liczb całkowitych
# %f: formatowanie liczb zmiennoprzecinkowych
# %s - łańcuch znaków (string)

print("Witaj %(user)s, masz teraz %(wiek)d lat" % {'user': user, "wiek": wiek})
# Witaj Tomek, masz teraz 39 lat
print("Witaj %(user)s, masz teraz %(age)d lat" % {'user': user, "age": wiek})
# Witaj Tomek, masz teraz 39 lat
print("Witaj %(user)s, masz teraz %(age)d lat, miło cię widzieć %(user)s" % {'user': user, "age": wiek})
# Witaj Tomek, masz teraz 39 lat, miło cię widzieć Tomek

# zrobić za pomocą f-string
print(f"Witaj {user}, masz teraz {wiek} lat. Miło Cię widzieć {user}.")
# Witaj Tomek, masz teraz 39 lat. Miło Cię widzieć Tomek.

# nie sprawdza typów
print(f"Witaj {wiek}, masz teraz {wiek} lat. Miło Cię widzieć {user}.")
# Witaj 39, masz teraz 39 lat. Miło Cię widzieć Tomek.

print("Używamy wersji Pythona %i" % 3)  # Używamy wersji Pythona 3
print("Używamy wersji Pythona %f" % 3)  # Używamy wersji Pythona 3.000000
print("Używamy wersji Pythona %f" % 3.9)  # Używamy wersji Pythona 3.900000
print("Używamy wersji Pythona %.2f" % 3.9)  # Używamy wersji Pythona 3.90
print("Używamy wersji Pythona %.1f" % 3.9)  # Używamy wersji Pythona 3.9
print("Używamy wersji Pythona %.0f" % 3.9)  # Używamy wersji Pythona 4 - zaokrąglił przy wyświetlaniu
print("Używamy wersji Pythona %.f" % 3.9)  # Używamy wersji Pythona 4

x = 3.99
print("Liczba %.f" % x)  # Liczba 4 zaokrąglił przy wyświetlaniu
print("Liczba się nie zmieniła", x)  # liczba się nie zmieniła

# zaokrąglienie matematyczne
x = round(x)
print("Liczba po zaokrągleniu", x)  # Liczba po zaokrągleniu 4

x = 3.14157890
x = round(x, 2)
print("Liczba zokrąglona do dwóch miejsc po przecinku", x)  # Liczba zokrąglona do dwóch miejsc po przecinku 3.14

print(f"Uzywamy wersji Pythona {wersja}")  # Uzywamy wersji Pythona 3.900001
print(f"Uzywamy wersji Pythona {wersja:.1f}")  # Uzywamy wersji Pythona 3.9
print(f"Uzywamy wersji Pythona {wersja:.2f}")  # Uzywamy wersji Pythona 3.90
print(f"Uzywamy wersji Pythona {wersja:.0f}")  # Uzywamy wersji Pythona 4

print(liczba)  # 890123456345123

print(f"Nasza duża liczba {liczba:,}")  # Nasza duża liczba 890,123,456,345,123
print(f"Nasza duża liczba {liczba:_}")  # Nasza duża liczba 890_123_456_345_123

# zamienic na spacje, kropke
print(f"Nasza duża liczba {liczba:,}".replace(",", "."))  # Nasza duża liczba 890.123.456.345.123
print(f"Nasza duża liczba {liczba:,}".replace(",", " "))  # Nasza duża liczba 890 123 456 345 123

parametr = 15000000000
parametr = 15_000_000_000  # ułatwienie dla programisty
print(parametr)  # 15000000000
print(type(parametr))  # <class 'int'>

print(f"{user:>10}")  # "     Tomek" - wyrównaj do prawej - 10 znaków
print(f"{user:<15}")  # "Tomek          " - wyrównaj do lewej
print(f"{user:^20}")  # "       Tomek        " - centruj

tekst = "jeden dwa trzy cztery"
# podział tekstu po znaku " "
print(tekst.split())  # ['jeden', 'dwa', 'trzy', 'cztery']

tekst2 = "jeden, dwa, trzy, cztery"
print(tekst2.split(","))
# ['jeden', ' dwa', ' trzy', ' cztery']
print(tekst2.split(", "))  # ['jeden', 'dwa', 'trzy', 'cztery']
