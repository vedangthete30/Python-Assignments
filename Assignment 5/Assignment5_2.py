class Circle:
    PI = 3.14

    def __init__(self, radius):
        self.Radius = radius
        
    def Accept(self):
        print("Radius given by the user is : ", self.Radius)

    def CalculateArea(self):
        area = (Circle.PI) * (pow(self.Radius, 2))
        print("Area of circle is : ", area)

    def CalculateCircumference(self):
        circumference = 2 * Circle.PI * self.Radius
        print("Circumference is : ", circumference)


def main():
    r = float(input("Enter radius : "))
    obj1 = Circle(r)
    obj1.Accept()
    obj1.CalculateArea()
    obj1.CalculateCircumference()


if __name__ == "__main__":
    main()