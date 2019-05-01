# Companion Python Code for Machine Learning Course
# @ Michael

# numpy library
# numpy library is built up on the list or you can see that it is constructed
# based on the list
# tips: one dimension, no need use [], for instance np.arange(1, 10)
# tips: two dimension, need use [], for instance, np.zeros([3, 3])
# tips: or use reshape to creat matrix np.arange(1, 10).reshape(3, 3)

import numpy as np


a = np.array([1, 2, 3])
a
type(a)
a.dtype
a.ndim
a.shape

b = np.array([1, 2, 3], [5.6, 7.8, 9.9])  # this is wrong
b = np.array([[1, 2, 3], [5.6, 7.8, 9.9]])
b.dtype
b.ndim
b.shape  # always use shape to check the dimension

# the input for array has to be a list []

g = np.array([['a', 'b', 'c'], [1, 6, 9]])
g.dtype  # dtype('<U1')
g.shape  # (2, 3)

# numpy is designed for numerical calcuation, is analogous to Matlab

# intrinsic creation of an array
np.zeros((3, 3))
np.zeros([3, 3])  # I recommand this one rather np.array((3, 3))
np.ones([6, 6])

# all built-in fuctions like arange, linspace are not taking list as input

np.arange(1, 8)  # array([1, 2, 3, 4, 5, 6, 7])
np.arange(1, 13, 2)  # array([ 1,  3,  5,  7,  9, 11])
np.arange(1, 13, 2).reshape(2, 3)  # array([[ 1,  3,  5],[ 7,  9, 11]])
np.linspace(0, 10, 100)  # last argument is how many numbers do you need
np.random.random(6)

a = np.arange(6)
a
np.sqrt(a)  # call sqrt from np.sqrt()
np.sin(a)

A = np.arange(0, 9).reshape(3, 3)  # by row
B = np.ones([3, 3])
A * B
np.dot(A, B)

A = np.arange(1, 10).reshape(3, 3)
B = 3*np.ones([3, 3])
A * B
np.dot(A, B)
B[1, 2] = 5
B
np.dot(A, B)

np.arange(0, 9).sum()  # 36
np.arange(0, 9).max()  # 8
np.arange(0, 9).min()  # 0
np.arange(0, 9).mean()  # 4.0
np.arange(0, 9).std()   # 2.581988897471611

a = np.arange(10, 16)
a[1:5:2]

# It does not matter you do row or column, always gives row
A = np.arange(0, 9).reshape(3, 3)
for row in A:
    print(row)

for column in A:
    print(column)

# apply_along_axis is analogous to apply, lapply, sapply in R

np.apply_along_axis(print, axis=0, arr=A)  # column = 0
np.apply_along_axis(print, axis=1, arr=A)  # row  = 1
np.apply_along_axis(np.sum, axis=0, arr=A)  # array([ 9, 12, 15])
np.apply_along_axis(np.sum, axis=1, arr=A)  # array([ 3, 12, 21])

A = np.random.random([3, 3])  # any built-in function need list as input
A > 0.5
A[A > 0.5] = 0.3  # conditional change all values at once
A.ravel()
A.transpose()

A = np.zeros([3, 3])
B = np.ones([3, 3])
[A, B]
np.vstack([A, B])  # I have to say matlap is more intuitivly
np.vstack([B, A])
np.hstack([A, B])

a = np.linspace(1, 9, 6)
b = np.linspace(2, 8, 6)
c = np.linspace(3, 10, 6)
np.column_stack([a, b, c])
np.row_stack([a, b, c])

d = np.row_stack([a, b, c])
np.split(d, [2], axis=0)
np.split(d, [2], axis=1)
np.split(d, [2, 3], axis=1)

# Warning: numpy array is mutalbe

a = np.arange(0, 10)
b = a
a[3] = 156
b

a = np.arange(0, 10)
b = a.copy()
a[3] = 156
b
a

# it should be enought for people who have some backgroup
# End of code
