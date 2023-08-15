def Prime(num):
    for i in range(2, num):
        if (num % i == 0):
            return True
        else:
            return False

def main():
    num = int(input("Enter number : "))
    Ans = Prime(num)
    if Ans == False:
        print("It is a prime number")
    else:
        print("It is not a prime number")

if __name__ == "__main__":
    main()