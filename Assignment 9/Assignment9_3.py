import os.path

def OpenCopy(fname):
    if os.path.exists(fname):
        with open(fname,'r') as Firstfile, open("Demo.txt",'a') as SecondFile:
            for line in Firstfile:
                SecondFile.write(line)
        
    else :
        print("File Doessn't exists")

def main():
    Filename = input("Enter a file name : ")
    os.chdir(r"D:\Python Assignments\Assignment 9")
    OpenCopy(Filename)

if __name__ == "__main__":
    main()