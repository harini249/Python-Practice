# Attributes in class and object  using different obj and multiple attribute

#Exercise 2

class Mobile:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price

m1 = Mobile("Samsung", "Galaxy S24",75000)
m2 = Mobile("Apple","iPhone 16",80000)

print("Mobile 1: ",m1.brand,m1.model,m1.price)
print("Mobile 2: ",m2.brand,m2.model,m2.price)
