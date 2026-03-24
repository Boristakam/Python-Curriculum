import math #importing maths class. this is not needed for part one of this lesson 


#Part 1

print("\n *****Part1*****\n")
friends = 0
friends += 1 #augmented assigment operator 
friends -= 2
print(f"You have {friends} friends")

friends *= (-3)
print(f"You have {friends} friends")

friends /= 2
print(f"You have {friends} friends")

friends **= 2 #power of 2
print(f"You have {friends} friends")

remainder = friends % 2 #modulus operator
print(remainder)

#math functions
x = 3.14
y = -4
z = 5
result = round(x,1) #3.1
result = abs(y)   #4
result = pow(4,3) #64
result = max(x, y, z)
result = min(x, y, z)
print(result)


#Part2

print("\n *****Part2*****\n")
print(math.pi)
print(math.e) #exponential constant
print(math.sqrt(4))
print(math.ceil(5.2))
print(math.floor(5.2))

radius = float(input("\nlets find the area of a circle. \nwhats the radius in cm?: "))
print(f"the area is {round((pow(radius, 2) * math.pi), 1)} cm^2\nalso the circumference of the circle is {round(math.pi * (2 *radius), 2)}")