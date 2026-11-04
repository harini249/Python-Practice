# global variable

# we cannot update the global variables data within the functions

# so we use forward declaration mechanisms

x = 10
def f1():
    global x
    print("Actual data : ",x)
    x+=5  # x = x+5 which means x = 10+5 = 15
    print("After modify : ",x) # `
f1()
    
