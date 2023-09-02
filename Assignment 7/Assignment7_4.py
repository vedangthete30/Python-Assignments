#Design python application which creates three threads as small, capital, digits. All the threads accepts string as parameter. Small thread display number of small characters, capital thread display number of capital characters and digits thread display number of digits. Display id and name of each thread.
import threading

def small_characters_count(input_str):
    thread_id = threading.get_ident()
    thread_name = threading.current_thread().name
    small_count = sum(1 for char in input_str if char.islower())
    print(f"Thread ID: {thread_id}, Thread Name: {thread_name}")
    print(f"Number of lowercase characters: {small_count}")

def capital_characters_count(input_str):
    thread_id = threading.get_ident()
    thread_name = threading.current_thread().name
    capital_count = sum(1 for char in input_str if char.isupper())
    print(f"Thread ID: {thread_id}, Thread Name: {thread_name}")
    print(f"Number of uppercase characters: {capital_count}")

def digits_count(input_str):
    thread_id = threading.get_ident()
    thread_name = threading.current_thread().name
    digit_count = sum(1 for char in input_str if char.isdigit())
    print(f"Thread ID: {thread_id}, Thread Name: {thread_name}")
    print(f"Number of digits: {digit_count}")

def main():

    input_str = input("Enter a string: ")

    small_thread = threading.Thread(target=small_characters_count, args=(input_str,))
    capital_thread = threading.Thread(target=capital_characters_count, args=(input_str,))
    digits_thread = threading.Thread(target=digits_count, args=(input_str,))

    small_thread.start()
    capital_thread.start()
    digits_thread.start()

    small_thread.join()
    capital_thread.join()
    digits_thread.join()

    print("Exit from main")

if __name__ == "__main__":
    main()
