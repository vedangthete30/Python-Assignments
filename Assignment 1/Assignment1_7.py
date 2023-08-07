def ChkDivisibleBy5(Number):
    if (Number % 5 != 0):
        return False
    else:
        return True
    
def main():
    Value = int(input("Enter a number to check : "))
    Result = ChkDivisibleBy5(Value)
    print(Result)

if __name__ == "__main__":
    main()