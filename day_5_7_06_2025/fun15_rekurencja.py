# funkcja rekurencyjna
# funkcja wywołuje samą siebie
# zalety - kompaktowy zapis, łatwe uniezależnienie od danych
# wady - zuzżycie pamięci, mozę nigdy nie zakońćzyć działania, trudny w debugowaniu
def add(num):
    if num == 0:
        return 0
    else:
        return num + add(num - 1)


print(add(5))  # 5 + 4 + 3 + 2 + 1, 15


def factorial(num):
    if num <= 1:
        return 1
    else:
        return num * factorial(num - 1)


print(factorial(5))  # 120


def nwd(a, b):
    if b == 0:
        return a
    else:
        return nwd(b, a % b)


print(nwd(48, 18))
print(48 % 18)  # 12
print(18 % 12)  # 6
print(12 % 6)  # 0 -> wynik 6
