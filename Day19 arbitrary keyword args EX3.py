# types of arguments

# arbitrary keyword arguments

# EX 3 normal parameter + **kwargs


def employee(name, **details):
    print("Name:", name)
    print("Details:", details)
employee("Harini",role = "Python Developer",experience = "Fresher", skill = "SQL")
