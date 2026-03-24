#python banking program 



import __main__


def show_balance(balance):
    print(f"Your current balance is: ${balance:.2f}\n")

def deposit(balance, amount):
    if amount > 0:
        balance += amount
        print(f"Deposited: ${amount:.2f}\n")
    else:
        print("Deposit amount must be positive")
        print()
    return balance # so the show_balance function can access the updated balance

def withdraw(balance, withdraw_amount):
    if withdraw_amount > 0 and withdraw_amount <= balance:
        balance -= withdraw_amount
        print(f"Withdrew: ${withdraw_amount:.2f}")
    elif withdraw_amount > balance:
        print("Insufficient funds for this withdrawal.\n")
    else:
        print("Withdrawal amount must be positive.\n")
    return balance # so the show_balance function can access the updated balance


def main():
    balance = 0 
    is_running = True

    while is_running:
        print("--- banking program ---")
        print("   1.show balance")
        print("   2.deposit")
        print("   3.withdraw")
        print("   4.exit")

        choice = input("enter your choice 1-4: ")
        match choice:
            case '1':
                show_balance(balance)
            case '2':
                amount = float(input("enter the amount to be deposited?: "))
                balance = deposit(balance, amount)
            case '3':
                withdraw_amount = float(input("enter the amount to be withdrawn?: "))
                balance = withdraw(balance, withdraw_amount)
            case '4':
                is_running = False
                print("exiting the banking program. thank you for using our service.\n")
            case _:
                print("that is not a valid choice\n")


if __name__ == '__main__':
    main()
