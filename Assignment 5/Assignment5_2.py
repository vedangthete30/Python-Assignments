class Circle:
    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0
        
    def Accept(self):
        self.Radius = float(input("Enter radius of circle : "))
                            

    def CalculateArea(self):
        self.Area = (Circle.PI) * (pow(self.Radius, 2))
        print("Area of circle is : ", self.Area)

    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius
        print("Circumference is : ", self.Circumference)


def main():
    obj1 = Circle()
    obj1.Accept()
    obj1.CalculateArea()
    obj1.CalculateCircumference()


if __name__ == "__main__":
    main()