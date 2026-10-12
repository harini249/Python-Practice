# List comprehension : Ex 1 ) program to print even  number in list

num = int(input("Enter you number : "))
print([i for i in range(1,num+1) if i%2 == 0])
