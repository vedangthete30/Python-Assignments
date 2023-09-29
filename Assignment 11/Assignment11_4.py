import os
from sys import *
import hashlib
import time

def calculate_checksum(file_path, block_size=1024):
    hasher = hashlib.md5()
    with open(file_path, 'rb') as f:
        while True:
            data = f.read(block_size)
            if not data:
                break
            hasher.update(data)
    return hasher.hexdigest()

def delete_duplicate_files(directory):
    start_time = time.time()
    log_file_name = 'deleted_duplicates_log.txt'
    duplicates = {}
    
    try:
        with open(log_file_name, 'w') as log_file:
            log_file.write(f"Deleted duplicate files in {directory}:\n")
            
            # Iterate over files in the directory
            for root, dirs, files in os.walk(directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    file_hash = calculate_checksum(file_path)
                    
                    # Check if the hash has been seen before (indicating a duplicate)
                    if file_hash in duplicates:
                        log_file.write(f"Deleted: {file_path}\n")
                        os.remove(file_path)  # Delete the duplicate file
                    else:
                        duplicates[file_hash] = file_path  # Store the hash for future comparisons

        print(f"Duplicates removed and logged in {log_file_name}")
        end_time = time.time()
        execution_time = end_time - start_time 
        print(f"Execution time: {execution_time:.2f} seconds")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    print("---------Automation Script---------")
    print("Automation script name = ",argv[0])


    if len(argv) != 2:
        print("Invalid Number of arguments ")
        exit()

    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This is a automation script")
        exit()

    elif(argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage : Assignment11_3.py <Directory Name>")

    else : 
        delete_duplicate_files(argv[1])
        print("Successfully executed the script.")


if __name__ == "__main__":
    main()