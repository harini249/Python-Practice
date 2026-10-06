# print the maximum element in list
x = eval(input("Enter you list elements : "))
max_val = x[0]
for i in x:
    if i> max_val:
        max_val = i
print("Maximum value : ",max_val)



# print the minimum value in the list
print("\n")
y = eval(input("Enter you element in list : "))
min_val = y[0]
for i in y:
    if i<min_val:
        min_val = i
print("Minimum value is : ",min_val)
