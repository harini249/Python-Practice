# types of arguments

# arbitrary keyword arguments

# exercise 3

def employee(**kwargs):
    for key,value in kwargs.items():
        print(key, value)
employee(name = 'Harini', skill = "Python", database = "SQL")

