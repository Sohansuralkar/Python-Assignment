print("First number")
no1 = int(input())

print("Second number")
no2 = int(input())

print("third Number ")
no3 = int(input())

if no1 > no2 and no1 > no3:
    print("Largest number is :", no1)
elif no2 > no1 and no2 > no3:
    print("largest number is :",no2)

else:
    print("largest number is ", no3)