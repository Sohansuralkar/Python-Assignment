print("Enter the number :")
number = int(input())

for i in range (1,number + 1):
    for j in range(i):
        print(j+1, end=" ")
    print()