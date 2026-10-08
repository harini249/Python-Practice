# collection : Dictionary

# creating dictionary

x = {}  # empty dict
print(type(x))


X = {1:"harini",2:"dhan",3:"hema"}
print(X,type(X))

#Retrive  the dict
print("\nRetreiving the data : ",X[1])  


#update the dict
X[3] = "parveen"
print("\nAfter update the data : ",X)

#dict class methods 

# get method is used to get the value of key
print("To  get the values of key : ",X.get(1))
