def Add(Num1, Num2):
    return(Num1 + Num2)

def main():
    Num1 = int(input("Enter First number : "))
    Num2 = int(input("Enter second number : "))
    Result = Add(Num1, Num2)
    print("Addition is : ", Result)

if __name__ == "__main__":
    main()