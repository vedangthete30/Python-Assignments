
def SumOfDigits(n):
    if n < 10:
        return n
    else:
        return n % 10 + SumOfDigits(n // 10)
    
    return sum

def main():
    n = int(input("Enter a number : "))
    ans = SumOfDigits(n)
    print(ans)

if __name__ == "__main__":
    main()