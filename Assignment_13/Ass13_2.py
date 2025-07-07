class BankAccount:
    ROI = 10.5
    def __init__(self):
        self.name = input("Please Enter Name : ")
        self.amount = input("Please Enter a amount while creating account : ")

    def deposite(self):
        self.amount = self.amount + int(input("Please enter the amount ddo you want deposite :"))

    def withdraw(self):
        self.amount = self.amount - int(input("Please Enter amount do you want to withdraw :")) 

    def calculateIntrest(self):
        self.amount = self.amount + BankAccount.ROI
        print("Total amount after intrest :", self.amount)

    def display(self):
        print("Name is : ",self.name)
        print("Account balance is : ",self.amount)

    def main(self):
        self.deposite()
        self.withdraw()
        self.calculateIntrest()
        self.display()

if __name__ == "__main__":
    obj = BankAccount()
    obj.main()

    