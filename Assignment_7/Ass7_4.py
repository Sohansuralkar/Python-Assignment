no = int(input("enter the numbers of ellemnt count :"))
data = []
for i in range (1, no+1):
    data.append(int(input(f"enter {i} element : ")))
from functools import reduce
res =reduce(lambda a,b: a*b,data)
print(res)