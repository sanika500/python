# f=open("demo.txt","wt")
# f.write("hello world")
# f.close()
# f=open("demo.txt","r")
# print(f.read())
import os
f=open("demo123.txt","w")
f.write("sanika")
f.write("\nsanika")
f.write("\nsanika")
f.close()
f=open("demo123.txt")
print(f.readline())
print(f.readline())
print(f.readline())
f.close()
# if os.path.exists("demo123.txt"):
#     os.remove("demo123.txt")
# else:
#     print("file does not exist")
    