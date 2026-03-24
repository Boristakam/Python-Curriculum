weight = float(input("enter your weight: "))
unit = input("is the weight in kg or pounds (type K or L): ")

if unit == "K":
    weight = weight *2.205
    print(f"your weight is {round(weight, 3)} pounds")
elif unit == "L":
    weight /= 2.205
    print(f"your weight is {weight} kg")
else:
    print("YOU DID NOT ENTER A VALID UNIT")