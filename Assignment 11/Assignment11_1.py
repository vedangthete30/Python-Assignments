from sys import *
import os
import hashlib

def hashfile(path, blocksize = 1024):
    afile = open(path, 'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()

def DisplayChecksum(directory):
    log_file_name = 'checksum_log.txt'

    try:
        with open(log_file_name, 'w') as log_file:
            log_file.write(f"Checksums for files in {directory}:\n")

            # Iterate over files in the directory
            for root, dirs, files in os.walk(directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    checksum = hashfile(file_path)
                    log_file.write(f"{file}: {checksum}\n")

        print(f"Checksums saved in {log_file_name}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    print("---- Automation Script-----")

    print("Application name : " +argv[0])

    if (len(argv) != 2):
        print("Error : Invalid number of arguments")
        exit()
    
    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is used to traverse specific directory and display checksum of files")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("usage : ApplicationName AbsolutePath_of_Directory Extention")
        exit()

    try:
        arr = DisplayChecksum(argv[1])

    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception as E:
        print("Error : Invalid input",E)

if __name__ == "__main__":
    main()
