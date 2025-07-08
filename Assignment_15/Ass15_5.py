import sys

def main():

    filename = input("Please enter a file name : ")
    f = open(filename,"r")
    fcontent = f.read()
    st = input("please enter the string you wwant to find : ")
    frequency = fcontent.count(st)
    print("frequency is given word is : ",frequency)

if __name__ == "__main__":
    main()