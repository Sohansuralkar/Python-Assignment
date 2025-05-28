#factors addition till given 

print("Enter the number")

a = int(input())
addition  = 0 

facans = []

for i in range(a):
    if i != 0 and a % i ==0:
        addition = addition + i
        facans.append(i)
print(facans)
print(addition)