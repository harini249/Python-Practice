# Working with builtin funtions

print("Working with builtin funtions\n")
x = [6,7,2,4,9]
print(x)
#len()
print("\nlen of list : ",len(x))
print("\nsum of list : ",sum(x))
print("\nmin of list : ",min(x))
print("\nmax of list : ",max(x))
print("\n sorted of list : ",sorted(x))
print("\nreversed of list : ",reversed(x)) # this return the obj no day so need means change to any datatype to display the data
print("\n reversed of list ",list(reversed(x)))

# working with list class methods

print("\n   working with list class methods ")
y = [1,2,4]
print("\n print y : ",y)
y.append(90)
print("\n After appending : ",y)
y.clear()

print("\n after clear : ",y)

y = [1,2,4]
a = y  # hard copy
print(y)
print("\n After hard copy y to a : ",a )

z = x.copy()
print("\n After shallow copy : ",z)

print("\n id of y : and  a : and z :",id(y),id(a),id(z), id(x))
