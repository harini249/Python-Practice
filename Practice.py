def employee(name, role = "Python developer", *skills):
    print(f"Name: {name}")
    print(f"Role: {role}")
    print(f"Skill: {skills}")

employee("Harini", "Python Developer", "SQL", "Git", "FastAPI")
employee("Kavi", "Data Analyst", "Python", "SQL", "Excel")
employee("Anu")
