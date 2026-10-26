# types of arguments

# arbitrary keyword arguments

# how to access individual values ex 1

def student(**kwargs):
    print(kwargs['name'])
    print(kwargs['age'])
student(name = "Harini",age = 22,course = "Python")


