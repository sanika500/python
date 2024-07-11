num=int(input("enter a number"))
a=0
c=num
while(num>0):
    rem=num%10

    a=a*10+rem
  
    num=num//10

print(a) 

if(c==a):
    print("the number is palindrome")
else:
    print("the number is not palindrome")
