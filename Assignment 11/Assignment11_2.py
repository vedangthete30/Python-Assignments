import os
import hashlib
from sys import *

# Function to calculate the checksum of a file
def calculate_checksum(file_path, block_size=1024):
    hasher = hashlib.md5()
    with open(file_path, 'rb') as f:
        while True:
            data = f.read(block_size)
            if not data:
                break
            hasher.update(data)
    return hasher.hexdigest()

def find_duplicate_files(directory):
    duplicate_files = {}
    for root, dirs, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            checksum = calculate_checksum(file_path)
            if checksum in duplicate_files:
                duplicate_files[checksum].append(file_path)
            else:
                duplicate_files[checksum] = [file_path]

    duplicate_files = {checksum: paths for checksum, paths in duplicate_files.items() if len(paths) > 1}
    return duplicate_files

def log_duplicate_files(duplicate_files):
    log_file_name = 'duplicate_files_log.txt'
    with open(log_file_name, 'w') as log_file:
        log_file.write("Duplicate files:\n")
        for checksum, file_paths in duplicate_files.items():
            log_file.write(f"Checksum: {checksum}\n")
            for file_path in file_paths:
                log_file.write(f"- {file_path}\n")

    print(f"Duplicate files logged in {log_file_name}")

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
        print("usage : python find_duplicate_files.py <directory>")
        exit()

    try:
        duplicate_files = find_duplicate_files(argv[1])
        log_duplicate_files(duplicate_files)

    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception as E:
        print("Error : Invalid input",E)

if __name__ == "__main__":
    main()
