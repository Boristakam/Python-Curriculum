# class method = allows operations related to the class itself, rather than instances of the class
#                they are not tied to any specific instance of the class and can be called on the class itself
#                Take (cls) as the first parameter which represents the class itself.
#
# Instance methods = best for operation on instances of the class (has access to object and class data)
# static methods = best for utility functions that do not need access to class data (no access to object or class data)
# class methods = best for class-level data or require access to the class itself (only has access to class data like class vars)




class Student: 

    count = 0 # class variable to keep track of the number of students created
    total_gpa = 0

    def __init__(self, name, gpa): # constructor method to initialize the name and gpa of the student
        self.name = name
        self.gpa = gpa
        Student.count += 1 # increment the count of students whenever a new student/object is created
        Student.total_gpa += gpa # add the gpa of the new student to the total gpa of all students

    """ INSTANCE NETHOD """
    def get_info(self): # instance method to return the name and gpa of the student
        return f"{self.name} has a GPA of {self.gpa}"
    
    """ CLASS METHODs """
    @classmethod
    def get_count(cls): # class method to return the total number of students created (cls gives access to the class variables)
        return f"Total number of students: {cls.count}"
    
    @classmethod
    def get_average_gpa(cls): 
        if cls.count == 0: # to avoid division by zero error
            return "No students created yet."
        return f"Average GPA of all students: {cls.total_gpa / cls.count:.2f}"
    

student1 = Student("Alice", 3.6)
student2 = Student("Bob", 3.8)

print(Student.get_count())
print(Student.get_average_gpa())