name = input("enter your full name: ")
result = len(name) #number of characters
print(result)

result = name.find("k") #gives postition of the first "k" in the input (note it is 0 indexed)
print (result)

result = name.rfind("a") #gives postition of the last "a" in the input (note it is 0 indexed)
print (result)
# -1 is returned if the char cannot be find 

name = name.capitalize() #just capitalises the first char of the sting input
print(name)
name = name.upper() #capitalises the whole sting input
print(name)

# .lower, .isdigit(returns true if string only contains digits), .isalpha(for strings of only chars no number or spaces)
# ,count("a") counts how many times a char occurs in a string, .replace("a", "b") replaces all "a" with "b"


print(help(str)) # for more functions and how to use them 




#validate user input exercise

user_name = input("create your user name\nit must not be more than 12 characters\nit must not contain spaces\nit must not contain ditgits: ")
if len(user_name) > 12:
    print("username too long!")
elif not user_name.isalpha():
    print("your username must not have digits or spaces")
elif user_name.find(" "):                    # this check is redundant because of the previous one
    print("username cannot have spaces")
else:
    print(f"welcome {user_name}!")

