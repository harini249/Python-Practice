# arbitary arguments : it takes zero or more values and default type is tuple return

# ex 3
def f1(*x):
    print(x,type(x))
f1(2.3,4j,False,9,(5,6),"harini",[7,8])   # more value and different data type 
