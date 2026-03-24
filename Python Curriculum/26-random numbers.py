import random
#print(help(random)) #gives a list of available methods for the random module and their definitions


low = 1
high = 100
options = ("rock", "paper", "scissors")
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "K", "Q"]

number = random.randint(low, high) # random number between 1 and 100
print(number)

print(random.random())  # return a random floating point number
print(random.randint()) # return a random integer number

handshape = random.choice(options) #choice method is used to seclect random items from a list/set/tupple
print(handshape)

shufflecards = random.shuffle(cards)
print(cards)