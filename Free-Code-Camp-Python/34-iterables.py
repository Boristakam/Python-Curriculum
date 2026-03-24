#iterable = an object/collection that can return its elements one at a time, allowing it to be iterated over in a loop

numbers = [1, 2, 3, 4] #the list numbers is an iterable. tupples, sets ans dictionaries are also iterables
fruits = {"apple", "banana", "orange"} #set
name = "bro code"   #string
my_dictionary = {"A": 1, "B": 2, "C": 3}  #dictionary


for num in reversed(numbers):
    print(num, end=" - ")


print()
for fruit in fruits: #cannot reverse sets 
    print(fruit)


for character in name:
    print(character, end="")


print("\n--- keys ---")
for key in my_dictionary.keys():
    print(key, end=" ")
print(("\n--- values ---"))
for value in my_dictionary.values():
    print(value, end=" ")
print(("\n--- keys & values ---"))
for key, value in my_dictionary.items():
    print(f"{key} = {value}")
