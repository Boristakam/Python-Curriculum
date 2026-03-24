#str(), int(), float(), bool()

name = "Boris"
age  = 27
gpa  = 4.1
is_student = False

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

print("**************")

gpa = int(gpa) #causes truncation 
print(gpa)

age = float(age) #adds decimal 
print(age)

age = str(age) #age is no longer a number int 
print(age)
print(type(age))
#age += 1 would cause error 
