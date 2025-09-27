from matplotlib import pyplot as plt

dane = [
    {"wiek": 55, "zarobki": 70, "decyzja": "tak"},
    {"wiek": 53, "zarobki": 50, "decyzja": "nie"},
    {"wiek": 47, "zarobki": 60, "decyzja": "tak"},
    {"wiek": 40, "zarobki": 30, "decyzja": "nie"},
    {"wiek": 35, "zarobki": 45, "decyzja": "tak"},
    {"wiek": 28, "zarobki": 65, "decyzja": "nie"},
    {"wiek": 31, "zarobki": 42, "decyzja": "tak"},
    {"wiek": 29, "zarobki": 50, "decyzja": "nie"},
    {"wiek": 52, "zarobki": 80, "decyzja": "tak"},
    {"wiek": 60, "zarobki": 55, "decyzja": "tak"},
]


# wskaznik giniego lub entropia (entropia - logarytmiczna - wolniejsza)
# funkcja Giniego (0 - dobrze)
def gini_index(dane):
    total = len(dane)
    if total == 0:
        return 0

    decyzje = [x['decyzja'] for x in dane]
    pozytywne = decyzje.count("tak") / total
    negatywne = decyzje.count("nie") / total
    gini = 1 - (pozytywne ** 2 + negatywne ** 2)
    return gini


def gini_po_podziale(lewa, prawa):
    total = len(lewa) + len(prawa)
    w1 = len(lewa) / total
    w2 = len(prawa) / total
    return w1 * gini_index(lewa) + w2 * gini_index(prawa)


def wypisz_grupe(nazwa, grupa):
    print(f"\n {nazwa} (liczba {len(grupa)})")
    print(f" tak:", sum(1 for x in grupa if x['decyzja'] == 'tak'))
    print(f" nie:", sum(1 for x in grupa if x['decyzja'] == 'nie'))
    print(f" Gini: {round(gini_index(grupa), 3)}")


# dzielimy wg wiek > 50
wiek_value = 50
wiek_lewo = [x for x in dane if x['wiek'] > wiek_value]
wiek_prawo = [x for x in dane if x['wiek'] <= wiek_value]

# obliczamy wskaźik giniego przed i po podziale
print("Gini (całość)", round(gini_index(dane), 3))
print("Gini po podziale (wiek >50)", round(gini_po_podziale(wiek_lewo, wiek_prawo), 3))
# Gini (całość) 0.48
# Gini po podziale (wiek >50) 0.45
# po podziale strata 0.03  - raczej ten parametr podziału jest w dobrą strone

wypisz_grupe("wiek > 50", wiek_lewo)
wypisz_grupe("wiek =< 50", wiek_prawo)
#  wiek > 50 (liczba 4)
#  tak: 3
#  nie: 1
#  Gini: 0.375
#
#  wiek =< 50 (liczba 6)
#  tak: 3
#  nie: 3
#  Gini: 0.5