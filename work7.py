# k=lambda a,b:a+b
# l=lambda a,b:a-b
# m=lambda a,b:a*b
# n=lambda a,b:a/b

from lambda2 import *

print(""" 1.Addition
          2.subtraction
          3.multiplication
          4.division
          enter your choice """)
choice=int(input())
a=int(input("enter a number"))
b=int(input("enter a number"))
if (choice==1):
       add(a,b)
elif(choice==2):
        sub(a,b)
elif(choice==3):
        mul(a,b)
elif(choice==4):
       div(a,b)
else:
        print("wrong choice") 