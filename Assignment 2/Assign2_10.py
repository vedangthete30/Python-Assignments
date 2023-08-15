def SumofDigits(num):
    sum = 0
    while num != 0:
        digit = num % 10
        sum = sum + digit
        num = num // 10

    return sum


def main():
    num = int(input("Enter a number : "))
    Ans = SumofDigits(num)
    print("Addition of digits is : ", Ans)


if __name__ == "__main__":
     main()