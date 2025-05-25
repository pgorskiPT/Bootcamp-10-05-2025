# napisac program kalkulator z wykorzystaniem pętli while True
# przechwycić wyjątki i obsłużyc
# ładnie wypisać wynik np.: Dodawanie 2 + 4 = 6

# wyswietlic menu z działaniami
# pobrac dane
# wyświetlic wynik wybranego działania
# ```python```

while True:
    print("""
    1. Dodawanie
    2. Odejmowanie
    3. Mnożenie
    4. Dzielenie
    5. Koniec
    """)

    odp = input("Podaj opcje menu")  # str
    if odp not in ["1", "2", "3", "4"]:
        break
    try:
        a = float(input("Podaj pierwszą liczbę"))
        b = float(input("Podaj drugą liczbę"))

        if odp == "1":
            print(f"Wynik dodawania {a} + {b} = {a + b}")
        elif odp == "2":
            print(f"Wynik odejmowania {a} - {b} = {a - b}")
        elif odp == "3":
            print(f"Wynik mnożenia {a} * {b} = {a * b}")
        elif odp == "4":
            print(f"Wynik dzielenia {a} / {b} = {a / b}")
    except ZeroDivisionError:
        print("Nie dziel przez zero!!!")
    except Exception as e:
        print("Bład", e)
    else:
        print("Działąnie wykonane poprawnie")
