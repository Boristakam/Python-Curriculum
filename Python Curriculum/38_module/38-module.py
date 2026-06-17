#module = python file containing code you want to include in your program (can be your own or a library module)
#         can be imported into other python files using the import statement
#         use the import statement to include the module in your program         I.E. import math
#         usefule to break down large programs into smaller, manageable pieces 


#print(help("module"))  # Displays help information about the module system
#print(help("import"))  # Displays help information about the import statement

#import math
# print(math.pi)  # Output: 3.141592653589793 

#import math as m # renames the module to 'm' for easier access
#print(m.pi)  # Output: 3.141592653589793 

#from math import pi  # imports only the 'pi' constant from the math module
#print(pi)  # Output: 3.141592653589793
# NOTE this approach is memory efficient but can lead to name conficts if multiple modules have the same function or variable names


#now importing my own module
import example
result = example.pi
print (result)
result = example.square(3)
print(result)
result = example.cube(3)
print(result)
result = example.circumference(5)
print(result)
result = example.area(5)
print(result)

