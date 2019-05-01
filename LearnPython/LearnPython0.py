# Lecture 0 - Introduction to Python
# Konstanz, 12/03/2019
# @ Michael(Fei) Wang

# Simple Numerical Programs to review Python

# For Loop

x = 4
for i in range(0, x):   # range function
    print(i)

# Show the scope of for loop

x = 4
for i in range(0, x):
    print(i)
    x = 5

x = 4
for j in range(x):
    for i in range(x):  # the function in the inner loop is evaluated each time
        print(i)
        x = 2

x = int(input('Enter an integer: '))
for ans in range(0, abs(x)+1):
    if ans**3 >= abs(x):
        break
if ans**3 != abs(x):
    print(x, 'is not a perfect cube')
else:
    if x < 0:
        ans = -ans
    print('Cube root of', x, 'is', ans)

# be careful on float

x = 0.0  # it is a float number
for i in range(10):
    x = x + 0.1
if x == 1.0:
    print(x, '= 1.0')
else:
    print(x, 'is not 1.0')


# End of code
