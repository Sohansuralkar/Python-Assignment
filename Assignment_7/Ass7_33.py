no = int(input("enter the numbers of ellemnt count :"))
data = []
for i in range (1, no+1):
    data.append(int(input(f"enter {i} element : ")))
res =list(map(lambda a : a*2,data))
print(res)