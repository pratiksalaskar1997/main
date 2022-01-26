#List Comprehension to Iterate through a String

str1 = 'pratiksalaskar'
print([i.split() for i in str1])

print([i for i in range(0, 101) if i % 2 == 0])
print([i**2 for i in range(0, 101)])
print([i for i in range(0, 101) if (i % 2)/i ==


print([x for x in range(2, 20) if all(x % y != 0 for y in range(2, x))])

print([x for x in range(0, 101) if x % 2 == 0 and x % 5 == 0])

a=[[1,2,5],
   [3,4,6]]
t=[]
for i in range(len(a[0])):
    l=[]
    for j in range (len(a)):
        l.append(a[j][i])
    t.append(l)
print(t)
===============================================================================
#1.Python program to find uncommon elements from two Strings

A = "Geeks for Geeks"
B = "Learning from Geeks for Geeks"
a = set(A)
b = set(B)
print(a.symmetric_difference(b))
================================================================================

#2.Python program to Replace all Characters of a List Except the given character
t = ['G', 'F', 'G', 'I', 'S', 'B', 'E', 'S', 'T']
T = []
#replacechr = ‘*’,
#remainchr = ‘G’
for i in t:
    if i != 'G':
        T.append('*')
    else:
        T.append(i)
print(T)
==================================================================================
#3. Write a Python program to remove an empty tuple(s) from a list of tuples.
A= [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
a = []
for i in A:
    if i != ():
        a.append(i)
print(a)
==================================================================================
#4.Python program to find common elements in three lists using sets

a1 = [1, 5, 10, 20, 40, 80]
a2 = [6, 7, 20, 80, 100]
a3 = [3, 4, 15, 20, 30, 70, 80, 120]
a = set(a1).intersection(set(a2))
b = a.intersection(set(a3))
print(b)
============================================================================
#5.Python – Convert Lists of List to Dictionary

s = [['a', 'b', 1, 2], ['c', 'd', 3, 4], ['e', 'f', 5, 6]]

#OUTPUT = {(‘c’, ‘d’): (3, 4), (‘e’, ‘f’): (5, 6), (‘a’, ‘b’): (1, 2)}

res = {tuple(i[:2] ): tuple(i[2:]) for i in s}
print(res)
========================================================================
#write a  Python program Accessing nth element from tuples in list.

s = eval(input('enter the list of tuple:'))
l = []
n = 1
for i in s:
    for j in i:
        l.append(j)
print(n,'th element is: ',l[n])
============================================================================
#Write Python program to find the sum of all items in a dictionary.
d = {1:2,3:4,5:6}
l = []
for i in d.items():
    for j in i:
        l.append(j)
print('sum of element present in the dictionary: ',sum(l))
=============================================================================
s = 'pratiksalaskar119'
#for i in s:
if s.isalnum()==True:
        print('true')
else:
        print('False')
=============================================================================
#write a Python program to find Cumulative sum of a listz
list = [10, 20, 30, 40, 50]
l = []
res = 0
#Output : [10, 30, 60, 100, 150]
for i in list:

    res += i
    l.append(res)
print(l)
'''




















