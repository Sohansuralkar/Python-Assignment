#return minimum number from list

print("Enter the numbers :")
elements = int(input())
flist = []
for i in range(elements):
    print("Enter ", i+1, "th elemnt")
    t = int(input())
    flist.append(t)
from functools import reduce
fans = reduce(lambda a, b : a if a<b else b, flist)
print("minimum value is :",fans)
