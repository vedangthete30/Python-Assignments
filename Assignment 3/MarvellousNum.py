def ChkPrime(lst):
    lst1 = []
    for i in range(0,len(lst)):
        if i % lst[i] != 0:
            lst1.append(lst[i])
            