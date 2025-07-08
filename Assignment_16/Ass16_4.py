def main():
    f = open("Student.txt","r")
    for i in range(10):
        a = int(input(f"please enter a{i} number :"))
        f.write(str(a)+"\n")
    f.close()

if __name__ == "__main__":
    main()