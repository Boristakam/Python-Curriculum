#function = block of reusable code
#           ple () after the function name to invoke 

def happy_bd(name, age):
    print(f"happy birthday {name}, you are {age} years old!")

def display_invoice(username, amount, due_date):
    print(f"hello {username}!\nyour bill of ${amount} is due on {due_date}")

def add(x, y):
    z = x + y
    return z

def divide(x, y):
    z = x / y
    return z

def create_name(first, last):
    first = first.upper()
    last = last.capitalize() #only capitalise the first character
    return first + " " + last
    
     


#happy_bd("boris")
happy_bd("boris", 20)
display_invoice("boris", 45.3, "01/02")

print(add(5, 2))
z = divide(6, 2)
print(z)

full_name = create_name("boris", "takam")
print(full_name)

