print(""" 1.Addition
          2.subtraction
          3.multiplication
          4.division
          enter your choice """)

choice=int(input())
a=int(input("enter a number"))
b=int(input("enter a number"))
if (choice==1):
    sum=a+b
    print("the sum is",a+b)
elif(choice==2):
    print("the difference is",a-b)
elif(choice==3):
    print("the product is",a*b) 
elif(choice==4):
    print("the quotient is",a/b)  
else:
    print("wrong choice")        
 
