a=int(input("enter a number"))
b=int(input("enter a number"))
try:
    c=a/b
    raise TypeError
except ZeroDivisionError:
    print("enter only number")
except NameError:
    print ("the number is")
finally:
    print("completed")