#collection = single "variable" used to store multiple values
#List = [] ordered and changeable. duplicates OK
#Set = {} unordered (prints elms in random order) and unchangeable. but add/revove OK. no duplicates
#Tuple = () ordered and unchangeable at all. duplicates OK. faster

#list 
#the following index operation with the square brakets dont work for sets because they are unchangeable (throws err)
print("\n************  LIST  **********\n")
fruits = ["apple", "pear", "guava", "banana"]
print(fruits)
print(fruits[0])
print(fruits[2])
print(fruits[0:3]) #first 3 elements
print(fruits[::2]) #every second element starting with first element 
print(fruits[::-1]) 

for fruit in fruits:
    print(fruit, end=" ")
    
print()

print(len(fruits))

print("apple" in fruits) #TRUE
print("yam" in fruits)   # FALSE

fruits[0] = "yam"
print("yam" in fruits)   #TRUE

fruits.append("pizza")
print(fruits)
fruits.remove("pizza")
print(fruits)
fruits.insert(0, "coffee") #insert also replaces 
print(fruits)

fruits.reverse() #reversed based on the order defined not in alphabetical order. can also reverse with the index operator as shown at the start of the lesson
print(fruits)

fruits.sort()  #if sorted first then the above reverse will also be in alphabetical order
print(fruits)

print(fruits.index("pear")) #returns the index number of the element in the list 

print(fruits.count("apple")) #0

fruits.clear() #all fruits are gone in the list 


# print(dir(fruits)) #prints  different methods available to the collection
# print(help(fruits)) #description of the method listed from the previous pring


#sets:
print("\n************  SETS  **********\n")
fruits2 = {"tomato", "lemon", "lime", "berries"}
#print(fruits2[0]) #err cannot use indexing on sets
fruits2.add("pizza") #remember sets are unordered so it gets added anywhere in the set of fruits
print(fruits2)
fruits2.pop() #removes a random element (run multiple times to see)
print(fruits2)


#tupples:
print("\n************  TUPLES  **********\n")
fruits = ("apple", "pear", "guava", "banana")
print(fruits)
print(fruits.count("apple"))
print(fruits[0])



