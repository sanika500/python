a=int(input("enter the number of elements"))
print("enter the elements")
b={}
for i in range(a):
    c=int(input())
    d=c**2
    b[c]=d
print(b)