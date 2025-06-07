# zrobic funkcję restauracja()
# zamow_pizza, zamow_napoj
# w zależności od zamówienia ma zwrócic odpowiednią funkcję
# użyc tych funkcji w głównym programmie

def restauracja(typ_zamowienia):
    print("Witamy w naszej restauracji")

    def zamow_pizza(skladniki="pieczarki"):
        print("Zamówiono pizza, skłądniki:", skladniki)

    def zamow_napoj(nazwa="herbata"):
        print('Zamow napoj:', nazwa)

    if typ_zamowienia.casefold().strip() == 'pizza':
        return zamow_pizza
    else:
        return zamow_napoj


zamowienie_pizza = restauracja('pizza')
zamowienie_pizza()
# Witamy w naszej restauracji
# Zamówiono pizza, skłądniki: pieczarki
zamowienie_pizza("pieczarki, szynka")
# Zamówiono pizza, skłądniki: pieczarki, szynka

zamowienie_napoj = restauracja('napoj')
zamowienie_napoj()
zamowienie_napoj('cola')
# Witamy w naszej restauracji
# Zamow napoj: herbata
# Zamow napoj: cola

zamowienie_pizza()
zamowienie_napoj()
zamowienie_napoj()
# Zamówiono pizza, skłądniki: pieczarki
# Zamow napoj: herbata
# Zamow napoj: herbata
# Przerwa 11:15
