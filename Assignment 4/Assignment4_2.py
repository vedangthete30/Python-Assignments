Multi = lambda num1,num2 : num1 * num2

def main():
    num1 = int(input("Enter a num1 : "))
    num2 = int(input("Enter a num2 : "))

    ans = Multi(num1, num2)
    print("Multiplication of given numbers is : ", ans)

if __name__ == "__main__":
    main()