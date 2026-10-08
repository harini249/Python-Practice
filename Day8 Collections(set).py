# collection : set

#creating the set

x = {}   # empty means this will be treat as dictionary so see next step
print(type(x))

x = set()  # creating the list
print(type(x))

#perfoming some operations

a = {7,34,6,2,8,2}
print(a)
a.add(100)  #add element
print("After add : ",a)

a.remove(2)
print("\n After removing 3 : ",a)


# set is mutavle it allow only immutable so if we create list with immutable element raise error
y = {5,4,3,5,3,5,6,6,"immutable",(1,2),[2,3]}# get error mutable list is there inside set
print(y) 

