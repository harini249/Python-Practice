#exercises if else

# 1)
print("Exercise 1 : pass or fail\n")
mark = int(input())
if mark>=35:
    print("Pass")
else:
    print("Fail")
print("\n========================")

#2)
print("Exercise 2 : income greater means not eligible for scholarship\n")
Income = int(input("Income : "))
if Income<7000:
    print("Eligible for Scholarship")
else:
    print("Not Eligible for Scholarship")

print("\n=============================")

#3)
print("Exercise 3 : number divisible by 3 and 5\n")
num = int(input("num : "))
if num%3 == 0 and num %5 == 0:
    print("Divisible by 3 and 5")
else:
    print("Not divisible by 3 and 5")
    

