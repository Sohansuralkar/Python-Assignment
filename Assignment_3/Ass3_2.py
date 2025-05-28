# n number from user and store it into list return maximum numb from
#list
print("Enter the numbers :")
elements = int(input())
flist = []
for i in range(elements):
    print("Enter ", i+1, "th elemnt")
    t = int(input())
    flist.append(t)
def maximum(a,b):
    if a>b:
        return a
    else:
        return b
first_element = 0
for i in flist:
    fans = maximum(first_element,i)
print("Maximum value is :",fans)
