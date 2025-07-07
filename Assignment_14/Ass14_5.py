class BankAccount:
    
    def __init__(self,account_no,name,balance):
        self.account_no = account_no
        self.name = name
        self.balance = balance

    def deposite(self):
        print("existing balance :",self.balance)
        deposite_amount =int(input("enter the amount that you wnat to deposite :"))
        self.balance = self.balance + deposite_amount
        print("Balance after deposite:",self.balance)

    def withdraw(self):
        print("existing balance :",self.balance)
        withdraw_amount =int(input("enter the amount that you wnat to withdraw :"))
        self.balance = self.balance - withdraw_amount
        print("Balance after deposite:",self.balance)

    def main(self):
        self.deposite()
        self.withdraw()

if __name__ == "__main__":
    obj = BankAccount("Sohan",120,1020)
    obj.main()

    

