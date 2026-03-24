name=input("enter your name: ")
while name == "": 
    print("you did not enter your name")
    name=input("enter your name") #give change to exist infinite loop by entering a correct value/char

print(f"your name is {name}!")



food=input("enter a food you like: ")
while not (food == "q" or food == "Q"):
    print(F"you like {food}")
    food=input("enter another food you like: ")

print("bye")


num=int(input("enter a number between 1 to 10: "))
while num < 1 or num >10:
    print("invalid number")
    num=int(input("enter a number between 1 to 10"))
print(f"your number is {num}")
