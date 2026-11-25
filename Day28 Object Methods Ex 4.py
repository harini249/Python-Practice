# Object Methods

# Exercise 4

class Student:
    def __init__(self,name,course):
        self.name = name
        self.course = course
    def display(self):
        print("Name: ",self.name)
        print("Course: ",self.course)

s1 = Student("Harini","Python")
s2 = Student("Anu","SQL")
s1.display()
s2.display()
