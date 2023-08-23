def maxNum(list):
    Max = 0
    for i in range(0,len(list)):
        if Max < list[i]:
            Max = list[i]

    return Max

def main():
    n = int(input("Enter number of elements : "))
    li = []
    print("Enter Elements : ")
    for i in range(0,n):
        val = int(input())
        li.append(val)

    max = maxNum(li)
    print(f"Maximum number from the given list is : {max}")

if __name__ == "__main__":
    main()