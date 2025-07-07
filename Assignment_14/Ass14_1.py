class Employees:
    def __init__(self,id,name,salary):
        self.name = name
        self.id = id
        self.salary = salary

    def display(self):
        print("Name :",self.name)
        print("Id :",self.id)
        print("Salary :",self.salary)

    def main(self):
        self.display()

if __name__ == "__main__":
    obj = Employees(1,"amit",50000)
    obj.main()