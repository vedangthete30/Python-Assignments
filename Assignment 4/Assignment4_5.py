from functools import reduce
from sympy import isprime

prime = lambda n : isprime(n)
multiply = lambda n : n * 2
max = lambda n1, n2 : n1 if n1 > n2 else n2


def main():
    lst = []
    n = int(input("Enter number of elements : "))
    print("Enter the elements : ")
    for i in range(0, n):
        element = int(input())
        lst.append(element)

    fout = list(filter(prime, lst))
    print(fout)

    mout = list(map(multiply, fout))
    print(mout)

    rout = reduce(max, mout)
    print(rout)
    

if __name__ == "__main__":
    main()