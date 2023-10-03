import psutil
import os
import getpass
import sys
import datetime

def create_log_file(directory):
    try:
        log_filename = os.path.join(directory, f"process_info.log")

        # Create and return the log file
        log_file = open(log_filename, 'w')
        return log_file
    except Exception as e:
        print(f"An error occurred while creating the log file: {str(e)}")

def write_process_info_to_log(log_file):
    try:
        log_file.write("Process Information:\n")
        log_file.write("--------------------\n")

        for process in psutil.process_iter(attrs=['name', 'pid']):
            try:
                process_info = process.as_dict(attrs=['name', 'pid'])
                pid = process_info['pid']
                name = process_info['name']

                # Get the username of the process owner
                username = getpass.getuser() if os.name == 'posix' else None

                log_file.write(f"Name: {name}, PID: {pid}, Username: {username}\n")
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

    except Exception as e:
        print(f"An error occurred while writing process information to the log file: {str(e)}")

def close_log_file(log_file):
    try:
        # Close the log file
        log_file.close()
    except Exception as e:
        print(f"An error occurred while closing the log file: {str(e)}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python process_info_to_log.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]

    log_file = create_log_file(directory)

    if log_file:
        write_process_info_to_log(log_file)
        close_log_file(log_file)
        print(f"Process information written to the log file in directory: {directory}")

if __name__ == "__main__":
    main()