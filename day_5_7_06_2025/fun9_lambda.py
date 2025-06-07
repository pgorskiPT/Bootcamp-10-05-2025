# funkcja lambda
# skrócony zapis funkcji
# lambda zwraca wynik - return
# funkcja anonimowa - deklaracja w miejscu wykonania

odejmij = lambda a, b: a - b  # return
print(odejmij(6, 8))  # -2
print(odejmij(b=8, a=87))  # 79

addition = lambda a, b: a + b
print(addition(6, 7))  # 13
res = addition(7, 8)
print(f"Wynik dodawania {res}")  # Wynik dodawania 15

res = lambda *args: sum(args)
print(res(10, 20))  # 30

res = lambda **kwargs: sum(kwargs.values())
print(res(a=10, b=20))  # 30

product = lambda a, b: a * b
print(product(4, 5))  # 20


def product1(nums):
    total = 1
    for i in nums:
        total *= i
    return total


res1 = lambda **kwargs: product1(kwargs.values())
print(res1(a=10, b=90))  # 900


def my_func(n):
    return lambda a: a + n


add10 = my_func(10)
add20 = my_func(20)
add30 = my_func(30)

print(add10(5))  # 15
print(add20(5))  # 25
print(add30(5))  # 35

oblicz_vat = lambda cena, vat=23: cena * (100 + vat) / 100
print(oblicz_vat(1000))
print(oblicz_vat(1000, 8))

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosły")
print(wiek(9))  # dziecko
print(wiek(10))  # nastolatek
print(wiek(17))  # nastolatek
print(wiek(18))  # dorosły
print(wiek(25))  # dorosły
