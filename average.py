a=int(input("enter the number of elements"))
print("enter the elements")
b=[]
for i in range(a):
    c=int(input())
    b.append(c)

try:
    d=sum(b)/a
    print(d)
except ZeroDivisionError:
    print("enter only numbers")
except NameError:
     print("the number is")
finally:
    print("completed")         