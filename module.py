f=open("sum.txt","r")
f.read()
k=0
for i in f:
    j=f.read(i)
    j=int(j)
    k=k+j
    
print(k)    
f.close

