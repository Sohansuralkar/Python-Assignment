class Employee:
    def __init__(self,__salary,__department,name):
        self.__salary = __salary
        self.__department = __department
        self.name = name

obj = Employee("Pqr","It",100000)
print(obj.name)
print(obj.__department)
print(obj.__salary)


        