import threading

def evenfactor(no):
    sum = 0
    for i in range(1,no+1):
        if i % 2 == 0:
            sum = sum + 1
    print("Addition of even factor is :",sum)

def oddfactor(no):
    sum = 0
    for i in range(1,no+1):
        if i % 2 != 0:
            sum = sum + 1
    print("Addition of even factor is :",sum)


def main():
    print("please enter number")
    no1 = int(input())
    T1 = threading.Thread(target= evenfactor, args = (no1,))
    T1.start()
    T1.join()

    print("please enter number")
    no2 = int(input())
    T2 = threading.Thread(target= oddfactor, args = (no2,))
    T2.start()
    T2.join()

    print("Exit from main ")

if __name__ == "__main__":
    main()
