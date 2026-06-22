""" class variables = shared amongs all instances of a class. 
    They are defined within the class but outside any instance methods and constructor (those defined within would be instace variables). 
    Class variables are used to store data that is common to all instances of the class. """


class Student:

     #class variables. all objects share this same version of it.
    class_year = 2027 #you access them using the name of the class name rather that the name of the object/instace of the class unlike for instance vars 
    num_student = 0

    def __init__(self, name, age):
        self.name = name #name and age are instance vars each object has its version of them 
        self.age = age
        Student.num_student += 1 #incrimenting our class var automatically each time an object is created. 

student1 = Student("tommy", 49) #to initialise vars we call the class
student2 = Student("alex", 15)
student2 = Student("josh", 28)

print(f"student 1 is {student1.name} of age {student1.age} is graduration in {Student.class_year}") #to read vars we call the constructor/methods
print(f"student 2 is {student2.name} of age {student2.age} is graduration in {Student.class_year}")
print(Student.num_student) #3
