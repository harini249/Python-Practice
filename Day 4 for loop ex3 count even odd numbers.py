# counting even number and odd numbers using for loop from 1 to 20

e_count = 0
o_count = 0
for i in range(1,21):
    if i%2 == 0:
        e_count+=1
    else:
        o_count+=1
print("Even Number count : ",e_count)
print("Odd Number count : ",o_count)
