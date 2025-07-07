class student:
    school_name = "SSC"
    def __init__(self,name,roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print(student.school_name)
        print(self.name)
        print(self.roll_no)

    def main(self):
        self.display()
        student.school_name = "HSC"
        self.display()

if __name__ == "__main__":
    obj = student("Sohan",10)
    obj.main()