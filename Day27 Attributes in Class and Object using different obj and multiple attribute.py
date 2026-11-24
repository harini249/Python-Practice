# Attributes in class and object  using different obj and multiple attribute

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age 

student1 = Student("Harini",22)
student2 = Student("Anu",21)

print("Student 1: ",student1.name)
print("Age: ",student1.age)
print("Student 2: ",student2.name)
print("Age: ",student2.age)
