# a={"brand":"bmw","model":"m5","price":"1.7","quantity":"40"}
# print(a)
# print(a["brand"])
# a["brand"]="mini"
# print(a)

# #get()
 # x = a.get("model")
 # print(x)
 #
 # #update()
 #
# # a.update({"price":1.9})
# # print(a)
# #
# # #add items
# #
# # a["year"]=2018
# # print(a)
# #
# # a.update({"year":2020})
# # print(a)
# #
# # #remove items
# #
# # # 1. pop()
# # # 2. popitem()
# # # 3. clear()
# # # 4. del keyword
# #
# # a.pop("quantity")
# # print(a)
# #
# # a.popitem()
# # print(a)
# #
# # a.clear()
# # print(a)
# #
# # del a
# # print(a)
# #
# # #copy
# #
# # # 1.copy()
# # # 2.dict() function
#
#
b={"brand":"maruti","model":"baleno","price":"8","quantity":"15"}
print(b)
a = b
print(a)
b.update({"price":10})
print(b)
print(a)

c=b.copy()
print(c)
c.update({"price":15})
print(c)
print(b)

# d=dict(b)
# print(d)
# d.update({"price":25})
# print(d)
# print(b)
#
# nested dictionaries

# num={
#     'a':{"one":1,"two":2,"three":3},
#     'a1':{"four":4,"five":5,"six":6}
# }
# print(num)
# print(num['a1'])
# print(num['a1']["five"])