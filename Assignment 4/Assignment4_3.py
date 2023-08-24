from functools import reduce

bound = lambda no : (no >= 70 and no <= 90)
increase = lambda no : no + 10
mult = lambda no1, no2 : no1 * no2


def main():
    n = int(input("Enter number of elements : "))
    lst = []
    print("Enter elements : ")
    for i in range(0,n):
        ele = int(input())
        lst.append(ele)

    foutput = list(filter(bound, lst))
    print(foutput)
    
    moutput = list(map(increase, foutput))
    print(moutput)

    routput = reduce(mult, moutput)
    print(routput)


if __name__ == "__main__":
    main()