# n numb and store in list and return additin
#prime number and user check from main module file
# listprime nd chkprime() function contains 
#module is just a .py file which contains functions nd logic

import MarvellousNum

print("Enter the elments ")
elements = int(input())
flist = []
for i in range(elements):
    print("enter number ", i + 1 , "th elements")
    t = int(input())
    flist.append(t)

def listprime(flist):
    faddition  = 0
    for i in flist:
        if MarvellousNum.Chkprime(i):
            print("prime number :", i)
            faddition = faddition + i 
    print("addition of all prime nos is :",faddition)

listprime(flist)