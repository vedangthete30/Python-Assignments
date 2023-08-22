def sumOfList(list1):
    sum = 0
    for i in range(0, len(list1)):
        sum = sum + list1[i]

    return sum


def main():
    list1 = []
    n = int(input("Enter number of elements : "))
    print("Enter Elements : ")
    for i in range(0,n):
        value = int(input())
        list1.append(value)

    Sum = sumOfList(list1)
    print(f"Sum of list elements is : {Sum}")

if __name__ == "__main__":
    main()