# Lecture 3 - Pandas
# @ Michael

# pandas library (DataFrame)
# pandas is quilivalent to dataframe format in R
# pandas is built upon the Numpy package, which gives the certain advantage for
# doing scientific programming

# tips: iloc is better for slicing the DataFrame

import numpy as np
import pandas as pd


# create a series
# the series looks neat compared to array
s = pd.Series([12, -4, 7, 9])
s1 = pd.Series([12, -4, 7, 9], index=['a', 'b', 'c', 'd'])
s1.values  # return an array  array([12, -4,  7,  9])
s1.index  # Index(['a', 'b', 'c', 'd'], dtype='object')
s1[2]
s1['c']
s1[s1 > 8]
s1/2
np.log(s1)

serd = pd.Series([1, 0, 2, 1, 2, 3],
                 index=['white', 'white', 'blue', 'green', 'green', 'yellow'])
serd.unique()
serd.isin([0, 3])

s2 = np.log(s1)
s2.isnull()

s2[s2.notnull()]


# DataFrame - copy idea from R (Caution: it's DataFrame, not dataframe)

# create a dataframe
df3 = pd.DataFrame(np.arange(16).reshape([4, 4]),
                   index=['red', 'blue', 'yellow', 'white'],
                   columns=['ball', 'pen', 'pencil', 'paper'])
df3

df3.columns  # column names of pandas
df3.index  # row names
df3.values
df3['pen']
df3pen = df3['pen']
df3pen.values
df3[1:3]  # only index for rows
df3.iloc[0]
df3.iloc[1:3]
df3.iloc[:, 1:3]  # works like R and Matlab but need iloc
df3.head()

df3.columns  # Index(['ball', 'pen', 'pencil', 'paper'], dtype='object')
df3.index  # Index(['red', 'blue', 'yellow', 'white'], dtype='object')

df3['new'] = 12  # create a new column
df3

df3.append([36, 36, 36, 36, 36])

pd.DataFrame([36, 36, 36, 36, 36])  # defaulty, it takes list as pd.Series

s1 = [36, 36, 36, 36, 36]
s1 = np.array(s1)
s1.shape  # (5,)
s1
s1.reshape(1, 5)
pd.DataFrame(s1.reshape(1, 5))

df3.append(pd.DataFrame(s1.reshape(1, 5)))
df3.append(pd.DataFrame(s1.reshape(1, 5)), ignore_index=True)

df3.values

# extract value, stack and convert back into dataframe
df4 = df3.values
df4 = np.vstack([df4, s1.reshape(1, 5)])
pd.DataFrame(df4)
df4 = pd.DataFrame(df4, columns=df3.columns)
df4

ss2 = ['hal', 'hb', 'gag', 'hg', 'g8']
ss2 = np.array(ss2)
ss2.shape
ss2.reshape(1, 5)

df5 = np.vstack([df3.values, ss2.reshape(1, 5)])
pd.DataFrame(df5)
df5 = pd.DataFrame(df5, columns=df3.columns)  # stack works better
type(df5['ball'])  # pandas.core.series.Series
type(df5['ball'].values)  # numpy.ndarray
df5['ball'].values.dtype
np.dtype(df5['ball'])  # object
df5.drop(3)
df5.drop(['new'], axis=1)

df5.apply(min, axis=0)
df5.apply(max, axis=1)

df5.sum()
df5.sum(axis=1)
df5.describe()
df5.sort_index()
df5.sort_index(axis=1)  # sort based on index

type(df5.iloc[2, 4])  # all str '12'
type(df5.iloc[4, 2])  # str 'gag'
df5.iloc[4, 2].isalpha()  # True
df5.iloc[2, 4].isalpha()  # False
df5.iloc[4, 2].isdigit()  # False
df5.iloc[2, 4].isdigit()  # True

df5
# task: filter out row are not digit
df5.to_csv('df5example.csv')

# End of code
