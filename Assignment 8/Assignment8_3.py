def Display(n):
    if n > 0:
        print(n, end = " ")
        n -= 1
        Display(n)

def main():
    n = int(input("Enter a number : "))
    Display(n)

if __name__ == "__main__":
    main()