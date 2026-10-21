# arbitary arguments : it takes zero or more values and default type is tuple return

# ex 4
def f1(x,*y):
    print(x,type(x))
    print(y,type(y))
f1(2.3,4j,False,9)   
