from sys import *
import os

def ChangeExtension(Dname, oldext, newext):
    log_file_name = 'ChangeExtension.log'

    try:
        with open(log_file_name, 'w') as log_file:
            log_file.write(f"Renaming files from '{oldext}' to '{newext}' in {Dname} : \n")

            for foldername, subfolder, files in os.walk(Dname):
                for file in files:
                    if file.endswith(oldext):
                        old_path = os.path.join(foldername, file)
                        new_name = os.path.splitext(file)[0] + newext
                        new_path = os.path.join(foldername, new_name)

                        os.rename(old_path, new_path)

                        log_file.write(f"{file} -> {new_name}\n")

        print(f"Files renamed and changes logged in {log_file_name}")

    except Exception as E:
        print(f"An error occured : {str(E)}")

def main():
    print("--------------Automation Script--------------")
    print("Automation Script name : ",argv[0])

    if(len(argv) != 4):
        print("Invalid number of arguments.")
        exit()

    if(argv[1] == "-h") or (argv[1] == "-H"):
        print("This automation script is used to perform file automation")
        exit()

    elif(argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage : Assignment10_2.py <Directory name> <.txt> <.doc>")

    else :
        ChangeExtension(argv[1], argv[2], argv[3])
        print("Script executed Succefully! Check ChangeExtension.log File for the output.") 

if __name__ == "__main__":
    main()