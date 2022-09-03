import platform,datetime,calendar,time,sys
a=platform.system()
print(a)
#to get os

r=dir(platform)
print(r)
import MODULE
t=dir(MODULE)
print(t)

w=datetime.datetime(2000,8,10)
print(w)
print(w.year)
print(w.day)
print(w.second)
print(w.strftime("%A"))
print(calendar.month(2000,8))
print(time.localtime())

d=sys.path
print(d)


a=min(20,55,10)
print(a)

b=max(20,55,10)
print(b)

c=pow(5,2)
print(c)

