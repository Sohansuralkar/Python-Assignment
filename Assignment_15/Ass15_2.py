import os
def main():
    filename = input("please enter the file name :")
    fobj = open(filename,"r")
    print(fobj.read())

if __name__ == "__main__":
    main()