menu = {"pizza": 3.00, 
        "nachos": 4.50,
        "popcorn": 6.00,
        "chips": 1.00,
        "soda": 5.00,
        "lemonade": 4.25}

cart = []
total = 0

#display menu 
print("------ MENU ------")
for key, value in menu.items():
    print(f"{key:9}: ${value:.2f}")
print("------------------")

while True:
    food = input("choose an item from the menu (q to quit): ")
    if food.lower() == "q": 
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("\nyour selection is: ", end="")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"total is: ${total:.2f}", end="")

