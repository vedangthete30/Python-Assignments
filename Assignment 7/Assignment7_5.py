import threading

def thread_1():
    for i in range(1, 51):
        print(f"Thread 1: {i}")

def thread_2():
    for i in range(50, 0, -1):
        print(f"Thread 2: {i}")

def main():

    t1 = threading.Thread(target=thread_1)

    t1.start()

    t1.join()

    t2 = threading.Thread(target=thread_2)

    t2.start()

    t2.join()

    print("Both threads have finished.")

if __name__ == "__main__":
    main()
