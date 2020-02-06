# Gradient Descent
# @ Michael

# pease read this: https://en.wikipedia.org/wiki/Gradient_descent#Python

import numpy as np
import matplotlib.pyplot as plt

# Generally, we want to find the minimum values for a function
# take this as an example:
# f(x) = x^4 - 3x^3 + 2


def polyfun(x):
    y = x**4 - 3 * x**3 + 2
    return(y)


x1 = np.linspace(-6, 6, 100)
y1 = polyfun(x1)
plt.plot(x1, y1)


# zoom in the picture
x2 = np.linspace(0, 3, 100)
y2 = polyfun(x2)
plt.plot(x2, y2)


# find the minium numerically

update_x = 8  # start it from value 8 (chosen by plotting the function)
alpha = 0.001  # learning rate
tolerate_rule = 0.00001  # set the torelate rule
max_iters = 10000  # set the Maximum iteration


# set the derivatie function
def polyfunder(x):
    yprime = 4 * x**3 - 9 * x**2
    return (yprime)


i = 0
while tolerate_rule >= 0.00001 and i <= max_iters:
    i += 1
    start_value = update_x
    update_x = start_value - alpha * polyfunder(start_value)
    tolerate_rule = abs(update_x - start_value)

print("Minimum value is at", update_x, "and minimum is", polyfun(update_x))
# i = 360, which means it converges quite fast


# find the minimum numerically, second example

next_x = 6  # We start the search at x=6
gamma = 0.01  # Step size multiplier
precision = 0.00001  # Desired precision of result
max_iters = 10000  # Maximum number of iterations


# Derivative function
def lm(x):
    y = 4 * x**3 - 9 * x**2
    return(y)


for i in range(max_iters):
    current_x = next_x
    next_x = current_x - gamma * lm(current_x)
    step = next_x - current_x
    if abs(step) <= precision:
        break

print("Minimum at", next_x)  # Minimum at 2.2499646074278457
