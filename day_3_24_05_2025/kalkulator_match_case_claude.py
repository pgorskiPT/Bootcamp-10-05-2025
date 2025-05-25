while True:  # 1. Tworzymy nieskończoną pętlę – program działa, dopóki nie przerwiemy (break)
    print("""
    1. Dodawanie
    2. Odejmowanie
    3. Mnożenie
    4. Dzielenie
    5. Koniec
    """)  # 2. Wyświetlamy użytkownikowi menu z dostępnymi opcjami

    odp = input("Podaj opcję menu: ")  # 3. Pobieramy od użytkownika wybór opcji z menu (jako tekst)

    match odp:  # 4. Sprawdzamy, jaką opcję wybrał użytkownik, przy pomocy match-case (od Python 3.10)
        case "5":
            break  # 5. Jeśli użytkownik wpisał "5" (Koniec), przerywamy pętlę i kończymy program
        case "1" | "2" | "3" | "4":  # 6. Jeśli użytkownik wybrał jedną z opcji od 1 do 4
            try:  # 7. Próbujemy wykonać poniższy blok (obsługa błędów)
                a = float(input("Podaj pierwszą liczbę: "))  # 8. Pobieramy pierwszą liczbę i zamieniamy na typ float
                b = float(input("Podaj drugą liczbę: "))    # 9. Pobieramy drugą liczbę i zamieniamy na typ float
                match odp:  # 10. Ponownie sprawdzamy, którą operację użytkownik wybrał
                    case "1":
                        print(f"Wynik dodawania {a} + {b} = {a + b}")  # 11. Dodawanie
                    case "2":
                        print(f"Wynik odejmowania {a} - {b} = {a - b}")  # 12. Odejmowanie
                    case "3":
                        print(f"Wynik mnożenia {a} * {b} = {a * b}")  # 13. Mnożenie
                    case "4":
                        if b == 0:  # 14. Przed dzieleniem sprawdzamy, czy dzielnik to zero
                            raise ZeroDivisionError  # 15. Jeśli tak, generujemy wyjątek (błąd dzielenia przez zero)
                        print(f"Wynik dzielenia {a} / {b} = {a / b}")  # 16. Jeśli dzielnik różny od zera – wykonujemy dzielenie
            except ZeroDivisionError:  # 17. Obsługa błędu dzielenia przez zero
                print("Nie dziel przez zero!!!")
            except Exception as e:  # 18. Obsługa innych, nieprzewidzianych błędów (np. nieprawidłowy typ danych)
                print("Błąd:", e)
            else:  # 19. Jeżeli nie wystąpił żaden błąd, wyświetlamy informację o poprawnym wykonaniu działania
                print("Działanie wykonane poprawnie")
        case _:  # 20. Każda inna opcja (poza 1-5) nieprawidłowy wybór
            print("Nieprawidłowa opcja, zakończenie programu.")  # 21. Komunikat o błędzie
            break  # 22. Przerywamy pętlę kończymy program