# Modifying Object Attributes

# Exercise 1

class Mobile:
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price
m1 = Mobile("Samsung",25000)
print("Original price and brand : ",m1.brand,m1.price)
m1.price = 30000
print("After updating the price : ",m1.brand,m1.price)
