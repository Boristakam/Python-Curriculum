#nested loop = a loop within a loop (inner and outer loop)

for x in range(3):
    for y in range(1, 10):
        print(y, end="")  #the end="" is to print the result on the same line. standard print statements have a hidden line character
                            # Note: any char can be added within those double quotes (space, coma etc) and they'll be printed between each result
    print() #printing a new line


#exercise: retangle drawing
print()
rows = int(input("enter the # of rows: "))
columns = int(input("enter the # of columns: "))
symbol = (input("enter a symbol to use: "))

for x in range(rows):
    for y in range(columns):
        print(symbol, end="") 
    print()