def prime(no):
    for i in range(2,no):
        if no % i == 0:
            return False
    return True


def main():
    cnt = int(input("please enter count of number of element you want to enter : "))
    datalist = []
    for i in range (cnt):
        datalist.append(int(input(f"please enter {i}element : ")))
    print("original data :",datalist)


    fdata = list(filter(prime,datalist))
    print("Data after filter :",fdata)

    mdata = list(map(lambda no : no * 2,fdata))
    print("data after mappinh :", mdata)

    from functools import reduce
    datalist = []
    rdata = reduce(lambda a,b : a if a>b else b,mdata)
    print("Final answer is :",rdata)

if __name__ == "__main__":
    main()