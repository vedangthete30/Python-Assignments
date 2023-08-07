def ChkNum(Value):
    if Value % 2!=0:
        print("Odd Number")
    else:
        print("Even Number")

def main():
    Number = int(input("Enter a number to check : "))
    ChkNum(Number)

if __name__ == "__main__":
    main()