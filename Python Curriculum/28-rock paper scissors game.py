import random

print("---- ROCK PAPER SCISSORS GAME ----")

rps = ("rock", "paper", "scissors")
print("you will choose a hand between rock, paper, and scissors. press 'q' to quit: ")
isRunning = True

while isRunning:   #for debugging purposes it is better to use a var here instead of TRUE & break combo 

    user_hand = None
    computer_hand = random.choice(rps)

    while user_hand not in rps:
        user_hand = input("enter your hand choice: ")

    print(f"player: {user_hand}\ncomputer: {computer_hand}")

    if user_hand == computer_hand: 
        print("it's a tie")
    elif user_hand == "rock" and computer_hand == "scissors":
        print("you win")  
    elif user_hand == "paper" and computer_hand == "rock":
        print("you win")  
    elif user_hand == "scissors" and computer_hand == "paper":
        print("you win")  
    elif user_hand == "scissors" and computer_hand == "rock":
        print("you lose")  
    else:
        print("you lose")  

    if not input("play again? (y/n): ").lower() == "y": 
        isRunning = False

print("thanks for playing!")