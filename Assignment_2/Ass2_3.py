## print factorial number multiplication of all vales till given


print("Please enter the number")
a = int(input())
b = 1
for i in range(a, 0, -1):
    b = b * i
print(b)