def main():
    f = open("Student.txt","w")
    l = {"SOhan","suralkar"}
    for i in l:
        f.write(i+"\n")
    f.close()

if __name__ == "__main__":
    main()