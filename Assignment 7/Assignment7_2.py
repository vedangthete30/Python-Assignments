import threading

def even_factor_sum(num):
    even_sum = 0
    for i in range(2, num + 1, 2):
        if num % i == 0:
            even_sum += i
    print(f"Sum of even factors for {num}: {even_sum}")

def odd_factor_sum(num):
    odd_sum = 0
    for i in range(1, num + 1, 2):
        if num % i == 0:
            odd_sum += i
    print(f"Sum of odd factors for {num}: {odd_sum}")

def main():

    num = int(input("Enter an integer: "))

    evenfactor_thread = threading.Thread(target=even_factor_sum, args=(num,))
    oddfactor_thread = threading.Thread(target=odd_factor_sum, args=(num,))

    evenfactor_thread.start()
    oddfactor_thread.start()

    evenfactor_thread.join()
    oddfactor_thread.join()

    print("Exit from main")

if __name__ == "__main__":
    main()
