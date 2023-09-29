import os
from sys import *
import shutil

def CopyDirectoryExt(Source_Dir, Dest_Dir, Extension):
    try :
        if not os.path.exists(Dest_Dir):
            os.makedirs(Dest_Dir)

        for filename in os.listdir(Source_Dir):
            src_path = os.path.join(Source_Dir, filename)
            if os.path.isfile(src_path) and filename.endswith(Extension):
                dest_path = os.path.join(Dest_Dir, filename)
                shutil.copy(src_path, dest_path)
                print(f"Copied {filename} to {Dest_Dir}")

    except Exception as E:
        print(f"An error occured : {str(E)}")


def main():
    print("-----------------Automation Script-----------------")
    print("Automation script name : ", argv[0])

    if len(argv) != 4:
        print("Invalid number of arguments!")
        exit()

    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This is file automation script")
        exit()
    
    elif (argv[2] == "-u") or (argv[2] == "-U"):
        print("Usage : Assignment10_4.py <Directory Name> <Directory Name> <Extension>")

    else : 
        CopyDirectoryExt(argv[1], argv[2], argv[3])
        print("Script Executed Successfully")

if __name__ == "__main__":
    main()
