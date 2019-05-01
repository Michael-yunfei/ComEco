# Lecture 5I - seaborn
# @ Michael

# Tips: ax or axes is for individual plot
# Tips: fig is for final plot
# Tips: always start by: fig, axes = plt.subplots()
# or call seaborn plots directyly but assign it with figure name

# Seaborn is a Python data visualization library based on matplotlib.
# It provides a high-level interface for drawing attractive and
# informative statistical graphics.


import pandas as pd
import matplotlib.pyplot as plt
import os  # the function for chaning working directory path
import seaborn as sns


# set working directory
os.getcwd()
os.chdir('/Users/Michael/Documents/ComEco/LearnPython')

# load dataset
mpg = pd.read_csv('mpg.csv')
mpg.head()
mpg.columns

# Seaborn tutorial

# Countbar plot

fig, ax = plt.subplots(figsize=(12, 6))
sns.countplot(mpg['manufacturer'], ax=ax)  # much easier and more beautiful
ax.set(title='Frequency of manufacturer',
       xlabel='Manufacturer',
       ylabel='Count')
fig.savefig('snscountplot.png', dpi=600, bbox_inches='tight')

# Except for the font of titles, the plot is quite elegant

# scatterplot

sns.set(style="darkgrid")  # or you can use plt.style.use('seaborn-talk')
fig, ax = plt.subplots(figsize=(6, 3.9))
sns.scatterplot(x=mpg['displ'], y=mpg['hwy'], ax=ax)

# two scatter plots, one with hue, one without hue
fig, axes = plt.subplots(1, 2, figsize=(9, 5.6), sharey=True)  # share y
sns.scatterplot(x=mpg['displ'], y=mpg['hwy'], ax=axes[0])
sns.scatterplot(x=mpg['displ'], y=mpg['hwy'], hue=mpg['class'], ax=axes[1])
fig.suptitle('Displacement vs highway efficiency')  # set title for all

# or we can set title sperately
fig, axes = plt.subplots(1, 2, figsize=(12, 5.6), sharey=True)  # share y
sns.scatterplot(x=mpg['displ'], y=mpg['hwy'], ax=axes[0])
axes[0].set(title='without hue', xlabel='Displacement',
            ylabel='Highway Efficiency')
sns.scatterplot(x=mpg['displ'], y=mpg['hwy'], hue=mpg['class'],
                alpha=0.8, ax=axes[1])
axes[1].set(title='with hue', xlabel='Displacement')
fig.suptitle('Displacement vs highway efficiency')  # set title for all
fig.savefig('snsscatter.png', dpi=600, bbox_inches='tight')

# call facet

g = sns.FacetGrid(mpg, col='class', col_wrap=4)
g.map(sns.scatterplot, 'displ', 'hwy')

# visit https://seaborn.pydata.org/tutorial/axis_grids.html
# for more explanations

sns.relplot(x='displ', y='hwy', data=mpg)  # very straightforward
sns.relplot(x='displ', y='hwy', hue='class', data=mpg)
grel = sns.relplot(x='displ', y='hwy', hue='class', data=mpg)
grel.set(title='Displacement vs highway efficiency')

# Advantage: easy to hand
# disadvntage: could not set the figsize
# tips: always start by: fig, axes = plt.subplots() or plt.subplots()
# never use relplot alone

# line plot
fig, ax = plt.subplots(figsize=(6, 3.8))
sns.lineplot(x='displ', y='hwy', data=mpg,
             hue='drv', alpha=0.9, ax=ax)

# regression line plot
fig, ax = plt.subplots(figsize=(6, 3.8))
sns.regplot(x='displ', y='hwy', data=mpg, ax=ax)


glm = sns.lmplot(x='displ', y='hwy', hue='drv', data=mpg)
glm.set(title='regression fit plots')
glm.fig.set_size_inches(6.5, 3.5)

# SUMMAR for Seaborn
# use: fig, axes = plt.subplots() is to call matplotlib
# use: seaborn plot and assign them into figure game, like
# glm = sns.lmplot(x='displ', y='hwy', hue='drv', data=mpg)
# then set it with title and figure attributes
# for multiple plots, try to call sns.FacetGrid rather than subplots
# When it comes to math plaot, use matplotlib; all others use seaborn

# Enc of code
