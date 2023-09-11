i = 1
def Display(n):
    global i 
    if i <= n:
        print(i, end = " ")
        i += 1
        Display(n)

def main():
    num = int(input("Enter a number : "))
    Display(num)

if __name__ == "__main__":
    main()