#just a list made up of lists (good for creating tables)

fruits =     ["apple", "pear", "guava", "banana"]
vegetables = ["celery", "onion", "carrots", "potatoes"]
meats =      ["beff", "pork", "fish", "turkey"]

groceries = [fruits, vegetables, meats]                 #same result as the assignment below
# groceries = [["apple", "pear", "guava", "banana"]
#             ["celery", "onion", "carrots", "potatoes"]
#             ["beff", "pork", "fish", "turkey"]]
print(groceries[0]) #prints fruits list 
print(groceries[1]) #prints vegetables list 
print(groceries[2]) #prints meats list 

print(groceries[0][2]) #prints guava . need 2 indeces to acess each element

print()
for list in groceries:
    for item in list:
        print(item, end=" ")
    print()


#excercise: 2d keypad
print()
row1 = ("1", "2", "3")
row2 = ("4", "5", "6")
row3 = ("7", "8", "9")
row4 = ("*", "0", "#")
keypad = (row1, row2, row3, row4)

for tuple in keypad:
    for element in tuple:
        print(element, end=" ")
    print()






