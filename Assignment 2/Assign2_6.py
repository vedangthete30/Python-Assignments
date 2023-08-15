# Enter a number : 5
# *  *  *  *  *
# *  *  *  *
# *  *  *
# *  *
# *


def Display(num):
    for i in range(num):
        for j in range(num):
            print("* ", end = " ")

        print()
        num = num - 1

def main():
    num = int(input("Enter a number : "))
    Display(num)

if __name__ == "__main__":
    main()