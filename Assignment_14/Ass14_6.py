class calculator:
    def add(self,a,b):
        return a + b
    def sub(self,a,b):
        return a - b
    def mul(self,a,b):
        return a * b
    def div(self,a,b):
        return a/b
    
    def main(self):
        val1 = int(input("Please enter first number"))
        val2 = int(input("Please enter Second number"))
        op = input("Please enter a operation : ")
        if op == "add":
            a = self.add(val1,val2)
            print(a)
        elif op == "sub":
            a = self.sub(val1,val2)
            print(a)
        elif op == "mul":
            a = self.mul(val1,val2)
            print(a)
        else:
            a = self.div(val1,val2)
            print(a)

if __name__ == "__main__":
    obj = calculator()
    obj.main()

        