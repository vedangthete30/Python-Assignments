from sys import *
import os
import psutil
import getpass

def create_log_file(filename):
    try:
        log_filename = f"{filename}.log"

        log_file = open(log_filename, 'w')
        return log_file
    
    except Exception as E :
        print(f"An error occured while creating the log file : {str(E)}")

def ProcInfo(log_file):
    try : 
        log_file.write("Process Information")
        log_file.write("-------------------/n")

        for process in psutil.process_iter():
            try:
                process_info = process.as_dict(attrs=['name', 'pid'])
                pid = process_info['pid']
                name = process_info['name']

                username = getpass.getuser() if os.name == 'posix' else None

                log_file.write(f"Name : {name}, PID : {pid}, Username : {username}\n")

            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

    except Exception as E:
        print(f"An error occurred while writing process information to the log file : {str(E)}")    

def close_log_file(log_file):
    try:
        log_file.close()

    except Exception as e:
        print(f"An error occurred while closing the log file: {str(e)}")


def main():
    print("---------------Process Automation Script---------------")
    log_file = create_log_file("process_info")
    ProcInfo(log_file)
    close_log_file(log_file)
    print("Process information written to the log file.")
    

if __name__ == "__main__":
    main()