# Companion Python Code for Machine Learning Course
# @ Michael

# Data import and transformation
# https://pandas.pydata.org/pandas-docs/stable/getting_started/comparison/comparison_with_r.html

import numpy as np
import pandas as pd

frame1 = pd.DataFrame({'id': ['ball', 'pencil', 'pen', 'mug', 'ash'],
                       'price': [12.33, 11.44, 33.21, 13.28, 38.9]})
frame1

frame2 = pd.DataFrame({'id': ['pencil', 'pencil', 'ball', 'pen'],
                       'color': ['white', 'red', 'red', 'black']})
frame2

pd.merge(frame1, frame2, on='id')  # check cheatsheet for tips

array1 = np.arange(9).reshape([3, 3])
array2 = np.arange(9).reshape([3, 3]) + 6
np.hstack([array1, array2])
np.concatenate([array1, array2], axis=1)  # same with stack

frame3 = pd.DataFrame(np.random.rand(9).reshape([3, 3]), index=[1, 2, 3],
                      columns=['A', 'B', 'C'])
frame3

frame4 = pd.DataFrame(np.random.rand(9).reshape([3, 3]), index=[4, 5, 6],
                      columns=['A', 'B', 'C'])
frame4

pd.concat([frame3, frame4])
pd.concat([frame3, frame4], axis=1)


# reshaping Data

longframe = pd.DataFrame({'color': ['white', 'white', 'white', 'red', 'red',
                                    'red', 'black', 'black', 'black'],
                          'item': ['ball', 'pen', 'mug',
                                   'ball', 'pen', 'mug',
                                   'ball', 'pen', 'mug'],
                          'value': np.random.rand(9)})
longframe
longframe.pivot('color', 'item')
longframe.pivot_table(index='color', columns='item',
                      values='value').reset_index()
# make sure you understand the difference
# clearly, R is much better than python for spreading dataframe

# mapping in DataFrame - quite powerful if you know how to use it well

frame5 = pd.DataFrame({'item': ['ball', 'mug', 'pen', 'pencil', 'ash'],
                       'color': ['white', 'red', 'green', 'black', 'yellow']})
prices = {'ball': 5.65, 'mug': 4.20, 'bottle': 1.49, 'pen': 1.39, 'ash': 39,
          'pencil': 0.59}
frame5['item'].map(prices)
frame5['price'] = frame5['item'].map(prices)
frame5

# group by

frame6 = pd.DataFrame({'color': ['white', 'red', 'green', 'red', 'green'],
                       'price1': [5.59, 4.20, 1.39, 4.38, 2.87],
                       'price2': [4.78, 1.89, 2.54, 3.33, 3.21]})
frame6.groupby('color').sum()
frame6.groupby('color').sum().add_prefix('total_')
frame6.groupby('color').sum().add_prefix('total_').reset_index()

# End of Code
