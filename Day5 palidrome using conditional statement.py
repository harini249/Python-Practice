# 1)  string is palindrome or not  (without ignore case)
print("The palindrome check program \n")

a = input("Enter your string : ")
rev_str = a[::-1] # logic
if a == rev_str:
    print("Palindrome String : ",rev_str)
else:
    print("Not Palindrome : ",rev_str)

print("/n===============================")

# 2) string is palindrome or not (with ignore case)

b = input("Enter your string : ")
word = b.lower()
if word == word[::-1]:
    print("Palindrome ")
else :
    print("Not Palindrome ")
