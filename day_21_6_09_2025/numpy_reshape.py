import numpy as np

arr = np.arange(1, 13)
print(arr)
print(arr.dtype)
print(arr.shape)
# [ 1  2  3  4  5  6  7  8  9 10 11 12]
# int64
# (12,) 1D

newarr = arr.reshape(4, 3)
print(newarr)
print(newarr.shape)
# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]]
# (4, 3) 2D

newarr = arr.reshape(2, 3, 2)
print(newarr)
print(newarr.shape)
# [[[ 1  2]
#   [ 3  4]
#   [ 5  6]]
#
#  [[ 7  8]
#   [ 9 10]
#   [11 12]]]
# (2, 3, 2)

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# newarr = arr.reshape(3, 3)
# Traceback (most recent call last):
#   File "/Users/radoslawjaniak/PycharmProjects/Bootcamp-10-05-2025/day_21_6_09_2025/numpy_reshape.py", line 33, in <module>
#     newarr = arr.reshape(3, 3)
# ValueError: cannot reshape array of size 8 into shape (3,3)

newarr = arr.reshape(2, 2, -1)
print(newarr)
print(newarr.shape)
# [[[ 1  2  3]
#   [ 4  5  6]]
#
#  [[ 7  8  9]
#   [10 11 12]]]
# (2, 2, 3) dostosowanie trzeciego wymiaru automatycznie (-1)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 2, -1)
print(newarr)
print(newarr.shape)
# [[[1 2]
#   [3 4]]
#
#  [[5 6]
#   [7 8]]]
# (2, 2, 2)

arr = np.arange(12)
print(arr)
newarr = arr.reshape(-1, 2)
print(newarr)
print(newarr.shape)
# [[ 0  1]
#  [ 2  3]
#  [ 4  5]
#  [ 6  7]
#  [ 8  9]
#  [10 11]]
# (6, 2)

newarr = arr.reshape(3, -1)
print(newarr)
print(newarr.shape)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]
# (3, 4)

newarr_order_f = arr.reshape((3, 4), order="F")  # w stylu fortrana, kolumnowo
print(newarr_order_f)
# [[ 0  3  6  9]
#  [ 1  4  7 10]
#  [ 2  5  8 11]]

newarr_order_c = arr.reshape((3, 4), order="C")  # C jest domyslnie, wierszowo
print(newarr_order_c)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]
print(newarr.flags)
#   C_CONTIGUOUS : True
#   F_CONTIGUOUS : False
