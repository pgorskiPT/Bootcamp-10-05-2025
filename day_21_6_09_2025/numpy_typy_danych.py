import numpy as np

arr = np.array([1, 2, 3, 4])
# odczytanie typu danych
print(arr.dtype)  # int64

print(np.iinfo(np.int64).min)
print(np.iinfo(np.int64).max)
# int64
# -9223372036854775808
# 9223372036854775807

# int16 = -32768 do 32767
# int8 = -128 do 127
# uint8 = 0 do 255 bez znaku, tylko wartości dodatnie
print(2 ** 10)  # 1024

arr_str = np.array(['apple', 'banana', 'cherry'])
print(arr_str.dtype)  # <U6, unicode, 6 znaków maksymalnie, < - little-endian

# stworzenie listy okreslonego typu
arr_own = np.array([1, 2, 3, 4], dtype="S")
print(arr_own.dtype)  # |S1
print(arr_own)  # [b'1' b'2' b'3' b'4']

arr_i4 = np.array([1, 2, 3, 4], dtype='i4')
print(arr_i4)  # [1 2 3 4]
print(arr_i4.dtype)  # int32

# arr_err = np.array(['a', "2", "3"], dtype="i")
# ValueError: invalid literal for int() with base 10: 'a'

arr_float = np.array([1.1, 2.1, 3.1, 4.1])
print(arr_float)
print(arr_float.dtype)
# [1.1 2.1 3.1 4.1]
# float64
print(np.finfo(np.float64))
# tiny =       2.2250738585072014e-308
# max =        1.7976931348623157e+308

print(arr)  # [1 2 3 4]
print(arr.dtype)  # int64
newarr = arr.astype("i")
print(newarr.dtype)  # int32

new_arr = arr.astype(int)
print(new_arr)
print(new_arr.dtype)  # [1 2 3 4]
# int64

arr_bool = np.array((1, 0, 3))
new_arr_bool = arr_bool.astype(bool)
print(new_arr_bool)  # [ True False  True]
print(new_arr_bool.dtype)  # bool

arr_float_2 = np.array([1.2, 2.2, 3.3, 4.4, 5.8])
print(arr_float_2.dtype)
print(arr_float_2)
# float64
# [1.2 2.2 3.3 4.4 5.5]
print("Konwersja na int32:", arr_float_2.astype("int32"))  # Konwersja na int32: [1 2 3 4 5]
print("Konwersja na int32:", arr_float_2.astype("int32").dtype)  # Konwersja na int32: int32

print("Konwersja na float16:", arr_float_2.astype("float16"))  # Konwersja na float16: [1.2 2.2 3.3 4.4 5.5]
print("Konwersja na float16:", arr_float_2.astype("float16").dtype)  # Konwersja na float16: float16

print('Konwersja na bool:', arr_float_2.astype("bool"))  # Konwersja na bool: [ True  True  True  True  True]
print('Konwersja na bool:', arr_float_2.astype("bool").dtype)  # Konwersja na bool: bool

print("Konwersja na U6:", arr_float_2.astype("U6"))  # Konwersja na U6: ['1.2' '2.2' '3.3' '4.4' '5.5']
print("Konwersja na U6:", arr_float_2.astype("U6").dtype)  # Konwersja na U6: <U6

print('konwersja na uint8:', arr_float_2.astype("uint8"))  # konwersja na uint8: [1 2 3 4 5]
print('konwersja na uint8:', arr_float_2.astype("uint8").dtype)  # konwersja na uint8: uint8
# uint8 255 + 255 = 512
# # numpy typy danych
# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type ( void )