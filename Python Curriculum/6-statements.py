age = int(input("enter your age: "))
if age < 18:
    print("you are too young")
elif age < 0:
    print("you have not been born yet")
elif age > 100:
    print("you are too old to sign up")
else:
    print("you are eligible to sign up")


for_sale = True
if for_sale:
    print("this item is for sale")
else:
    print("this item is not for sale")