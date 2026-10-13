# Hard copy

# In hard copy both the data have same memory

x = [1,2,3,[4,5,[6,7]]]
y = x   #x value is copied to y

print(x)    
print(y)    
print("\nMemory address of x variable : ",id(x))
print("Memory address of y variable : ",id(y))

print("\n============================")
print("\n Single dimensional ")
# single dimensional

x[1] = 20
print("\nAfter update of x :",x)
print("Same but y value : ",y)
y[0] =10
print("\nAfter update of y : ",y)
