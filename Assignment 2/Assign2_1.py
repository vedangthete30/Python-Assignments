import Arithmetic

def main():
    num1 = int(input("Enter a number : "))
    num2 = int(input("Enter a second number : "))

    Arithmetic.Addition(num1, num2)
    Arithmetic.Subtraction(num1, num2)
    Arithmetic.Multiplication(num1, num2)
    Arithmetic.Division(num1, num2)

if __name__ == "__main__":
    main()