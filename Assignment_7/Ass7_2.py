print("enter the list")
no = int(input())
data = []
for i in range(1 , no+1):
    data.append(int(input(f"please enter {i} element : ")))

res = list(map(lambda a : a*2 , data))
print(res)

