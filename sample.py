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

