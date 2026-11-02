# variable

# local variables   Ex 3

def f1(x,y):
    z = x+y
    print(x,y,z)
f1(4,5)
def f2():
    print(z) # error because local variable cannot access within another function
f2()
