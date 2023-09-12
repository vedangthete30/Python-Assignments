import os.path
def OpenRead(fname):
    if os.path.exists(fname):
        fobj = open(fname, 'r')
        if fobj:
            print("File is opened succesfully and it contains : ")
            for line in fobj:
                print(line)
            fobj.close()
        else:
            print("Unable to open the file.")
    else : 
        print("Files doesn't exists")

def main():
    FileName = input("Enter a file name : ")
    os.chdir(r"D:\Python Assignments\Assignment 9")
    OpenRead(FileName)

if __name__ == "__main__":
    main()