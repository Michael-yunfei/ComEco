# Function for calculating the minimum distance of codes based on
# Hamming distance
# @ Michael (UCD, ID: 17210880)

# important the main package
import numpy as np
import sys


def HammingDist(c):
    # Warning: this function only works for binary codewords
    # Input: a multiple dimensions of array
    # Output: the minimal distance based on Hamming distance function
    # Algorithm: simple for loop

    n = c.shape[0]  # get the number of codewords
    # len = c.shape[1]  # get the length of codewords
    if n <= 1:
        sys.exit('The number of codewords has to be equal or greater than 2')
    d = np.sum(np.abs(c[0, ]-c[1, ]))
    # initialize the minimial distance as first two codewords
    for i in range(n):
        code1 = c[i, ]  # extract the first code
        countj = i
        while countj < n-1:
            countj += 1
            d_temp = np.sum(np.abs(code1 - c[countj, ]))
            if d_temp < d:
                d = d_temp
    return(d)


a = np.array([[0,0,0,0,0], [1,1,1,0,0], [0,0,1,1,1],
              [1,1,0,1,1]])
a.shape

HammingDist(a)
# = 3

b= np.array([[0,0,0,0,0,0,0], [1,0,1,0,1,0,1], [0,1,1,0,0,1,1],
             [1,1,0,0,1,1,0], [0,0,0,1,1,1,1], [1,0,1,1,0,1,0], [0,1,1,1,1,0,0],
             [1,1,0,1,0,0,1]])
b.shape

HammingDist(b)
# = 4


# function for search tenary code with n = 5, d = 3,

benchmark = np.array([[0, 0, 0, 0, 0], [0, 0, 1, 1, 1], [1, 1, 1, 0, 0],
                     [0, 0, 2, 2, 2], [2, 2, 2, 0, 0], [0, 1, 0, 1, 2],
                     [0, 1, 2, 0, 1], [0, 2, 0, 2, 1], [1, 0, 2, 1, 0],
                     [2, 0, 1, 2, 0], [0, 2, 1, 0, 2]])
benchmark.shape



# initialize a 243 by 5 matrix, as we can have 3**5 = 243
codematrix = np.zeros([243, 5])
# creat a combination matrix
ct = 0
for i in range(3):
    for j in range(3):
        for k in range(3):
            for m in range(3):
                for n in range(3):
                    vct = np.array([i, j, k, m, n])
                    codematrix[ct, ] = vct
                    ct += 1

# Now search all vectors that have minimal distance = 3
codematrix
codematrix.shape  # (243, 5)

# search all codewords in codematrix which have the minimm distance 3

for rows in range(243):
    code = codematrix[rows, ]
    if (np.count_nonzero(code - benchmark[0, ]) >=3 and
            np.count_nonzero(code - benchmark[1, ]) >=3 and
            np.count_nonzero(code - benchmark[2, ]) >=3 and
            np.count_nonzero(code - benchmark[3, ]) >=3 and
            np.count_nonzero(code - benchmark[4, ]) >=3 and
            np.count_nonzero(code - benchmark[5, ]) >=3 and
            np.count_nonzero(code - benchmark[6, ]) >=3 and
            np.count_nonzero(code - benchmark[7, ]) >=3 and
            np.count_nonzero(code - benchmark[8, ]) >=3 and
            np.count_nonzero(code - benchmark[9, ]) >=3 and
            np.count_nonzero(code - benchmark[10, ]) >=3):
        print(code)




codecount = 0
for i in range(codematrix.shape[0]):
        if (np.count_nonzero(codematrix[i, ] - benchmark[0, ]) >= 3 and
        np.count_nonzero(codematrix[i, ] - benchmark[1, ]) >= 3 and
        np.count_nonzero(codematrix[i, ] - benchmark[2, ]) >=3 and
        np.count_nonzero(codematrix[i, ] - benchmark[3, ]) >=3 and
        np.count_nonzero(codematrix[i, ] - benchmark[4, ]) >=3):
            codecount += 1
            benchmark = np.vstack([benchmark, codematrix[i, ]])

codecount  # 58

# now, we expand our benchemark and search inside the benchmark again!

benchmark2 = benchmark[0:6, ]

codecount2 = 0
for i in range(benchmark.shape[0]):
    if (np.count_nonzero(benchmark[i] - benchmark2[0, ]) >=3 and
        np.count_nonzero(benchmark[i] - benchmark2[1, ]) >=3 and
        np.count_nonzero(benchmark[i] - benchmark2[2, ]) >=3 and
        np.count_nonzero(benchmark[i] - benchmark2[3, ]) >=3 and
        np.count_nonzero(benchmark[i] - benchmark2[4, ]) >=3 and
        np.count_nonzero(benchmark[i] - benchmark2[5, ]) >=3):
        codecount2 +=1
        benchmark2 = np.vstack([benchmark2, benchmark[i, ]])

codecount2  # 39


# now, we expand our benchemark2 and search inside the benchmark2

benchmark3 = benchmark2[0:7, ]

codecount3 = 0
for i in range(benchmark2.shape[0]):
    if (np.count_nonzero(benchmark2[i] - benchmark3[0, ]) >=3 and
        np.count_nonzero(benchmark2[i] - benchmark3[1, ]) >=3 and
        np.count_nonzero(benchmark2[i] - benchmark3[2, ]) >=3 and
        np.count_nonzero(benchmark2[i] - benchmark3[3, ]) >=3 and
        np.count_nonzero(benchmark2[i] - benchmark3[4, ]) >=3 and
        np.count_nonzero(benchmark2[i] - benchmark3[5, ]) >=3 and np.count_nonzero(benchmark2[i] - benchmark3[6, ]) >=3):
        codecount3 +=1
        benchmark3 = np.vstack([benchmark3, benchmark2[i, ]])

codecount3  # 32


benchmark4 = benchmark3[0:8, ]

codecount4 = 0
for i in range(benchmark3.shape[0]):
    if (np.count_nonzero(benchmark3[i] - benchmark4[0, ]) >=3 and
        np.count_nonzero(benchmark3[i] - benchmark4[1, ]) >=3 and
        np.count_nonzero(benchmark3[i] - benchmark4[2, ]) >=3 and
        np.count_nonzero(benchmark3[i] - benchmark4[3, ]) >=3 and
        np.count_nonzero(benchmark3[i] - benchmark4[4, ]) >=3 and
        np.count_nonzero(benchmark3[i] - benchmark4[5, ]) >=3 and np.count_nonzero(benchmark3[i] - benchmark4[6, ]) >=3 and np.count_nonzero(benchmark3[i] - benchmark4[7, ]) >=3):
        codecount4 +=1
        benchmark4 = np.vstack([benchmark4, benchmark3[i, ]])

codecount4  # 15

benchmark5 = benchmark4[0:9, ]

codecount5 = 0
for i in range(benchmark4.shape[0]):
    if (np.count_nonzero(benchmark4[i] - benchmark5[0, ]) >=3 and
        np.count_nonzero(benchmark4[i] - benchmark5[1, ]) >=3 and
        np.count_nonzero(benchmark4[i] - benchmark5[2, ]) >=3 and
        np.count_nonzero(benchmark4[i] - benchmark5[3, ]) >=3 and
        np.count_nonzero(benchmark4[i] - benchmark5[4, ]) >=3 and
        np.count_nonzero(benchmark4[i] - benchmark5[5, ]) >=3 and np.count_nonzero(benchmark4[i] - benchmark5[6, ]) >=3 and np.count_nonzero(benchmark4[i] - benchmark5[7, ]) >=3 and np.count_nonzero(benchmark4[i] - benchmark5[8, ]) >=3):
        codecount5 +=1
        benchmark5 = np.vstack([benchmark5, benchmark4[i, ]])

codecount5  # 8


benchmark6 = benchmark5[0:10, ]

codecount6 = 0
for i in range(benchmark5.shape[0]):
    if (np.count_nonzero(benchmark5[i] - benchmark6[0, ]) >=3 and
        np.count_nonzero(benchmark5[i] - benchmark6[1, ]) >=3 and
        np.count_nonzero(benchmark5[i] - benchmark6[2, ]) >=3 and
        np.count_nonzero(benchmark5[i] - benchmark6[3, ]) >=3 and
        np.count_nonzero(benchmark5[i] - benchmark6[4, ]) >=3 and
        np.count_nonzero(benchmark5[i] - benchmark6[5, ]) >=3 and np.count_nonzero(benchmark5[i] - benchmark6[6, ]) >=3 and np.count_nonzero(benchmark5[i] - benchmark6[7, ]) >=3 and np.count_nonzero(benchmark5[i] - benchmark6[8, ]) >=3 and
        np.count_nonzero(benchmark5[i] - benchmark6[9, ]) >=3):
        codecount6 +=1
        benchmark6 = np.vstack([benchmark6, benchmark5[i, ]])

codecount6  # 4

benchmark6.shape


benchmark7 = benchmark6[0:11, ]

codecount7 = 0
for i in range(benchmark6.shape[0]):
    if (np.count_nonzero(benchmark6[i] - benchmark7[0, ]) >=3 and
        np.count_nonzero(benchmark6[i] - benchmark7[1, ]) >=3 and
        np.count_nonzero(benchmark6[i] - benchmark7[2, ]) >=3 and
        np.count_nonzero(benchmark6[i] - benchmark7[3, ]) >=3 and
        np.count_nonzero(benchmark6[i] - benchmark7[4, ]) >=3 and
        np.count_nonzero(benchmark6[i] - benchmark7[5, ]) >=3 and np.count_nonzero(benchmark6[i] - benchmark7[6, ]) >=3 and np.count_nonzero(benchmark6[i] - benchmark7[7, ]) >=3 and np.count_nonzero(benchmark6[i] - benchmark7[8, ]) >=3 and
        np.count_nonzero(benchmark6[i] - benchmark7[9, ]) >=3 and np.count_nonzero(benchmark6[i] - benchmark7[10, ]) >=3):
        codecount7 +=1
        benchmark7 = np.vstack([benchmark7, benchmark6[i, ]])

codecount7  # 0

benchmark7.shape

benchmark7



# Calculate the distance:

q6g1 = np.array([[1, 1, 1, 0, 0], [0, 1, 2, 1, 2]])

q6g2 = np.array([[0, 0, 1, 2, 1,], [1, 2, 2, 2, 0]])

q6kspace = np.zeros([9, 2])

q6count = 0
for i in range(3):
    for j in range(3):
        vtmp = np.array([i, j])
        q6kspace[q6count, ] = vtmp
        q6count += 1


q6kspace


q6kspace @ q6g1

q6kspace @ q6g2
