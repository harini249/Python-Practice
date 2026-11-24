# Attributes in class and object  using different obj and multiple attribute

#Exercise 4

class Employee:
    def __init__(self,name,age,department,salary,experience):
        self.name = name
        self.age = age
        self.department = department
        self.salary = salary
        self.experience = experience
e1 = Employee("Harini",22,"IT",20000,"Fresher")
e2 = Employee("Anu",23,"IT",30000,"1 year")
e3 = Employee("Hema",23,"IT",40000,"2 year")

print("Employee 1: ",e1.name,e1.age,e1.department,e1.salary,e1.experience)
print("Employee 2: ",e2.name,e2.age,e2.department,e2.salary,e2.experience)
print("Employee 3: ",e3.name,e3.age,e3.department,e3.salary,e3.experience)
