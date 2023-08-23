from Assignment3_1 import sumOfList
from MarvellousNum import ChkPrime

def main():
    n = int(input("Enter a number of elements : "))
    List = []
    print("Enter elements : ")
    for i in range(0,n):
        val = int(input())
        List.append(val)
    Plist=[]
    Plist = ChkPrime(List)
    print(Plist)
    Sum = sumOfList(Plist)
    print("Sum of the prime elements from the list is : ", Sum)


if __name__ == "__main__":
    main()