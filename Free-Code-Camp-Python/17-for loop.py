#executes a block of code a fixed number of times 
#overlaps weith while loop content

for x in range(1, 11):       #counts from 1 to 10 not to 11
    print(x)

print("\n")
for x in reversed(range(1, 11)):   #using reverse function to iterate backwards
    print(x)

print("happy new year")

print("\n")
for x in range(1, 11, 2):  #counts in steps of 2 sarting from 1. Note: can use -1 step to count backwards see next lesson
    print(x)

print("\n")
creditcard = "32298-8976-34" #printing elements of arrays/strings/sequence etc
for x in creditcard:
    print(x)

print("\n")
for x in reversed(range(1, 20)):
    if x == 13 or x == 12:          #skip number 13 and 12 using the continue keyword
        continue                    #the break keyword can be used instead if we want to exit/excape the for loop
    else:
        print(x)


#index operators