#inheritance = allows a class to inherit attributes and methods from another class
#              helps with code readability and extensibility
#              class Child(Parent) 

class Animal: 
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):  #inherited methods and attributes from class Animal but can also have uniques ones
    def speak(self):
        print(f"{self.name} says woof")

class  Cat(Animal):
    pass


dog1 = Dog("spark")
cat1 = Cat("minou")

print(f"{dog1.name}, {dog1.is_alive}")
print(f"{cat1.name}, {cat1.is_alive}")

dog1.eat()
dog1.sleep()
dog1.speak()