import threading
def increase(no):
    print("in increase ")
    for i in range (no +1):
        print(i)

def decrease(no):
    print("in decrease")
    for i in range(50, 0 , -1):
        print(i)

def main():
    print("Enter number")
    no = int(input())
    T1 = threading.Thread(target = increase , args = (no,))
    T1.start()
    T1.join()

    T2 = threading.Thread(target = decrease , args = (no,))
    T2.start()
    T2.join()

if __name__ == "__main__":
    main()
    