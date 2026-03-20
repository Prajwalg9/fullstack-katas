import random

class Account:
    def __init__(self,name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance
        print("Account created successfully!")
        self.display()
        
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}")
        
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}")
        else:
            print("Insufficient funds")
    def display(self):
        print(f"Account Holder: {self.name}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance}")

def create_acc():
    name = input("Enter your name: ")
    account_number= "PGB"+str(random.randint(100000, 999999))
    balance = 0
    return name,account_number,balance

def main():
    while True:
        print("\n1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Display Account Details")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name,account_number,balance=create_acc()
            account = Account(name,account_number,balance)
        elif choice == '2':
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == '3':
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == '4':
            account.display()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
main()