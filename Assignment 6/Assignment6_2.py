class BankAccount:
    ROI = 10.5  

    def _init_(self):
        self.Name = ""
        self.Amount = 0.0
        

    def Display(self):
        self.Name = input("Enter your name: ")
        self.Amount = float(input("Enter initial amount in the account: "))
        print(f"Name: {self.Name}, Amount: {self.Amount}")

    def Deposit(self):
        deposit_amount = float(input("Enter the amount to deposit: "))
        self.Amount += deposit_amount
        print(f"Deposited {deposit_amount} successfully.")
        self.Display()

    def Withdraw(self):
        withdraw_amount = float(input("Enter the amount to withdraw: "))
        if withdraw_amount <= self.Amount:
            self.Amount -= withdraw_amount
            print(f"Withdrew {withdraw_amount} successfully.")
        else:
            print("Insufficient balance.")
        self.Display()

    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        print(f"Interest calculated: {interest}")
        self.Display()

def main():
    account1 = BankAccount()
    account1.Display()

    account2 = BankAccount()
    account2.Display()


    account1.Deposit()
    account1.Withdraw()
    account1.CalculateInterest()

    account2.Deposit()
    account2.Withdraw()
    account2.CalculateInterest()

if __name__ == "__main__":
    main()


