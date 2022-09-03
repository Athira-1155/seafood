#loop

f=["apple","orange","kiwi","mango"]
for i in f:
    print(i)

c=("ford","maruthi","suzuki",10)
for n in c:
    print(n)

i={"arun","ibaco","snowy"}
for c in i:
    print(c)
c={"model":"mustang","brand":"BMW","year":1964}
for i in c:
    print(i)

e = {"arun":"chocalate","ibaco":"stwbry","snowy":"vanila"}
for i,h in e.items():
    print(i,h)

e={"arun":"chocalate","ibaco":"stwbry","snowy":"vanila"}
for i in e.values():
    print(i)
s="i am the sorry aliya"
for x in s:
    print(x)

#break statement
vehicle=["bus","car","bike"]
for i in vehicle:
    if i=="car":
        break
    print(i)
#continue statement
l=[10,20,30,40]
for i in l:
    if i==30:
        continue
    print(i)
#Range function
for i in range(7):
    print(i)
for i in range(2,7,2):
    print(i)
for i in range(2,7,3):
    print(i)
#else ststement in for loop
for i in range(15):
    print(i)
else:
    print("we are")

for i in range(7):
    if i==7:
        break
    print(i)
else:
    print("mine")
#pass statement
for i in range(8):
    pass


c={"arun":"chocalate","ibaco":"stwbry","snowy":"vanila"}
n={20,30,40,50}
for i,j in c.items():
    for y in n:
         print(i,j,y)
