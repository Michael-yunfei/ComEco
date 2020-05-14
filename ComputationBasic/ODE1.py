# General slope fields for first order differential equations
# @ Michael (UCD)
# good webiste: https://homepages.bluffton.edu/~nesterd/java/slopefields.html

# Import main packages
import numpy as np
import matplotlib.pyplot as plt
import sys
import os


# define the differential equation diff1: y' = x/y
def diff1(x, y):
    return x/y


# set the x and y domain
x = np.linspace(-3, 3, 50)
y = np.linspace(-4, 4, 50)

# now we plot function
for j in x:
    for k in y:
        slope = diff1(j,k)
        domain = np.linspace(j-0.07, j+0.07, 2)
        def fun1(x1, y1):
            z = slope*(domain-x1)+y1
            return z
        plt.plot(domain,fun1(j,k))

plt.title("Slope field y'")
plt.grid(True)
plt.show()


# Matlab method

# set the x and y domain
x = np.linspace(-3, 3, 100)
y = np.linspace(-4, 4, 100)
X, Y = np.meshgrid(x, y)  # do the meshgrid
dy = X/Y
dx = np.ones(dy.shape)

color = dy
lw = 1
plt.streamplot(X,Y,dx, dy, color=color, density=1., cmap='jet', arrowsize=1)



# Use source code written by Professor Ringland
os.getcwd()
os.chdir('/Users/Michael/Documents/ComEco/ComputationBasic')
from resources306 import *


def f(x, y):
    return x/y


slopefieldplot(f, -3, 3, -2, 2, 0.2, lw=1)
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('slopefield.png', dpi=300)


x = sp.symbols('x')
y1 = x**2-2*x+2
y2 = ((x**2-2*x+2)*sp.exp(x)-3)*sp.exp(-x)
y1,y2

slopefieldplot( f, -2,2, -1,2, .2 ,lw=2)
expressionplot(y1,x,-2,2,color='r',alpha=.4,lw=3)
expressionplot(y2,x,-1,2,color='b',alpha=.4,lw=3)
plt.xlabel('x')
plt.ylabel('y')

y3**2 = x**2 + 2
expressionplot(y3, x, -4, 4, color='m', alpha=0.5, lw=2)


## Autonomouse equations
