i = 1
fact = 1
def Factorial(n):
    global i, fact
    if i <= n:
        fact = fact * i
        i += 1
        Factorial(n)
    
    return fact

def main():
    n = int(input("Enter a number : "))
    ans = Factorial(n)
    print(ans)

if __name__ == "__main__":
    main()