# Lecture 6 - Exceptions and Assertions
# @ Michael

# An 'exception' is usually defined as 'something that does not conform to the
# norm'
# Virtually every module in the Python library uses them

# First example


val = input('Enter an integer: ')
try:
    val = int(val)
    print('The square of the number you entered is', val**2)
except ValueError:
    print(val, 'is not an integer')


# Second Example


def getRatios(vect1, vect2):
    '''Assumes: vect1 and vect2 are equal length lists of numbers
    returns: a lit cotining the meaningful values of
    vect1[i]/vect2[i]'''
    ratios = []  # empty list for storving values
    for index in range(len(vect1)):
        try:
            ratios.append(vect1[index]/vect2[index])
        except ZeroDivisionError:
            ratios.append(float('nan'))
        else:
            raise ValueError('getRatios called with bad arguments')
    return ratios


help(getRatios)  # hope you can understand why we use '''

v1 = [1, 2, 3, 6]
v2 = [2, 4, 9, 12]
getRatios(v1, v2)
v3 = [2, 4, 0, 12]
getRatios(v1, v3)  # [0.5, 0.5, nan, 0.5]
v4 = ['a', 4, 9, 19]
getRatios(v1, v4)  # return errors

# Take away: try, except mechanims is efficient control flow

x = 10
if x > 5:
    raise Exception('x should not exceed 5. The value of x was: {}'.format(x))

# visit https://realpython.com/python-exceptions/ for more information

# End of code
