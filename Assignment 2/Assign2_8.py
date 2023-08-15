# Enter a number : 5
 
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

def Display(num):
    for i in range(num + 1):
        for j in range(1, i+1):
            print(j, end = " ")

        print()
        num = num + 1


def main():
    num = int(input("Enter a number : "))
    Display(num)

if __name__ == "__main__":
    main()