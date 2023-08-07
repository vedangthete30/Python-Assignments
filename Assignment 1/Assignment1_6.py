def ChkNumber(Value):
    if (Value > 0):
        print("Positive Number")
    elif(Value < 0):
        print("Negative Number")
    else:
        print("Zero")


def main():
    Number = int(input("Enter a number : "))
    ChkNumber(Number)

if __name__ == "__main__":
    main()