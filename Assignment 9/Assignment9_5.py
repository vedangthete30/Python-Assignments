import os.path

def StrOcccurance(fname,str):
    cnt = 0
    if os.path.exists(fname):
        fobj = open(fname, 'r')
        content = fobj.read()
        occurance = content.count(str)
        return occurance

def main():
    filename = input("Enter a file name : ")
    string = input("Enter a string to check frequency of it : ")
    os.chdir(r"D:\Python Assignments\Assignment 9")
    ans = StrOcccurance(filename, string)
    print(f"String occured for {ans} times")


if __name__ == "__main__":
    main()