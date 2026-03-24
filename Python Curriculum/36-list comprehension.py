#list comprehension = a concise way to create lists in python. theyre compact and easier to read than traditional loops
#                     [expression    for   value   in    iterable   if   condition]


#conventional way:
doubles = []
for x in range(1, 11): #the second element in this range function (11) is exclusive therefore our 1 to n-1 or 1 to 11 - 1 are printed
    doubles.append(x * 2)
print(doubles)


#now using a list comprehension
doubles = [x*2 for x in range(1, 11)]
print(doubles)

triples = [y*3 for y in range(1, 11)]
print(triples)

squares = [x ** 2 for x in range(1, 11)] 
print(squares)

fruits = ["apple", "banana", "orange"]
fruits = [fruit.upper() for fruit in fruits] #NOTE fruits here can be replaced with the definition of fruits above 
fruits_Initial = [fruit[0] for fruit in fruits] #takes the first character of each fruit NOTE: they are all capital letter now
print(fruits)
print(fruits_Initial)



numbers = [1, -2, -3, -4, -6, -9]
positive_numbs = [abs(num) for num in numbers] #makes all number positive 
print(positive_numbs)

#now using  condition 
positive_numbs = [num for num in numbers if num >= 0] #only retains the positive numbers 
print(positive_numbs)

even_numbs = [(num) for (num) in (numbers) if (num % 2 == 0)] #only retains even number
print(even_numbs)




grades = [85, 79, 82, 90, 56, 61, 30]
passing_graded = [grade for grade in grades if grade >= 60]
print(grades)
