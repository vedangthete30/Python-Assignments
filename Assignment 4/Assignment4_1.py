Power = lambda no : pow(no, 2)

def main():
    num = int(input("Enter a number : "))
    ans = Power(num)
    print(f"Power of 2 for the given number is : ",ans)

if __name__ == "__main__":
    main()