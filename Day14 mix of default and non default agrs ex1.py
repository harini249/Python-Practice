# mixing of both non default, default arguments

# ex 2


def add(x=1,y):     # x is default , y is non default arguments
    z = x+y
    print(z)    # error because non default args never follow default arguments 
add(4,5)

