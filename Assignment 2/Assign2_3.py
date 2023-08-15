def Factorial(num):
    ans = 1
    for i in range(1, num + 1):
        ans = ans * i
    
    return ans

def main():
    Number = int(input("Enter a number to calculate its factorial : "))
    Ans = Factorial(Number)
    print("Factorial of the given number is : ", Ans)

if __name__ == "__main__":
    main()