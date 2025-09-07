import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)
print(newarr)
# [array([1, 2]), array([3, 4]), array([5, 6])]

newarr = np.array_split(arr, 4)
print(newarr)  # [array([1, 2]), array([3, 4]), array([5]), array([6])]
print(newarr[0])  # [1 2]
print(newarr[1])  # [3 4]
print(newarr[2])  # [5]
print(newarr[3])  # [6]

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr, 3)
print(newarr)
# [array([[1, 2],
#        [3, 4]]), array([[5, 6],
#        [7, 8]]), array([[ 9, 10],
#        [11, 12]])]

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18]])
newarr = np.array_split(arr, 3, axis=1)
print(newarr)
# [array([[ 1],
#        [ 3],
#        [ 5],
#        [ 7],
#        [ 9],
#        [11],
#        [13],
#        [15],
#        [17]]), array([[ 2],
#        [ 4],
#        [ 6],
#        [ 8],
#        [10],
#        [12],
#        [14],
#        [16],
#        [18]]), array([], shape=(9, 0), dtype=int64)]

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.hsplit(arr, 3)
print(newarr)
# [array([[ 1],
#        [ 4],
#        [ 7],
#        [10],
#        [13],
#        [16]]), array([[  2],
#        [  5],
#        [  8],
#        [ 11],
#        [141],
#        [ 17]]), array([[ 3],
#        [ 6],
#        [ 9],
#        [12],
#        [15],
#        [18]])]

newarr = np.vsplit(arr, 3)
print(newarr)
# [array([[1, 2, 3],
#        [4, 5, 6]]), array([[ 7,  8,  9],
#        [10, 11, 12]]), array([[ 13, 141,  15],
#        [ 16,  17,  18]])]

#  raise ValueError('dsplit only works on arrays of 3 or more dimensions')
# newarr = np.dsplit(arr, 3)
arr3d = arr.reshape((6, 1, 3))
newarr = np.dsplit(arr3d, 3)
print(newarr)

# [array([[[ 1]],
#
#        [[ 4]],
#
#        [[ 7]],
#
#        [[10]],
#
#        [[13]],
#
#        [[16]]]), array([[[  2]],
#
#        [[  5]],
#
#        [[  8]],
#
#        [[ 11]],
#
#        [[14]],
#
#        [[ 17]]]), array([[[ 3]],
#
#        [[ 6]],
#
#        [[ 9]],
#
#        [[12]],
#
#        [[15]],
#
#        [[18]]])]
