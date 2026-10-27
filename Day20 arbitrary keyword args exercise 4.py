# types of arguments

# arbitrary keyword arguments

# exercise 4

def project(project_name, **details):
    print(project_name)
    for key,value in details.items():
        print(key,value)
project("AI Appointment Conflict Manager",language = "Python",backend = "FastAPI",database = "SQLite")
