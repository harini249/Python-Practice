# types of arguments

# arbitrary keyword arguments

# loop through **kwargs  EX 2


def student(**kwargs):
    for key, value in kwargs.items():
        print(key,value)
student(name = "Harini",age = 22,course = "Python")


