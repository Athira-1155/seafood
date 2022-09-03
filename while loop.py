# n=int(input("enter the number:"))
# i=1
# fact=1
# while(i<=n):
#     fact=fact*i
#     i=i+1
# print(fact)
#
# #add n natural numbers
# n=int(input("enter a number:"))
# i=1
# f=1
# while(i<=n):
#     f=f+i
#     i=i+1
# print(f)

#break statement
#i=0
#while(i<5):
    #print(i)
    #if i==4:
        #break
    #i=i+1

#continue statement
# i=1
# while(i<=5):
#      i=i+1
#      if i==2:
#          continue
#      print(i)
#else statement
# i=0
# while i<5:print()
#     print(i)
#     i=i+1
# else:
#     print("end")

# n=str(input("enter a type:"))
# v={"A","a","E","e","I","i"}
# while n in v:
#     print("vowels")
#     break
# else:
#     print("not vowels")
#
vowels="aeiou AEIOU"
while True:
    s=str(input("enter letter:"))
    if s in vowels:
        break
    print("not vowels")
print("vowels")
