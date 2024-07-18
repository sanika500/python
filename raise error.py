a=int(input("enter the marks"))
b=[]
for i in range(a):
    c=int(input())
    b.append(c)
try:
    d=sum (a)
    print(d)
    raise TypeError
except ZeroDivisionError:
    print("enter the limit")
except NameError:
    print ("the number is")
finally:
    print("completed")
      
    

