import psutil

def get_process_info(process_name):
    try:
        process_info = None

        for process in psutil.process_iter(attrs=['name', 'pid']):
            try:
                process_attrs = process.as_dict(attrs=['name', 'pid'])
                name = process_attrs.get('name', None)

                if name and name.lower() == process_name.lower():
                    process_info = process_attrs
                    break
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

        return process_info

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

def main():
    process_name = input("Enter the name of the process: ")
    process_info = get_process_info(process_name)

    if process_info:
        print(f"Process Name: {process_info['name']}")
        print(f"PID: {process_info['pid']}")
    else:
        print(f"No running process found with the name '{process_name}'")

if __name__ == "__main__":
    main()