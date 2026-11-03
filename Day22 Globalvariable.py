# Global variable

x,y = 10,20
def f1():
    z = x+y   
    print(x,y,z)  # 10,20,30
f1()
a = x-y  # -10
print(a,x,y)  # -10 , 10, 20
def f2():
    p = a+x+y  #20
    print(p,a,x,y) # 20
f2()
print(a,x,y) # -10, 10, 20


