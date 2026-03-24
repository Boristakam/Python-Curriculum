import random

#print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518") #prints these unicode characters uses for ascii art = ● ┌ ─ ┐ │ └ ┘

dice_art = {1: ("┌─────────┐",
                "│         │",
                "│    ●    │",
                "│         │",
                "└─────────┘"), 
            2: ("┌─────────┐",
                "│    ●    │",
                "│         │",
                "│    ●    │",
                "└─────────┘"),
            3: ("┌─────────┐",
                "│  ●      │",
                "│    ●    │",
                "│      ●  │",
                "└─────────┘"),
            4: ("┌─────────┐",
                "│  ●   ●  │",
                "│         │",
                "│  ●   ●  │",
                "└─────────┘"),
            5: ("┌─────────┐",
                "│  ●   ●  │",
                "│    ●    │",
                "│  ●   ●  │",
                "└─────────┘"),    
            6: ("┌─────────┐",
                "│  ●   ●  │",
                "│  ●   ●  │",
                "│  ●   ●  │",
                "└─────────┘")}

dice_rolled = []
total = 0
number_of_dice = int(input("how many dice?: "))

for die in range (0, number_of_dice):  #note the 0 can be omited 
    dice_rolled.append(random.randint(1, 6))


# for die in range(number_of_dice):
#                               #key       #iterator to get all values
#     for line in dice_art.get(dice_rolled[die]):
#         print(line)


""" for printing the dice art horizontally instead of vertically as done above
    it's a little more complex: you have to print the first line of every die art first, then the second lines and so on
    therefore a total of 5 iterations 
"""
for line in range(5): 
    for die in dice_rolled:
                           #get tuple 1's line 1 etc etc
        print(dice_art.get(die)[line], end=" ")
    print() #to stack the lines


for die in dice_rolled:
    total += die

#print(dice_rolled)      
print(f"total: {total}")
