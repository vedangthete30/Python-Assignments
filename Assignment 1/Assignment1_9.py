def First10Even():
    for i in range(2, 20 + 1, 2):
        print(i, end=" ")

def main():
    print("First 10 Even numbers are : ")
    First10Even()

if __name__ == "__main__":
    main()