# a=int(input("enter the number of elements"))
# print("enter the elements")
# b={}
# for i in range(a):
#     c=int(input())
#     d=c**2
#     b[c]=d
# print(b)

a=int(input("enter the number of elements"))
print("enter the elements")
b=[]
for i in range(a):
    c=int(input())
    d=c**2
    b.append(c)
    b.append(d)

print(b)