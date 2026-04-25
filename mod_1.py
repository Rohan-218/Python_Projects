import mod
from mod import sum
a=int(input("Enter 1st number : "))
b=int(input("Enter 2nd number : "))
a,b=mod.swap(a,b)
print("First number = {}\nSecond number = {}".format(a,b))
sum(a,b)