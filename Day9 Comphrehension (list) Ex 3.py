# List comprehension : Ex 3) program input to element into nested list


x = int(input("Enter no of list object : "))
y = int(input("Enter no of elements into each list : "))
print([[eval(input() for j in range(y)] for i i range(x)])
