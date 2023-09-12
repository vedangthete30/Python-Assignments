import os.path
import filecmp

def Compare(f1, f2):
    compare = filecmp.cmp(f1, f2)

    if compare == True:
        print("Success")
    else : 
        print("Files are not same")

def main():
    file1 = input("Enter first file name : ")
    file2 = input("Enter second file name : ")
    os.chdir(r"D:\Python Assignments\Assignment 9")
    Compare(file1, file2)

if __name__ == "__main__":
    main()