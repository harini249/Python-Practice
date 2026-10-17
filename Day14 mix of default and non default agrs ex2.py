# mix of default args and non default

# ex 3

def calculate_salary(name, salary, bonus = 5000):
    print(f"{name}'s total salary is {salary+bonus}" )

calculate_salary("Harini", 30000)
calculate_salary("Kavi", 40000, 10000)
