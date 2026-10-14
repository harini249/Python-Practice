# deep copy

# deep copy can be implemented by deepcopy() of  copy module

from copy import deepcopy
x = [1,2,3,[4,5,[6,7]]]
y = deepcopy(x)

print("x : ",x)
print("y : ",y)
print("Memory Address of x : ",id(x))
print("Memory Address of y : ",id(y))
