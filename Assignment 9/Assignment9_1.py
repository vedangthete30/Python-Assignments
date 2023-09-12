import os.path
def ChkFileExistance(Fname):
    if os.path.exists(Fname):
        print(f"{Fname} exists in the current directory")
    else:
        print(f"{Fname} doesn't exists in the current directory")

def main():
    FileName = input("Enter a file name to check : ")
    os.chdir(r"D:\Python Assignments\Assignment 9")
    ChkFileExistance(FileName)

if __name__ == "__main__":
    main()

