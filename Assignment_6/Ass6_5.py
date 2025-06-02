no = int(input("Enter the number :"))
flag = True
for i in range(2,round(no/2)):
    if no % i == 0:
        flag = False
if flag :
    print("Prime number ")
else:
    print("not a prime number")