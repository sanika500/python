# class main():
  
#     def __init__(self):
#         print("hello")
# p=main()
# q=main()

# class School():
#     SchoolName="Technical High School"
#     Section="High School"
#     Numberofclasses=6
#     Numberofteachers=10
#     NumberofStudents=300
    
#     def __init__(self):
#         print("SCHOOL DETAILS")
#     def school(self) :
#         print(self.SchoolName) 
#         print(self.Section)
#         print(self.Numberofclasses)
#         print(self.Numberofteachers)
#         print(self.NumberofStudents)
# p=School()
# p.school()

# class Main():
#     def __init__(self,name):
#         print("my name is",name)
# p=Main("john")

# class Main():
#     def __init__(self,name):
#         self.name=name
# p=Main("john") 
# print(p.name)   

# class Master():
#     def __init__(self,name,age):
#         self.nam=name
#         self.ag=age
# p=Master("john","20")
# print(p.nam)
# print(p.ag)


# class Master():
#     def __init__(self,name,age):
#         self.nam=name
#         self.ag=age
       
#     def __str__(self):
#            return"john  20"  
           
# p=Master("john","20")
# print(p)

   
   
class master():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"{self.name} {self.age}"
p1=master("john","20")
print(p1)
           
        