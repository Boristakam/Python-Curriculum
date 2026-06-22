# duct typing = another way to achieve polymorphism besides inheritance
#               object must have the minimum necessary number of attributes/methods
#               "If it looks like a duck and quacks like a duck, it must be a duck"

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("woof!")

class Cat(Animal):
    def speak(self):
        print("meow!")

class Car:
    def speak(self):
        print("honk!")


animals = [Dog(), Cat(), Car()] #list of animal objects. #NOTE: Car is not an animal object but it has the same method as the other animals 
#for every animal in the list of animals have each of them use their speak method. no err is thrown for Car object
for animal in animals:
    animal.speak() #no err is thrown for Car object
    #print(animal.alive)    #err is thrown here because the Car object does not have an alive attribute

