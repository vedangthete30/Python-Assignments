# Pattern - if number is 5 then
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

def Display(num):
    for i in range(num):
        for j in range(num):
            print("* ", end = " ")
        
        print()

        

def main():
    number = int(input("Enter a number : "))
    Display(number)

if __name__ == "__main__":
    main()