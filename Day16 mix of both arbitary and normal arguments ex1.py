# arbitary arguments : it takes zero or more values and default type is tuple return

#mix of both arbitary and normal arguments


def f1(*x,y):
    print(x,type(x))
    print(y,type(y))
f1(3.2,4j,False,y = 9) 
