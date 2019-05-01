# Lecture 5I - Matplotlib
# @ Michael

# By the name, we can see that Matplotlib is the extension of Matlab in Python
# It is very helpful if you are fimilary with matlab
# For future, you can compare data visualizaiton here with R (ggplot2) and
# Javascript (D3.js)

# Tips: all data visualization follows the way of buildong up layers
# we have three layers: scripting, artist, and backend in Matplotlib.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import os  # the function for chaning working directory path

plt.plot([1, 2, 3, 4])  # you can call plt.show() to show the plot
plt.axis([0, 5, 0, 20])  # change the range of axis
plt.title('My first plot')

# plot sin and cons functions

t1 = np.arange(0, 2.5, 0.1)
y1 = np.sin(math.pi * t1)
y2 = np.sin(math.pi * t1 + math.pi / 2)
y3 = np.cos(math.pi * t1 - math.pi)
plt.plot(t1, y1, y2, y3)  # compare the difference with the following one
plt.plot(t1, y1, t1, y2, t1, y3)
plt.plot(t1, y1, 'bo', t1, y2, 'r--', t1, y3, 'g-.')
# visit https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html for
# more parameters

# add legend
# at this stage, you might realize it's not that straightforward to add legends
# we need do this

plt.plot(t1, y1, 'bo', label='sin function 1')
plt.plot(t1, y2, 'r--', label='sin function 2')
plt.plot(t1, y3, 'g-.', label='cos function')
plt.legend()
plt.show()

plt.plot(t1, y1, 'bo', label='sin function 1')
plt.plot(t1, y2, 'r--', label='sin function 2')
plt.plot(t1, y3, 'g-.', label='cos function')
plt.legend(loc='lower center')  # change the position
plt.title('Comparision of sin and cos function')
plt.axis([-1, 3, -1.5, 1.5])
plt.show()

plt.plot(t1, y1, 'bo', label='sin function 1')
plt.plot(t1, y2, 'r--', label='sin function 2')
plt.plot(t1, y3, 'g-.', label='cos function')
plt.axis([-1, 3, -1.5, 1.5])
plt.legend(loc='upper left')  # change the position
plt.title('Comparision of sin and cos function')
plt.show()

# the tricky to add legend

plt.plot(t1, y1, 'bo', label='sin function 1')
plt.plot(t1, y2, 'r--', label='sin function 2')
plt.plot(t1, y3, 'g-.', label='cos function')
plt.axis([-0.5, 4.5, -1.5, 1.5])
plt.legend(loc='center right')  # change the position
plt.title('Comparision of sin and cos function')
plt.show()

# write math equations, put r before math and $$

plt.plot(t1, y1, 'bo', label=r'$\sin(\pi t)$')
plt.plot(t1, y2, 'r--', label=r'$\sin(\pi t + \frac{\pi}{2})$')
plt.plot(t1, y3, 'g-.', label=r'$\cos(\pi t - \pi)$')
plt.axis([-0.5, 4.5, -1.5, 1.5])
plt.legend(loc='center right')  # change the position
plt.title('Comparision of sin and cos function')
plt.show()

# make the plot become more beautiful and core more readable
# use heck string, such as #F6776F

plt.plot(t1, y1, color='#F6776F', linewidth=2, label=r'$\sin(\pi t)$')
plt.plot(t1, y2, color='#4688F1', linewidth=2,
         label=r'$\sin(\pi t + \frac{\pi}{2})$')
plt.plot(t1, y3, color='#4F9E94', linestyle='-.',
         linewidth=2, label=r'$\cos(\pi t - \pi)$')
plt.axis([-0.5, 4.5, -1.5, 1.5])
plt.legend(loc='center right')  # change the position
plt.title('Comparision of sin and cos functions')
plt.show()

# change font of title and add x-asix lablels

plt.plot(t1, y1, color='#F6776F', linewidth=2, label=r'$\sin(\pi t)$')
plt.plot(t1, y2, color='#4688F1', linewidth=2,
         label=r'$\sin(\pi t + \frac{\pi}{2})$')
plt.plot(t1, y3, color='#4F9E94', linestyle='--',
         linewidth=2, label=r'$\cos(\pi t - \pi)$')
plt.axis([-0.5, 4.5, -1.5, 1.5])
plt.legend(loc='center right')  # change the position
plt.title('Comparision of sin and cos functions', fontsize=16)
plt.xlabel('time t')
plt.ylabel('y')
plt.grid()  # add grid
plt.show()


# is this the effective way to do plot? No, why? see following examples
# load mpg csv data
# visit https://rpubs.com/shailesh/mpg-exploration for description of dataset
print(os.getcwd())
os.chdir('/Users/Michael/Documents/ComEco/LearnPython')
mpg = pd.read_csv('mpg.csv')  # load csv
type(mpg)  # pandas.core.frame.DataFrame
mpg.head()
mpg.describe()
mpg.columns
# Index(['manufacturer', 'model', 'displ', 'year', 'cyl', 'trans', 'drv',
#        'cty', 'hwy', 'fl', 'class'], dtype='object')


# check the distribution of manufacture
# always use bar for 'string' or discrete values
mpg['manufacturer'].value_counts().plot('bar')

# you see that it is not straightforward

# Effectively using matplotlib
# Using matplotlib needs a little bit deep understanding on it's structure
# read this: https://pbpython.com/effective-matplotlib.html
#  I highly recommend getting in the habit of doing this:

plt.style.available  # check the available theme
plt.style.use('ggplot')
fig, ax = plt.subplots()  # creat a canvas, fig is final image, ax is plot
mpg['manufacturer'].value_counts().plot(kind='bar', ax=ax)
ax.set(title='Frequency of manufacturer', xlabel='manufacturer',
       ylabel='Count')
fig.savefig('manubar.png', dpi=360, bbox_inches='tight')

# plot Displacement vs highway efficiency
fig, ax = plt.subplots()
ax.scatter(mpg['displ'], mpg['hwy'])

# I hope now you shoule realize that matplotlib is very old fashion
# code is barely readable
# that's why we will stick to seaborn and plotnine for next lecture

# End of code
