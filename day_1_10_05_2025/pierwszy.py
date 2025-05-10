import sys

print()  # wypisz/wydrukuj

print("Nazywam się Radek")  # Nazywam się Radek
print("Nazywam się Radek")  # Nazywam się Radek
print("Nazywam się Radek")  # Nazywam się Radek
print("Nazywam się Radek")  # Nazywam się Radek
print("Nazywam się Radek")  # Nazywam się Radek
print("Nazywam się Radek")  # Nazywam się Radek
print("Nazywam się Radek")  # Nazywam się Radek
# ctrl d - powielanie lini z kursorem
# Reformat code ⌥ ⌘ L
# Nazywam się Radek
# Nazywam się Radek
# Nazywam się Radek
# Nazywam się Radek
# Nazywam się Radek
# Nazywam się Radek
# Nazywam się Radek
print('Nazywam się Radek')  # Nazywam się Radek
# Process finished with exit code 0 - program wykona się bez błędu

# ctrl / - wstawienie komentarza
# print("Nazywam się Radek')
#   File "/Users/radoslawjaniak/PycharmProjects/Bootcamp-10-05-2025/day_1_10_05_2025/pierwszy.py", line 22
#     print("Nazywam się Radek')
#           ^
# SyntaxError: unterminated string literal (detected at line 22)
print("Dalej")

# type() - sprawdzenie typu danych
print(type("Radek"))  # <class 'str'> - string, dane tekstowe
print("39" + "14")  # konkattenacja, łączenie tekstów 3914

# print("39" + 14) # TypeError: can only concatenate str (not "int") to str
# silne typowanie - nie zmienia typów podczas operacji
print(type(14))  # <class 'int'>, liczby calkowite

print("39" + str(14))  # 3914 str() - rzutowanie na stringa

print(39 + 14)  # 53
print(int("39") + 14)  # 53, int() - rzutowanie na int

print(5 * "4")  # 44444
print(35 * 168)
print(35 * "168")
# 5880
# 168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168

# zakres int
print(sys.int_info)
# sys.int_info(bits_per_digit=30,
#              sizeof_digit=4,
#              default_max_str_digits=4300,
#              str_digits_check_threshold=640)
# w 64 bit pythonie liczba maksymalnie jaka zmiesci sie w pamięci

# zmienna - pudełko na dane
# typowanie dynamiczne - typ zmiennej jest określany na podsatwie typu danych jakie do niej wrzucimy
# konwencja nazewnicza - snake_case
# camelCase, PascalCase, kebab-case - inne konwencje

# PEP8 - nazwa zmiennej powinna podpowiadac, co przechowuje
name = "Radek"  # wpisanie wartości do zmiennej
print(type(name))  # <class 'str'>
print(name)  # Radek - wypisanie wartości

name_info: str = "Maciek"  # podpowiedz dla programisty
# to nie jest deklaracja typu!!!
print(name_info)
print(type(name_info))
# Maciek
# <class 'str'>
name_info = 90
print(name_info)
print(type(name_info))
# 90
# <class 'int'>
# pip install mypy skrypt sprawdzajacy typy
# cd day_1_10_05_2025 - zmiana katalogu
# (.venv) radoslawjaniak@mac day_1_10_05_2025 % mypy pierwszy.py
# pierwszy.py:75: error: Incompatible types in assignment (expression has type "int", variable has type "str")  [assignment]
# Found 1 error in 1 file (checked 1 source file)
# (.venv) radoslawjaniak@mac day_1_10_05_2025 %

age = 48
print(age)
print(type(age))

age = "Radek"
# print(age + name_info) # TypeError: can only concatenate str (not "int") to str
print(int("48") + name_info)  # 138
