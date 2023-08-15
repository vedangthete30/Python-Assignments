def AddFactors(num):
    ans = 0
    for i in range(1, num):
        if num % i == 0:
            ans = ans + i
    return ans

def main():
    Number = int(input("Enter a number : "))
    Ans = AddFactors(Number)
    print("Addition of the factors is : ", Ans)

if __name__ == "__main__":
    main()