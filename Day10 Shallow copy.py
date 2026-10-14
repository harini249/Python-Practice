# Shallow copy 

# In shallow copy both the data have different memory Address
#also implemented by builtin fn,methods,comprehension ,copy(),slicing

print("Using builtin function list()")

x = [1,2,3]
y = list(x)   #x value is copied to y but different memory address 

print("Data of x : ",x)    
print("Data of y : ",y)    
print("\nMemory address of x variable : ",id(x))
print("Memory address of y variable : ",id(y))

print("\n============================")

print("\n Using copy() builtin function ")


c = [7,8,9]
d = c.copy()   # here c value is copied to d but different memory address 

print("Data of c : ",c)    
print("Data of d : ",d)    
print("\nMemory address of x variable : ",id(c))
print("Memory address of y variable : ",id(d))


print("\n============================")
