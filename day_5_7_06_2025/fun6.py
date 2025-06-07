# fukcja, która oblicza średnią
def srednia(name=None, *cyfry):  # dowolna ilość argumentów pozycyjnych
    print(cyfry)
    count = len(cyfry)
    suma = 0
    sum_p = sum(cyfry)
    try:
        for c in cyfry:
            suma += c
        avg = suma / count
        avg_p = sum_p / count
    except Exception as e:
        print("Bład", e)
    else:
        print(f"Średnia dla ucznia {name} wynosi {avg}")
        print(f"Średnia dla ucznia {name} wynosi {avg_p}")
    finally:
        print("Następne obliczenie")


srednia()  # ()
srednia(5, 5, 5, 5, 5, 5, 5)  # (5, 5, 5, 5, 5, 5, 5)
# ()
# Bład division by zero
# Następne obliczenie
# (5, 5, 5, 5, 5, 5, 5)
# Średnia wynosi 5.0
# Następne obliczenie
# ()
# Bład division by zero
# Następne obliczenie
# (5, 5, 5, 5, 5, 5, 5)
# Średnia wynosi 5.0
# Średnia wynosi 5.0
# Następne obliczenie
name, *oceny = ("Radek", 3, 4, 5, 6, 5, 5, 5, 4)
srednia("Radek", 3, 4, 5, 6, 5, 5, 5, 4)
# ()
# Bład division by zero
# Następne obliczenie
# (5, 5, 5, 5, 5, 5)
# Średnia dla ucznia 5 wynosi 5.0
# Średnia dla ucznia 5 wynosi 5.0
# Następne obliczenie
# (3, 4, 5, 6, 5, 5, 5, 4)
# Średnia dla ucznia Radek wynosi 4.625
# Średnia dla ucznia Radek wynosi 4.625
# Następne obliczenie
