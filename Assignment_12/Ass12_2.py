class Circle:
    pi = 3.14
    def __init__(self):
        self.radius, self.area, self.circumference = 0.0,0.0,0.0

    def accept(self):
        self.radius = int(input("Please Enter a radius of circle :"))

    def calculatearea(self):
        self.area = Circle.pi * self.radius * self.radius

    def calculatecircumference(self):
        self.circumference = 2 * Circle.pi * self.radius

    def Display(self):
        print("ARea of circle is :",self.area)
        print("Radius of circle is :",self.radius)
        print("Circumference of circle is :",self.circumference)

    def main(self):
        self.accept()
        self.calculatearea()
        self.calculatecircumference()
        self.Display()

if __name__ == "__main__":
    obj = Circle()
    obj.main()
