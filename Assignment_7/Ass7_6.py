no = int(input("enter the numbers of ellemnt count :"))
data = []
for i in range (1, no+1):
    data.append(int(input(f"enter {i} element : ")))
res =list(filter(lambda a : a>1 and all(a % i != 0 for i in range(2,round(a/2)+1)),data))
print(res)