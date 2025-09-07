import numpy as np

arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]

newarr = arr[x]  # zastosowaliśmy maske
print(newarr)  # [41 43]

arr = np.array([41, 42, 43, 44])
filter_arr = []

for element in arr:
    if element > 42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

newarr = arr[filter_arr]
print(filter_arr)
print(newarr)  # [43 44]

arr = np.array([41, 42, 43, 44])
filter_arr = arr > 42
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)
# [False False  True  True]
# [43 44]

arr = np.arange(21)
even = arr[arr % 2 == 0]  # modulo, częsć całkowita
print("Parzyste:", even)
# Parzyste: [ 0  2  4  6  8 10 12 14 16 18 20]

arr = np.random.randint(0, 100, size=100)

mean_values = np.mean(arr)  # średnia
print(mean_values)  # 52.56
grather_than_mean = arr[arr > mean_values]
print("Średnia:", mean_values)
print("Wartości większe od średniej:", grather_than_mean)
# Średnia: 51.84
# Wartości większe od średniej: [89 70 56 97 76 65 91 93 55 57 66 83 90 99 64 54 90 83 65 64 69 52 75 93
#  97 96 82 52 98 63 60 86 64 93 57 71 74 67 99 98 75 78 68 88 62 89 72 91
#  89 56 68 66 67]

arr = np.array([1, 2, np.nan, 4, np.nan, 6, 7])
print(arr)  # [ 1.  2. nan  4. nan  6.  7.]  # nan -> None

filtered_arr = arr[~np.isnan(arr)]
print("Tablica bez NaN:", filtered_arr)  # Tablica bez NaN: [1. 2. 4. 6. 7.]

arr = np.random.random((5, 5))
print(arr)
print(arr.shape)  # (5, 5)

filtered_arr = arr[arr > 0.5]
print("Większe od 0.5", filtered_arr)
# Większe od 0.5 [0.70065522 0.70337354 0.8532293  0.58479645 0.63809561 0.83010815
#  0.53911956 0.57718572 0.91304649 0.72726845 0.68640667 0.66156896
#  0.79801535 0.70115897 0.5284332 ]
print(filtered_arr.shape)  # (11,)
