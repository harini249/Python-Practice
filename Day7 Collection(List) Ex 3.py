# Ex 3 : Printing all possible index of particular element in list

x = eval(input("Enter your List elements : "))
elem = eval(input("Enter the element to print all possible index of that in list : "))
for i in range(len(x)):
    if x[i] == elem:
                 print(i)
