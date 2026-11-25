# Modifying Object Attributes

# Exercise 2

class Employee:
    def __init__(self,name, salary,department):
        self.name = name
        self.salary = salary
        self.department =department
        
e1 = Employee("Harini", 25000, "IT")
e2 = Employee("Anu", 30000, "HR")

print(f"{e1.name}, {e1.salary}, {e1.department}")
print(f"{e2.name}, {e2.salary}, {e2.department}")
e1.salary = 35000
print(f"{e1.name}, {e1.salary}, {e1.department}")
print(f"{e2.name}, {e2.salary}, {e2.department}")
