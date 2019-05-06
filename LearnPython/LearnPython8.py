# Lecture 8 - Classes and Objected-Oriented Programming (2)
# @ Michael

import numpy as np
import matplotlib.pyplot as plt

# learn printing format

x = 'michael'
ia = 42
ifl = 5.986
got = 'John Snow'

print('{}'.format(x))  # michael
print('{:d}'.format(ia))  # 42
print('{} {}'.format('michael', 'Hwang'))  # michael Hwang
print('{:f}'.format(ifl))  # 5.986000
print('{:.2f}'.format(ifl))  # 5.99
print('{} {} {:.2f}'.format(x, got, ifl))  # michael John Snow 5.99


# Bank accounts

class Account:
    def __init__(self, name, account_number, initial_amount):
        self.name = name
        self.no = account_number
        self.balance = initial_amount

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def dump(self):
        print('{} {} {} {:d}'.format(self.name, self.no, 'balance:',
                                     self.balance))


a1 = Account('John Snow', '19371551951', 20000)
a2 = Account('Michael Hwang', '19371564761', 20000)
a1.deposit(100)
a2.deposit(5600)
a2.withdraw(300)
a1.withdraw(80)
a1.balance  # 20020
a2.balance  # 25300
a1.dump()  # John Snow 19371551951 balance: 20020
a2.dump()  # Michael Hwang 19371564761 balance: 25300

#  most people take calss as a manufacture for doing the abstract stuff
# exericse: modify the above class by adding an attribute get_balance()


# polynominal function in python, p(x)=x4−4⋅x2+3⋅x
def p(x):
    return x**4 - 4*x**2 + 3*x


xdm = np.linspace(-3, 3, 500, endpoint=True)
yrn = p(xdm)
fig, ax = plt.subplots(1, 1, figsize=(6.9, 4.7))
ax.plot(xdm, yrn)
fig.show()


class Polynominal:
    '''A class for polynominal funcitons'''

    def __init__(self, coefficients):  # you can add * in front of coefficients
        '''input: coefficients like a_n, a_{n-1}, ...n_1'''
        self.coefficients = coefficients[::-1]  # reverse the order

    def __repr__(self):
        ''' default function to print out results'''
        return "Polynominal" + str(self.coefficients[::-1])


# we can represent the function like:
p2 = Polynominal([4, 0, -4, 3, 0])
print(p2)
p3 = Polynominal(4, 0, -4, 3, 0)  # why error ?


class Polynominal:
    '''A class for polynominal funcitons'''

    def __init__(self, *coefficients):  # you can add *
        '''input: coefficients like a_n, a_{n-1}, ...n_1'''
        self.coefficients = coefficients[::-1]  # reverse the order

    def __repr__(self):
        ''' default function to print out results'''
        return "Polynominal" + str(self.coefficients[::-1])

    def __call__(self, x):
        res = 0
        for index, coeff in enumerate(self.coefficients):
            res += coeff * x**index
        return res


p4 = Polynominal(4, 0, -4, 3, 0)

for x in range(-3, 3):
    print(x, p4(x))

xdom4 = np.linspace(-3, 3, 500, endpoint=True)
yrng4 = p4(xdom4)
plt.plot(xdom4, yrng4)


# now we add more attributes
# first we define a function to zip for two parameters
def zip_longest(iter1, iter2, fillchar=None):
    for i in range(max(len(iter1), len(iter2))):
        if i >= len(iter1):
            yield (fillchar, iter2[i])
        elif i >= len(iter2):
            yield (iter1[i], fillchar)
        else:
            yield (iter1[i], iter2[i])
        i += 1


p5 = (-2,)
p6 = (4, -1, 9)
for x in zip_longest(p5, p6, fillchar=0):
    print(x)


class Polynomial:

    def __init__(self, *coefficients):
        """ input: coefficients are in the form a_n, ...a_1, a_0
        """
        # for reasons of efficiency we save the coefficients in reverse order,
        # i.e. a_0, a_1, ... a_n
        self.coefficients = coefficients[::-1]  # tuple is turned into list

    def __repr__(self):
        """
        method to return the canonical string representation
        of a polynomial.
        """
        # The internal representation is in reverse order,
        # so we have to reverse the list
        return "Polynomial" + str(self.coefficients[::-1])

    def __call__(self, x):
        res = 0
        for index, coeff in enumerate(self.coefficients):
            res += coeff * x**index
        return res

    def degree(self):
        return len(self.coefficients)

    @staticmethod
    def zip_longest(iter1, iter2, fillchar=None):
        for i in range(max(len(iter1), len(iter2))):
            if i >= len(iter1):
                yield (fillchar, iter2[i])
            elif i >= len(iter2):
                yield (iter1[i], fillchar)
            else:
                yield (iter1[i], iter2[i])
            i += 1

    def __add__(self, other):
        c1 = self.coefficients
        c2 = other.coefficients
        res = [sum(t) for t in Polynomial.zip_longest(c1, c2)]
        return Polynomial(*res)

    def __sub__(self, other):
        c1 = self.coefficients
        c2 = other.coefficients

        res = [t1-t2 for t1, t2 in Polynomial.zip_longest(c1, c2)]
        return Polynomial(*res)


p7 = Polynomial(4, 0, -4, 3, 0)
p8 = Polynomial(-0.8, 2.3, 0.9, 1, 0.8)
psum = p7 + p8
pdiff = p7 - p8
xdom9 = np.linspace(-3, 3, 500, endpoint=True)
f7 = p7(xdom9)
f8 = p8(xdom9)
fsum = psum(xdom9)
fdiff = pdiff(xdom9)
fig, ax = plt.subplots(1, 1, figsize=(8.9, 5.6), sharex=True)
ax.plot(xdom9, f7, label='F7')
ax.plot(xdom9, f8, label='F8')
ax.plot(xdom9, fsum, label='F-sum')
ax.plot(xdom9, fdiff, label='F-diff')
ax.legend()
ax.set_title('Plot of Polynomial functions')

# visit https://www.python-course.eu/polynomial_class_in_python.php
# for more examples
# End of code
