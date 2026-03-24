#they are a one line shortcut for the if else statement 

num1 = 5 
num2 = 2
print("positive" if num1 > 0 else "negative")
result = "even" if num1%2 == 0 else "odd"
print(f"the number is {result}")

max_num = num1 if num1>num2 else num2      #can do the same with different conditional expression =>, <=, etc
print(f"the greater number is {max_num}") 