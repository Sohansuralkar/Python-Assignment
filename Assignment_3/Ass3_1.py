print("Enter number of elenments" )
elements = int(input())
flist = []
for i in range(elements):
    print("please enter ", i + 1, "th element")
    t = int(input())
    flist.append(t)
from functools import reduce
add = lambda a,b :a+b
fadd = reduce (add,flist)
print("Final addition :",fadd)
