# Day 6 collection : 1) List

x = []  #creating list
print(type(x))   #to see type of variable  

print("\n==========================")

x = [2,2.3,True,"Harini",[1,3,4],(6,7,4)]   # allow data inside both mutable & immutable but list  is mutable
print("printing List : ",x)
print("\n===========================")

y = [1,2,3,4,5]
a = [1,2.3,"harini",[1,2],(2,3)]
print("List support homogenious means same data type : ",y)
print("List support heterogenious support different data type :",a)

print("\n===================================")
print("Support indexing ")
print(a[2])
