# Attributes in class and object  using different obj and multiple attribute

#Exercise 3

class Book:
    def __init__(self,title,author,pages,price):
        self.title = title 
        self.author = author
        self.pages = pages
        self.price = price

b1 = Book("Python Basics","John","250 pages",450)
b2 = Book("SQL Guide","David","300 pages",550)


print("Book 1: ",b1.title,b1.author,b1.pages,b1.price)
print("Book 2: ",b2.title,b2.author,b2.pages,b2.price)
