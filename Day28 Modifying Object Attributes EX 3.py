# Modifying Object Attributes

# Exercise 3

class Student:
    def __init__(self,name, age,course):
        self.name = name
        self.age = age
        self.course = course
        
e1 = Student("Harini", 22, "Python")
e2 = Student("Anu", 21, "SQL")

print(f"{e1.name}, {e1.age}, {e1.course}")
print(f"{e2.name}, {e2.age}, {e2.course}")
e1.age = 23
e2.course = "Python"
print(f"{e1.name}, {e1.age}, {e1.course}")
print(f"{e2.name}, {e2.age}, {e2.course}")
