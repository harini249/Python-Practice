a = int(input("Enter a value : "))
b = int(input("Enter b value : "))
operation = input("Enter any of the operation to perform add/sub/mul/div : ")
if operation == "add":
    print(a+b)
elif operation == "sub":
    print(a-b)
elif operation == "mul":
    print(a*b)
elif operation == "div":
    print(a/b)
else:
    print("operation is not listed ")
