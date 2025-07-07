class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def d(self):
        print("In parent class:")

class Teacher(person):
    def __init__(self, name, age,subject,salary):
        super().__init__(name, age)
        self.subject = subject
        self.salary = salary

    def display(self):
        print(self.name)
        print(self.subject)
        print(self.age)
        print(self.salary)
        self.d()


if __name__ == "__main__":
    obj = Teacher("XYZ",10,"English",50000)
    obj.display()