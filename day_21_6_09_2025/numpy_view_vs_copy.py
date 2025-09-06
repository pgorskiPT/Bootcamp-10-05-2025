import numpy as np

# kopia tabeli
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)
# [42  2  3  4  5]
# [1 2 3 4 5] kopia się nie zmieniła
print(id(x), id(arr))  # 4336489872 4336488432
print(x.base is arr)  # False - nie jest widokiem, False

# widok
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr)
print(x)
# [42  2  3  4  5]
# [42  2  3  4  5] zmiana w obydwu tabelach
print(id(x), id(arr))  # 4367978480 4367980016
print(x.base is arr)  # True, jest widokiem do tabeli arr

arr = np.arange(10)
print(arr)  # [0 1 2 3 4 5 6 7 8 9]
view = arr[2:5]  # taki slice zwraca widok
print(view)  # [2 3 4]
view[0] = 99
print(arr)
print(view)
# [ 0  1 99  3  4  5  6  7  8  9]
# [99  3  4]
print(view.base is arr)  # True

arr = np.arange(10)
copy = arr[::2]
copy[0] = 99
print(copy)
print(arr)
# [99  2  4  6  8]
# [99  1  2  3  4  5  6  7  8  9]
print(copy.base in arr)  # True, jest to widok

arr = np.arange(1000)
copy = arr[::2]
copy[0] = 67
print(copy[0])  # 67
print(arr[0])  # 67
print(copy.base is arr)  # True

# reshape() wskazuje kształt
arr = np.arange(1, 13).reshape(3, 4)
print(arr)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]

view_col = arr[:, 1].view()
print(view_col)  # [ 2  6 10]
view_col[:] = 99
print(arr)
# [[ 1 99  3  4]
#  [ 5 99  7  8]
#  [ 9 99 11 12]]

copy_row = arr[0, :].copy()
copy_row[:] = 0
print(arr)
# [[ 1 99  3  4]
#  [ 5 99  7  8]
#  [ 9 99 11 12]]
print(copy_row)
# [0 0 0 0]
print(copy_row.base is arr)  # False, to jest kopia

view_submatrix = arr[:2, :2].view()
view_submatrix *= 10
print(view_submatrix)
# [[ 10 990]
#  [ 50 990]]
print(arr)
# [[ 10 990   3   4]
#  [ 50 990   7   8]
#  [  9  99  11  12]]

lista = [1, 2, 3, 4, 5]
print(lista * 2)  # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
lista_slice = lista[1:3]  # to jest kopia listy pythonowej, dziąla inaczej niż w numpy
print(lista_slice)  # [2, 3]
lista_slice[0] = 99
print(lista)
print(lista_slice)
# [1, 2, 3, 4, 5]
# [99, 3]

arr_1d = np.arange(10)
view_reversed = arr_1d[::-1].view()
view_reversed[0] = 999
print(arr_1d)
print(view_reversed)
# [  0   1   2   3   4   5   6   7   8 999]
# [999   8   7   6   5   4   3   2   1   0]
print(view_reversed.base is arr_1d)  # True

arr_3d = np.arange(27).reshape((3, 3, 3))
print(arr_3d)
copy_3d = arr_3d.copy()
copy_3d[0, 0, 0] = -1
print(copy_3d[0])
print(arr_3d[0])
# [[-1  1  2]
#  [ 3  4  5]
#  [ 6  7  8]]
# [[0 1 2]
#  [3 4 5]
#  [6 7 8]]
print(copy_3d.base is arr_3d)  # False, jest to kopia

arr_float = np.array([1.1, 2.2, 3.3, 4.4], dtype='float32')
print(arr_float.dtype)  # float32
arr_view_as_int = arr_float.astype('int32').view()  # mimo view() stworzyło kopię
print(arr_float)  # [1.1 2.2 3.3 4.4]
print(arr_view_as_int)  # [1 2 3 4]
print(arr_view_as_int.dtype)  # int32
print(arr_float.dtype)  # float32

print(arr_view_as_int.base is arr_float)  # False - kopia
