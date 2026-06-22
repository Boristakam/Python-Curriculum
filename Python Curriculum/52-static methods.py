#static methodds = a method that belongs to a class rather than any object from that class (instance)
#                   Usually used for general utility functions (Code tied strictly to a class's domain)
#                   we use the @staticmethod decorator to define a static method    
#                   Static methods do not have access to the instance (self) or the class (cls) and can only access the parameters that are passed to them. 
#                   They cannot modify the state of the class or its instances. 
#                   they are used for operations that are related to the class but do not require access to any specific instance or class data. 
#                     i.e. a BankAccount class might have a static method to validate a bank account number, which does not require access to the bank account's balance or other instance-specific data.

#instance method = methods studied up to this point. they are best for operations on instances/objects of the class.
#static methods = best for utility functions that do not need access to class data 


class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self): #instance method - it needs to be called by an instance/object of the Employee class unlike the static method below
        return f"{self.name} works as a {self.position}"
    
    @staticmethod # this decorator means we dont need to to create an object of the class to use is method below it. it can be called directly from the class itself
    def is_valid_position(position):
        valid_positions = ["manager", "developer", "designer"]
        return position in valid_positions  # returns a boolean value


""" using the static method without creating an instance of the Employee class """
print(Employee.is_valid_position("manager")) # True
print(Employee.is_valid_position("janitor")) # False

""" using the instance method by creating an instance of the Employee class """
employee1 = Employee("Alice", "developer")
print(employee1.get_info()) # Alice works as a developer

employee2 = Employee("Bob", "janitor")
print(employee2.get_info()) # Bob works as a janitor