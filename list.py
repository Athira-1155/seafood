a=['apple','kiwi']
b=[1,2,3,4,5]
a.insert(0,'orange')
print(a)
#append()

a.append('banana')
print(a)

#extend()

a.extend(b)
print(a)
b.extend(a)
print(b)

#remove

a.remove('banana')
print(a)
a.pop(3)
print(a)
del a[2]
print(a)
# del a
# print(a)
a.clear()
print(a)




