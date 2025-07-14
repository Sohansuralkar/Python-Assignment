import psutil

def process_infor():
    for pro in psutil.process_iter():
        res = pro.as_dict(attrs=["name","pid","username"])
        print(res)

def main():
    process_infor()

if __name__ == "__main__":
    main()