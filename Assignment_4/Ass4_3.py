print("Enter the elements ")
elements = int(input())
data = []
for i in range(elements):
    print("ENter elements ", i+1, "th eelement")
    t = int(input())
    data.append(t)

fdata = list (filter(lambda a :a if a>=70 and a<=90 else False, data))
mdata = list(map(lambda a : a+10, fdata))

from functools import reduce
rdata = reduce(lambda a,b : a*b, mdata)

print("Final product is :", rdata)