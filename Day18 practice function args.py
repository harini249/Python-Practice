def student(name, course="Python", *skills):
    print(f"Name: {name}")
    print(f"Course: {course}")
    print(f"Skills: {skills}")


student("Harini", "Python", "SQL", "Git", "FastAPI")
student("Kavi", "SQL", "Excel", "Python")
student("Anu")
