# a=("apple","orange","grape")
# b="banana"
# a=list(a)
# a.append(b)
# print(a)

a=list()
print("enter the elements")
b=int(input())
for i in range(b):
    print("enter the number")
    c=int(input())
    a.append(c)
a=tuple(a)
d=list()
for k in a:
    if(k%2==0):
        d.append(k)
print(d)
