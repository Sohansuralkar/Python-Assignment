print("Enter the elements ")
elements = int(input())
data = []
for i in range(elements):
    print("ENter elements ", i+1, "th eelement")
    t = int(input())
    data.append(t)

fdata = list(filter(lambda a :a>1 and all(a%i!=0 for i in range(2, a-1)),data))
mdata = list(map(lambda a : a*2, fdata))

from functools import reduce
rdata = reduce(lambda a,b : a if a>b else b, mdata)

print("Final product is :", rdata)