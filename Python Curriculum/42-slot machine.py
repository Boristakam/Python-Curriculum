#slot machine 
import random


def spin_row():
    symbols = ["🍒", "🍋", "🍊", "🍉", "🍇"]
    return [random.choice(symbols) for symbol in range(3)] #using list comprehension to pick a random element 3 times (return list of 3 random elements)

def print_row(row):
    print("*************")
    print(" | ".join(row))
    print("*************")

def get_payout(row, bet):
    payout = 0  # Initialize payout to 0
    if row[0] == row[1] == row[2]:
            if row[0] == "🍒":
                payout = bet * 2
            elif row[0] == "🍋":
                payout = bet * 3
            elif row[0] == "🍊":
                payout = bet * 4
            elif row[0] == "🍉":
                payout = bet * 5
            elif row[0] == "🍇":
                payout = bet * 6
    return payout

def main():
    balance = 100

    print("*********************************")
    print("Welcome to the Slot Machine!")
    print("symbols: [🍒, 🍋, 🍊, 🍉, 🍇]")
    print("*********************************")

    while balance > 0:
        print(f"Your current balance is: {balance}")

        bet = input("Enter your bet amount: ")

        if not bet.isdigit():
            print("please enter a valid value")
            continue #allows the skip current loop iteration and jump back to the top - (the rest of code in the while loop is not executed , jumps back to the start of the while loop) 

        bet = int(bet)

        if bet > balance:
            print("Insufficient balance.")
            continue

        if bet <= 0:
            print("Bet must be greater than 0.")
            continue

        balance -= bet

        # Spin the slot machine
        row = spin_row()
        print("spinning...\n")
        print_row(row)

        # Calculate payout
        payout = get_payout(row, bet)
        if payout > 0:
            print(f"You won {payout}!")
        else:
            print(f"You lost")

        balance += payout #no need to subtract the bet amount here because it is done as soon as the bet is placed

        play_again = input("Do you want to play again? (Y/N): ").strip().lower() #strip function removes trailing spaces
        if play_again != 'y':
            break

    print(f"Game over! your final balance is: {balance}")
    print("Thanks for playing.")

if __name__ == '__main__': #the double underscore is called dunder (short for double under)
    main()