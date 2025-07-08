def main():
    f = open("Student.txt","r")
    lines = f.readlines()
    print("lines :",len(lines))
    word_cnt = sum(len(line.split()) for line in lines)
    char_cnt = sum(len(line)for line in lines)
    print("words : ",word_cnt)
    print("Characters :",char_cnt)

if __name__ == "__main__":
    main()

    