# Enter a number : 4
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4

def Display(num):
    for i in range(num):
        for j in range(1, num+1):
            print(j, end = " ")
        print()

def main():
    num = int(input("Enter a number : "))
    Display(num)

if __name__ == "__main__":
    main()