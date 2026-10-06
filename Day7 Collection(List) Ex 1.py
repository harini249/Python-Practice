# Collections : List Ex 1 : program to print list obj through iterable obj

print("List through while loop \n")
x = eval(input("Enter the items : "))   
i = 0
while i<len(x):
    print(x[i])
    i+=1
    
print("\n List through for loop")

c = eval(input("Enter the items : "))
for i in c:
    print(i)

print("\n Print nested list element  through iteration")

a = eval(input("Enter nested list : "))
for i in a:
    print(i)

print("\n Retrieve each element from nested list ")

f = eval(input("Enter a nested list to display each elemnet through iteration : "))
for i in f:
    for j in i:
        print(j)
