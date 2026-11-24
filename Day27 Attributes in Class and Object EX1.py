# Attributes in class and object  using different obj and multiple attribute

#Exercise 1

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary 

e1 = Employee("Harini",25000)
e2 = Employee("Anu",30000)

print("Employee 1: ",e1.name,e1.salary)
print("Employee 2: ",e2.name,e2.salary)
