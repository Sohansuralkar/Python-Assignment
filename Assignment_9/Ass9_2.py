import multiprocessing

def onee(l1):
    fl1 = []
    print(l1)
    for i in l1:
        t = i**2
        print(t)
        fl1.append(t)
    print("Final List is : ",fl1)

def main():
    print("Enter the coiunt of element fisrt list :")
    c1 = int(input())
    l1 = []
    for i in range(c1):
        print("Please Enter ",i,"th element")
        t = int(input())
        l1.append(t)

    p1 = multiprocessing.Process(target=onee,args=(l1,))
    p1.start()
    p1.join()

if __name__ == "__main__":
    main()