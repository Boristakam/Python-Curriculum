#polymorphism = many form
#               to ways to achieve it:
#               1. inheritance = an object could be treated of the same type as a parent type
#               2. duck typing = object must have necessary attributes/methods

from abc import ABC, abstractmethod

class Shape:

    @abstractmethod # this makes the method abstract, meaning it must be implemented by any subclass (Circle and Square classes)
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius**2


class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side * self.side


#circle = Circle() #it's a circle and a shape
shapes = [Circle(4), Square(5)]

for shape in shapes:
    print(f"{shape.area()}cm^2")
