class Numbers:
    def __init__(self):
        self.value = int(input("Please Enter a number : "))

    def prime(self):

        if lambda n : n > 1 and all(n % i != 0 for i in range(2,n**0.5+1)):
            print("Number is Prime ")
        else:
            print("Number is not a prime number")

    def perfect_number(self):
        add = 0 
        for i in range(1,self.value):
            if self.value % i == 0:
                add = add + i 
        if add == self.value:
            print("Number is perfect number ")

        else:
            print("Number is not a perfect number")

    def sumofffactor(self):
        sum_of_factors = 0
        for i in range(1,self.value + 1):
            if self.value % i == 0:
                sum_of_factors = sum_of_factors + i

        print("Adition of all factors of given number is :",sum_of_factors)

    def main(self):
        self.prime()
        self.perfect_number()
        self.factors()
        self.sumofffactor()

if __name__ == "__main__":
    obj = Numbers()
    obj.main()
