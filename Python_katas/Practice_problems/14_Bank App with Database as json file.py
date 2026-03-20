
import json
FILE= 'LenaDenaBank.json'

def Load_data(FileName):
    try:
        with open(FileName,'r') as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        return []

def Save_data(FileName, data):
    with open(FileName,'w') as f:
        json.dump(data, f, indent=4)

def Register_new():
    print("\nRegister New Account:")
    name = input("Please enter your name: ")
    username = input("Please enter your username: ")
    password = input("Please enter your password (This will be your pin): ")
    date = input("Please enter your date of birth: ")
    balance = 0
    user = {
        "name": name,
        "username": username,
        "password": password,
        "date": date,
        "balance": balance
    }
    Data = Load_data(FILE)
    Data.append(user)
    Save_data(FILE, Data)

    print("Account Created Successfully! Please login to your account!")

def check_bal(user):
    print(f"Your Balance is: {user['balance']}")

def deposit_money(user):
    amount = float(input("Enter amount to deposit: "))
    user['balance'] += amount
    Data = Load_data(FILE)
    for d in Data:
        if d['username'] == user['username']:
            d['balance'] = user['balance']
            break
    Save_data(FILE, Data)
    print("Amount Deposited Successfully!")
    check_bal(user)

def debit_money(user):
    amount = float(input("Enter amount to be debited: "))
    if user['balance'] >= amount:
        pin = input("Please enter your pin: ")
        Data = Load_data(FILE)
        if pin == user['password']:
            user['balance'] -= amount
            for d in Data:
                if d['username'] == user['username']:
                    d['balance'] = user['balance']
                    break
            Save_data(FILE, Data)
            print("Amount debited Successfully!")
        else:
            print("Incorrect pin!")
    else:
        print("You don't have enough money to debit!")
        check_bal(user)

def change_pin(user):
    pin = input("Please enter your Existing pin: ")
    if user['password'] == pin:
        pin = input("Enter your New pin: ")
        user['password'] = pin
        Data = Load_data(FILE)
        for d in Data:
            if d['username'] == user['username']:
                d['password'] = user['password']
                break
        Save_data(FILE, Data)
        print("Pin Changed Successfully!")
    else:
        print("Incorrect Pin!")

def delete_Acc(user):
    pin=input("Please enter your pin: ")
    if pin==user['password']:
        Data = Load_data(FILE)
        new_data = [d for d in Data if d['username'] != user['username']]
        confirm = input("Are you sure you want to delete this account? (y/n): ")
        if confirm.lower() == 'y':
            Save_data(FILE, new_data)
            print("Account Deleted Successfully!")
            return True
        else:
            print("Account Not Deleted!")
            return False
    else:
        print("Incorrect Pin!")
        return False


def User_dashboard(user):
    print("\nUser dashboard:")
    while True:
        print("1. Check Balance\n2. Deposit Money\n3. Withdraw Money\n4. Change PIN\n5. Delete Account\n6. Logout")
        choice = int(input("Please enter your choice: "))
        if choice == 1:
            check_bal(user)
        elif choice == 2:
            deposit_money(user)
        elif choice == 3:
            debit_money(user)
        elif choice == 4:
            change_pin(user)
        elif choice == 5:
            if delete_Acc(user):
                return

        elif choice == 6:
            print("Logged Out!")
            return
        else:
            print("Please enter a valid choice")
            continue

def Login():
    print("\nLogin to Existing Account:")
    username = input("Please enter your username: ")
    password = input("Please enter your password (pin): ")
    Data = Load_data(FILE)
    for d in Data:
        if d['username'] == username and d['password'] == password:
            User_dashboard(d)
            return
    print("Invalid Username or Password!")


print("welcome to Lena Dena Bank")

while True:
    print("\n1. Register New Account")
    print("2. Login to Existing Account")
    print("3. Exit Application")

    try:
        inp = int(input("Please enter your choice: "))
    except:
        print("Invalid input. Enter only numbers!")
        continue

    if inp == 1:
        Register_new()
    elif inp == 2:
        Login()
    elif inp == 3:
        print("Thank you for using Lena Dena Bank!")
        break
    else:
        print("Please enter a valid choice (1–3)")
