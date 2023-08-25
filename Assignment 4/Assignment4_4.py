from functools import reduce

even = lambda i : (i % 2 == 0)
square = lambda i : (pow(i, 2))
add = lambda n1, n2 : n1 + n2


def main():
    lst = []
    n = int(input("Enter number of elements : "))
    print("Enter elements : ")
    for i in range(0, n):
        elements = int(input())
        lst.append(elements)

    foutput = list(filter(even, lst))
    print(foutput)

    moutput = list(map(square, foutput))
    print(moutput)

    routput = reduce(add, moutput)
    print(routput)

if __name__ == "__main__":
    main()