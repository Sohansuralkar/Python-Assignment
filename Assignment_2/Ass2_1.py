import arithmatic as A

print("Enter The first number")
a = int(input())

print("Enter second number : ")
b = int(input())

aans = A.Addition(a,b)
print("Addition is :",aans)

sans = A.Subraction(a,b)
print("Substraction is : ",sans)

mans = A.Multiplication(a,b)
print("Multiplicatuion is : ",mans)

dans = A.Division(a,b)
print("Division is :",dans)