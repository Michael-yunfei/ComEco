# Lecture 1 - Data structure
# @ Michael

# mutable and immutable object (very important!)
# list, set, dict are mutable objects
# all others are immutable objects

for i in range(6):
    print(i)

L = ['I did it all', 4, 'love']
for i in range(len(L)):
    print(L[i])

L[0:2]  # see the difference index
L[1:2]
L[1:3]

Techs = ['MIT', 'Caltech']
Ivys = ['Harvard', 'Yale', 'Brown']
Univs = [Techs, Ivys]
Univs1 = [['MIT', 'Caltech'], ['Harvard', 'Yale', 'Brown']]
Univs == Univs1
print('Ids of Univs[0] and Univs[1]', id(Univs[0]), id(Univs[1]))
print('Ids of Univs1[0] and Univs1[1]', id(Univs1[0]), id(Univs1[1]))
Techs.append('RPI')
print(Univs)
print(Univs1)

for e in Univs:
    print("Univs contains", e)
    print(' which contains')
    for u in e:
        print(' ', u)


def updatelist(list1):
    list1 += [10]


n = [5, 6]
print(id(n))
updatelist(n)
print(n)  # list has been updated
print(id(n))  # but not id


def updateint(int1):
    int1 += 10


b = 5
print(id(b))
updateint(b)  # b is not updated, only go through the function
print(b)  # int is not mutable


def updatetuple(tuple1):
    tuple1 += ('haha')


t1 = (1, 'two', 3)
t2 = (3.25, 'pi')
t1+t2
print(id(t1))  # 4420485768
updatetuple(t1)  # this functions gives error
print((t1, 3.25, 'pi'))
print((t1, t2))
print((t1+t2))

# Tuple is immutable, we cannot append it

# The following examples shows the tricky part of list


def removeDups(L1, L2):
    for e1 in L1:
        if e1 in L2:
            L1.remove(e1)


L1 = [1, 2, 3, 4]
L2 = [1, 2, 5, 6]
removeDups(L1, L2)
print(L1)  # [2, 3, 4], however it should be[3, 4] why?


def removeDups2(L1, L2):
    L1clone = L1[0:len(L1)]  # try newL1 = L1
    for e1 in L1clone:  # try for e1 in newL1:
        if e1 in L2:
            L1.remove(e1)


L1 = [1, 2, 3, 4]
L2 = [1, 2, 5, 6]
removeDups2(L1, L2)
print(L1)  # [3, 4], why?

# List comprehension - quite handy

L = [x**2 for x in range(1, 7)]
print(L)  # [1, 4, 9, 16, 25, 36]

mixed = [1, 2, 'a', 3, 4, 5.6]
print([x**2 for x in mixed if type(x) == int])  # [1, 4, 9, 16]

# enumerate

my_list = ['apple', 'banana', 'grapes', 'pear']
for c, value in enumerate(my_list, 1):
    print(c, value)


# Functions as ojbects


def applyToEach(L, f):
    """Assumes L is a list, f a function
       Mutate L by replacing each element, e, of L by f(e)"""

    for i in range(len(L)):
        L[i] = f(L[i])


L = [1, -2, 3.3]
print("L = ", L)
applyToEach(L, abs)
print('L =', L)

# Strings

st = 'My Name is Michael, I am from sch68cls2; my friend Vishnu is \
      from sch7cls16'
st[0]  # 'M'
st.count('a')  # count how many times the string 'a' occur
st.count('sch')
st.find('sch')
st[30:33]
st.find('cls')
st[33:35]
st.index('sch')  # only gives the first one

# now we want to find all indexes

sch_str = 's'
sch_indx = [[i, a] for i, a in enumerate(st) if a == sch_str]
print(sch_indx)

# task: split sch 68 and class 12
stlist = st.split(" ")
schcls = [i for i in stlist if i[0:3] == 'sch']
sch_cls_list = []
for i in schcls:
    schindx = i.find('sch')
    clsindx = i.find('cls')
    sch_cls_list.append(i[schindx:schindx+3])
    sch_cls_list.append(i[schindx+3:clsindx])
    sch_cls_list.append(i[clsindx:clsindx+3])
    sch_cls_list.append(i[clsindx+3:len(i)])
print(sch_cls_list)  # not bad, need clean ';'


# Dictonaries

monthNumbers = {'Jan': 1, 'Feb': 2, 'Mar': 3}
monthNumbers['Feb']


# End of code
