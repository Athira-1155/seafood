# class firstclass:
#     x=12
# obj=firstclass()
# print(obj.x)
#
# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# s1=Student("Anu",20)
# print(s1.name)
# print(s1.age)
#
# class Car:
#     def __init__(athi,color,year):
#         athi.color=color
#         athi.year=year
#     def Method(athi):
#         print("color of car is "+athi.color)
# c=Car("red",2000)
# c.Method()
#
# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# s1=Student("Anu",20)
# s1.age=25
# print(s1.age)
#
# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# s1=Student("Anu",20)
# del  s1.age
# print(s1.name)
# print(s1.age)
#
# class Student:
#     pass
#

# class Type:
#     def __init__(self,x):
#         self.x=x
# R1=Type("HELLO WORLD")
# print(R1.x)
#
# class Text:
#     def fun(self):
#         print("Hello World")
# obj=Text()
# obj.fun()
#
#
# class fact:
#     def factorial(self):
#         fact=1
#         n=int(input("enter the number"))
#         for i in range(1,n+1):
#             fact=fact*i
#         print(fact)
# obj=fact()
# obj.factorial()

class Bank:
    def sib(self):
        balance=10000
        print("current balance",balance)
        n=str(input("do you wanted to withdrow? "))
        if(n=="yes"):
            a=int(input("Amount:"))
            balance=(balance-a)
            print("balance amount:",balance)
            print("Do you want to continue:",balance)
        else:
            z=str(input("Do You Want To Deposite:"))
            if(z=="yes"):
                h=int(input("enter the Amount:"))
                balance=(balance+h)
                print("balance amount is:",balance)

obj=Bank()
obj.sib()






