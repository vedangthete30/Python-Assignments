def CountDigits(num):
    digit = 0
    while num != 0:
        num = num // 10
        digit = digit + 1

    return digit

def main():
    num = int(input("Enter a number : "))
    ans = CountDigits(num)
    print("Number of digits in the given value is : ", ans)

if __name__ == "__main__":
    main()