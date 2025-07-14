import psutil

def process_infor(pr_name):
    for pro in psutil.process_iter():
        if pro.name() == pr_name:
            print("process is running , below the information about this process")
            print(pro.as_dict())

def main():
    print("enter a process name : ")
    process_name = input()
    process_infor(process_name)


if __name__ == "__main__":
    main()
    