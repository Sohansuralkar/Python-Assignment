#n number from user and store it into list accept one another nd return frequency
print("Enter the numbers ")

element = int(input())
flist = []
for i in range(element):
    print("Enter num ", i+1, "th element")
    t = int(input())
    flist.append(t)

print("Enter another number")

at = int(input())
def sun(flist,at):
    counter = 0 
    for i in flist:
        if i == at:
            counter = counter + 1
    return counter
fans = sun(flist,at)

print("frquency of number is :",fans)
