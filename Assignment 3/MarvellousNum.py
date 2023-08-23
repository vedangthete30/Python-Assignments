def ChkPrime(lst):
    lst1 = []
    for i in lst:
        if i == 0 or i == 1:
            continue
        for num in range(2, i // 2 + 1):
            if i % num == 0:
                break

        else:
            lst1.append(i)

    return lst1
