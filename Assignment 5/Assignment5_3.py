class Arithmetic:
    Arithmetic = 0

    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = int(input("Enter a number : "))
        self.Value2 = int(input("Enter another number : "))
        
    def Addition(self):
        return (self.Value1) + (self.Value2)
    
    def Substraction(self):
        return abs(self.Value1 - self.Value2)

    def Multiplication(self):
        return self.Value1 * self.Value2
    
    def Division(self):
        return self.Value1 / self.Value2


def main():
    obj1 = Arithmetic()

    obj1.Accept()
    print("Addition is : ",obj1.Addition())
    print("Substraction is : ",obj1.Substraction())
    print("Multiplication is : ",obj1.Multiplication())
    print("Division is : ",obj1.Division())
    



if __name__ == "__main__":
    main()