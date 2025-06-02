add = lambda a,b : a+b
sub = lambda a,b : a-b
multi = lambda a,b : a*b
division = lambda a,b : a/b

def main():
    print("Please enter the first number :")
    number1 = int(input())

    print("Please enter the second number :")
    number2 = int(input())

    sans = add(number1,number2)
    print("Addition is : ",sans)

    sans = sub(number1,number2)
    print("Substraction is : ",sans)

    sans = multi(number1,number2)
    print("multiplication is : ",sans)

    sans = division(number1,number2)
    print("division is : ",sans)

if __name__ == "__main__":
    main()


    