#Anagram program : Anagram string ==  same length and frequency eg : duck = kucd this have same length and frequency d,u,c,k each
string1 = input("Enter you string1 : ")
string2 = input("Enter you string2 : ")
if len(string1) == len(string2):
    if sorted(string1) == sorted(string2):
        print("Anagram string")
    else:
        print("Not Anagram string")
else:
    print("Not Anagram string")
