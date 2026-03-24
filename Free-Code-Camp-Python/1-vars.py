#this is my first python program

print("I like pork")
print("it's really good")

#stings
food = "pizza"
first_name = "Boris"
email = "boris@email.com"
print(first_name)
#f-string aka format sting
print(f"Hello {first_name}")
print(f"You like {food}")
print(f"Your email is {email}")

#integers
age = 27
quantity = 3
print(f"You are {age} years old")
print(f"You are bying {quantity} items")

#floats
price = 10.99
distance = 20.25 
print(f"The price is ${price}")
print(f"You ran {distance} km")

#booleans
is_student = True
for_sale   = False
if is_student:
    print("You are a student")
else:
    print("You are not a student")

if for_sale:
    print("That item is for sale")
else:
    print("The item is not for sale")