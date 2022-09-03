n=int(input("enter the number"))
if n<1:
    raise expection("no number less than")

n=str(input("enter a string"))
if not type(n) is int:
    raise typeerror("only integer allowed")