import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
isRunning = True

print("\n----- Python number guessing game -----")
print(f"guess the random number between {lowest_num} and {highest_num} ")

while isRunning:

    guess = (input("enter your guess: "))

    if guess.isdigit():
        guess = int(guess)
        guess += 1

        if guess < lowest_num or guess > highest_num:
            print("that number is out of range")
        elif guess < answer:
            print("your guess is too low!")
        elif guess > answer:
            print("your guess is too high!")
        else:
            print("CORRECT, you got the right number!")
            print(f"number of guesses: {guesses}\n")
            isRunning = False
    else:
        print(f"invalid guess\nplease select number between {lowest_num} and {highest_num}")


