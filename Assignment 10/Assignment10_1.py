import os
from sys import *

def DirectoryFileSearch(Dname, Fextension):
    log_file_name = 'DirectoryFileSearch.log'

    try :
        with open(log_file_name, 'w') as log_file:
            log_file.write(f"List of {Fextension} files in {Dname} : \n")

            for foldername, subfolder, files in os.walk(Dname):
                print("Current Directory name : ",foldername)

                for subname in subfolder:
                    print("Subfolder name is : ",subname)

                for file in files:
                    if file.endswith(Fextension):
                        file_path = os.path.join(foldername, file)
                        log_file.write(file_path + '\n')

        print(f"List of {Fextension} files saved in {log_file_name}")

    except Exception as E:
        print(f"An error occured : {str(E)}")

def main():
    print("--------------------Automation Script--------------------")
    print("Automation Script Name : ",argv[0])

    if(len(argv) != 3):
        print("Invalid number of arguments.")
        exit()
    
    if(argv[1] == "-h") or (argv[1] == "-H"):
        print("This automation script is used to perform File automation.")
        exit()

    elif(argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage : Assignment10_1.py <Directory Name> <File Extension>")

    else : 
        DirectoryFileSearch(argv[1], argv[2])
        print("Script Excecuted Successfully!")

if __name__ == "__main__":
    main()