# 1) Printing char is digit or alpha or special character with  using built in funstions

char = input("Enter here : ")
if char.isalpha():
    if char.islower():
        print("Char is lower Aphabetic")
    else :
        print("Char is upper Alphabetic")
elif char.isdigit():
    print("Digits")
else:
    print("Symbols")

# 2) Printing char is digit or alpha or special character  usingout built in funstions

char = input("Enter here : ")
if (char>='a' and char<='z') or (char>="A" and char<="Z"):
    if (char>='a' and char<='z'):
        print("Char is lower Aphabetic")
    else :
        print("Char is upper Alphabetic")
elif (char>='0' and char<='9'):
    print("Char is numeric")
else:
    print("char is symbols")



    
