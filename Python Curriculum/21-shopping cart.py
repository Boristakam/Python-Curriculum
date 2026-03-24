foods = []
prices = []
total = 0

while True:
    food = input("enter a shopping item enter (q) at anytime to quit: ")
    if food.lower() == "q":
        print("thanks for the list!")
        break
    else:
        price = float(input(f"enter the $price of {food}: "))

    foods.append(food)
    prices.append(price)

print("\n---Your shopping list---\n")
for food in foods:
    print(food)

for price in prices:
    total += price

print(f"\nyour total is ${total:.2f}")

    