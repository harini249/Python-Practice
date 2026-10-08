# collections : tuple

x = ()    #creating a tuple 
print(type(x))

print("====================\n")
x = (5,3,4,7)
print(x,type(x))

print("=====================\n")

# tuple is both homogenious(same datatype) and hetrogenious(different datatype)

y = (2,3,4,5)    # homogenious 
print("homogenious datatype : ",y)

f = (1,2.4,False,"Harini",[1,3],(5,4))
print("heterogenious :",f)


print("\n tuple cannot update if try will get error ")

print(y)
y[0] = 1
