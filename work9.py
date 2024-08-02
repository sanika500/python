# a=(input("enter a word"))
# import re
# x=re.search("^a",a)
# if x:
#     print("name starts with a")
# else:
#     print("name not starts with a")

# a=(input("enter a word"))
# import re
# x=re.search("p$",a)
# if x:
#     print("the name ends with p")
# else:
#     print("name not ends with p")

a=(input("enter a word"))
import re
x=re.search("^a.*p$",a)
if x:
    print("the name starts with a and end with p")
else:
     print("the name  not starts with a and end with p")


