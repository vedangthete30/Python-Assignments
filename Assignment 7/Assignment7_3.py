import threading

def even_list_sum(numbers):
    even_sum = sum(x for x in numbers if x % 2 == 0)
    print(f"Sum of even elements: {even_sum}")

def odd_list_sum(numbers):
    odd_sum = sum(x for x in numbers if x % 2 != 0)
    print(f"Sum of odd elements: {odd_sum}")

def main():

    input_str = input("Enter a list of integers separated by spaces: ")
    numbers = list(map(int, input_str.split()))

    evenlist_thread = threading.Thread(target=even_list_sum, args=(numbers,))
    oddlist_thread = threading.Thread(target=odd_list_sum, args=(numbers,))

    evenlist_thread.start()
    oddlist_thread.start()

    evenlist_thread.join()
    oddlist_thread.join()

    print("Exit from main")

if __name__ == "__main__":
    main()
