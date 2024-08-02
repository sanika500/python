

class Employee():
    def __init__(self,name,salary):  
        self.name=name
        self.salary=salary
    def get_status(self):
        if(self.salary>100000):
            print("high salary")
        elif(self.salary>50000 and self.salary<100000):
            print("mid salary")
        else:
            print("lowsalary")
    def __str__(self):
        return f"{self.name}-{self.salary}{self.status}"
    
class Manager(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)
p1=Employee("anu",55000) 
p1.get_status() 
            

       
