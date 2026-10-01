salary = int(input("Enter your salary : "))
age = int(input("Enter your age : "))
if salary>=20000 or age<=25:
    loan_amt = int(input("Enter your loan amount : "))
    if loan_amt>=50000:
        print("Maximum loan amount")
    else:
        print("Eligible for loan ")
else:
    print("Not eligible for loan")
