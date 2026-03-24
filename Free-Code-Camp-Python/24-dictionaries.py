#dictionary = a collection of {key: value} pairs
#             ordered and changeable. No duplicates 

capitals = {"USA": "Washington DC", 
            "India": "New Delhi",
            "China": "Beijing"}

#print(dir(capitals)) #prints all different attributes/methods of a dictionary 
#print(help(capitals)) #prints all definitions of different attributes of a dictionary 


print(capitals.get("USA")) #use the key to print the value
print(capitals.get("China")) 
print(capitals.get("Japan")) #returns none 

print()
capitals.update({"Germany": "Birlin"}) #adding new key value pair
print(capitals)
capitals.update({"USA": "Detroit"}) #changing
print(capitals)
capitals.pop("India") #removes key value pair
print(capitals)
capitals.popitem() #removes latest key value pair that was added
print(capitals)
#capitals.clear() # clears all 

print()
keys = capitals.keys() #keys method returns all keys in the dictionary. note keys are iterable same with values 
print(keys) #prints them in a list  

print()
for key in capitals.keys(): 
    print(key)

print()
for value in capitals.values(): 
    print(value)


print()
items = capitals.items()  #items() function is the only way to access all items at the same time to manipulate them 
print(items) #prints a 2D list of tuples 

for key, value in capitals.items():   #wouldnt work without the items() function 
    print(f"{key}: {value}")
