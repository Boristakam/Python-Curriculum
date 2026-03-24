operator = input("enter and operator (+ _ * /): ")
num1 = float(input("enter the first number: "))
num2 = float(input("enter the second number: "))

if operator == "+":
    print(f"The sum is {num1 + num2}")
elif operator == "-":
    print(f"The difference is {num1 - num2}")
elif operator == "*":
    print(f"The product is {num1 * num2}")
elif operator == "/":
    print(f"The division is {round((num1 / num2), 3)}")
else:
    print("invalid operator entered")
