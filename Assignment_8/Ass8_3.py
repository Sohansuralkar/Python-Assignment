import threading

def evenlistadd(l1):
    sum = 0
    for i in l1:
        if i % 2 == 0:
            sum = sum + 1
    print("Addition of even element  is :",sum)

def oddlistadd(l2):
    sum = 0
    for i in l2:
        if i % 2 != 0:
            sum = sum + 1
    print("Addition of even element is :",sum)


def main():
    print("please enter number of element : ")
    lec = int(input())
    lec1 = []
    for i in range(lec):
        print("Enter number ", i ,"th elemnt : ")
        t = int(input())
        lec1.append(t)
    print(lec1)
    T1 = threading.Thread(target = evenlistadd, args=[(lec1,)])
    T1.start()
    T1.join()

    print("please enter number of element : ")
    lec2 = int(input())
    lec2 = []
    for i in range(lec2):
        print("Enter number ", i ,"th elemnt : ")
        t = int(input())
        lec2.append(t)
    print(lec2)
    T2 = threading.Thread(target = oddlistadd, args=[(lec2,)])
    T2.start()
    T2.join()

if __name__ == "__main__":
    main()
