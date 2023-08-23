def minOfList(list):
    min = list[0]
    for i in range(0, len(list)):
        if min > list[i]:
            min = list[i]

    return min

def main():
    list=[]
    n = int(input("Enter number of elements : "))
    print("Enter elements : ")
    for i in range(0,n):
        num = int(input())
        list.append(num)

    min = minOfList(list)
    print(f"Minimum from the list is : {min}")

if __name__ == "__main__":
    main()