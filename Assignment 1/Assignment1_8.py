def Display(Number):
    for i in range (Number):
        print("*", end=" ")
def main():
    Number = int(input("Enter how many stars you want to print : "))
    Display(Number)

if __name__ == "__main__":
    main()