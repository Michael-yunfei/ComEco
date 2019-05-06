# Lecture 7 - Classes and Objected-Oriented Programming (1)
# @ Michael

# This one is the most important lecture until this stage
# Please spend some time to understand it well

# The key to object-oriented programing is thinking about
# objects as `collections' of both data and methods that operate on that data

# Every object has a type that defines the kinds of thingks that
# programs can do with that object

# Programming = data structure + algorithm (abstraction + decomposition)

# in python, data abstractions are done through classes

import datetime

# create a class


class IntSet(object):
    '''An IntSet is a set of integers'''

    def __init__(self):
        '''create an empty set of integers'''
        self.vals = []

    def insert(self, e):
        '''assumes e is an integer and insert e into self'''
        if e not in self.vals:
            self.vals.append(e)

    def member(self, e):
        '''assumes e is an integer
        returns True if e is in self, and False otherwise'''
        return e in self.vals

    def remove(self, e):
        '''assumes e is an integer and removes e from self
        raises ValueError if e is not in self'''
        try:
            self.vals.remove(e)
        except Exception as e:
            raise ValueError(str(e) + ' not found')

    def getMembers(self):
        '''Returns a list containing the elements of self
        Nothing can be assumed about the order of the elements'''
        return self.vals[:]

    def __str__(self):
        '''Returns a string representation of self'''
        self.vals.sort()
        result = ''
        for e in self.vals:
            result = result + str(e) + ','
        return '{' + result[: -1] + '}'  # -1 omits trailing comma


# You can see that a class is just a collection of actions:
# we define
# we name the methods or actions we want to with this class

s = IntSet()
s.insert(3)
print(s.member(3))  # True
print(s.member(5))  # False

s.insert(5)
s.insert(9)
print(s)  # {3,5,9}

# You can see that class is very helpful to organize large programs


# Using classes to keep track of students and faculty


class Person(object):
    '''A calss to keep track of students and faculty'''

    def __init__(self, name):
        '''create a name'''
        self.name = name
        try:
            lastBlank = name.rindex(' ')
            self.lastname = name[lastBlank+1:]
        except Exception:
            self.lastname = name
        self.birthday = None  # finish all initialize setting

    def getname(self):
        '''return full name'''
        return self.name

    def getlastname(self):
        '''return the last name'''
        return self.lastname

    def setbirthday(self, birthday):
        '''assumes birthday is of type datatime data'''
        self.birthday = birthday

    def getage(self):
        '''calcuate the age'''
        if self.birthday is None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days

    def __str__(self):
        '''return self's name'''
        return self.name


me = Person('Michael Wang')
him = Person('Vishnu Kant')
her = Person('Marina')

print(him.getlastname())  # Kant, don't forget ()
him.setbirthday(datetime.date(1993, 12, 30))
him.getage()/365  # 25.353424657534248 years

# End of code
