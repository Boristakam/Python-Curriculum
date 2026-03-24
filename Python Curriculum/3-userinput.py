# print("What is your name?: ")
# name = input() #returns the user input as a string
# print("How old are you?:")
# age = input()  #returns the user input as a string, there value given cannot used as int

# simplifying the above code
name = input("What is your name?: ")
age = int(input("How old are you?: ")) #casting to int before return input data is always str

age = int(age)
age += 1

print(f"Thanks, your name is {name}, you are {age} years old\n")


#Exercise 1 rectangle are calc
length = int(input("What is the length of your rectange?: "))
width = int(input("What is the width of your rectange?: "))
area = length * width
print(f"The area of your rectangle is {area} cm²")


#Exercise 2 shopping cart program 
item = input("what item would you like to buy?: ")
price = float(input("what is the price?: "))
quantity = int(input("how many would you like?: "))
cost = price * quantity
print(f"your total is ${cost}")