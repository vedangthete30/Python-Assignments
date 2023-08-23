def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count
 
 
# Driver Code
lst=[]
n = int(input("Enter number of elements : "))
print("Enter elements : ")

for i in range(0,n):
    num = int(input())
    lst.append(num)

x = int(input("Enter element to search : "))

print('Frequency is : ',countX(lst, x))
