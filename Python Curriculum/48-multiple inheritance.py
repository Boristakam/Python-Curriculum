# multiple inheritance = inherits from more that 1 parent clss
#                        C(A, B) #C inherits from A and B
# multilevel inheritance = inherit from a parent which inherits from another parent. C(B) <- B(A) <- A   


class Animal: #parent class
    def __init__(self, name): #constructor
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

class Prey(Animal): #parent Rabbit, Hawk and Fish classes, and child of Animal class
    def flee(self):
        print(f"{self.name} is fleeing ")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name}is hunting ")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator): #can access attr and methods from both parent classes. as well as parent of parent
    pass

rabbit = Rabbit("bugs")
hawk = Hawk("tony")
fish = Fish("nemo")

rabbit.flee()
hawk.hunt()
fish.hunt()
fish.flee()
fish.eat()

#would use a super() function to access/use the constructor of a parent class