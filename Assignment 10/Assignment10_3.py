from sys import *
import os
import shutil

def CopyDirectory(SourceDir, DestDir):
    try :
        if not os.path.exists(DestDir):
            os.makedirs(DestDir)

        for filename in os.listdir(SourceDir):
            source_path = os.path.join(SourceDir, filename)
            dest_path = os.path.join(DestDir, filename)

            if os.path.isfile(source_path):
                shutil.copy2(source_path, dest_path)

        print(f"Files copied from '{SourceDir}' to '{DestDir}'")

    except Exception as E:
        print(f"An error occured : {str(E)}")

def main():
    print("-------------Automation script-------------")
    print("Automation script name : ",argv[0])

    if len(argv) != 3:
        print("Invalid number of Arguments")
        exit()

    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This automation script is used to perform file automation")
        exit()

    elif(argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage : Asssignment10_3.py <Directory Name> <Directory Name>")

    else :
        CopyDirectory(argv[1], argv[2])
        print("Script Executed Successfully!")

if __name__ == "__main__":
    main()