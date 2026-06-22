# super() = function used in child class to call methods from a parent class (superclass)
#           allows to extend the functionality of the inherited methods


class Shape:
    def __init__(self,  colour, is_filled):
        self.colour = colour
        self.is_filled = is_filled

    def describe(self):
        print(f"it is {self.colour} and {'filled' if self.is_filled else 'not filled'}")


class Circle(Shape):
    def __init__(self, radius, colour, is_filled):
        self.radius = radius
        super().__init__(colour, is_filled)

    def describe(self): #method override - it overrided the describe method from the parent class
        print(f"it is a circle with an are of {3.14*self.radius*self.radius} cm^2")
        #if we still want to use the parents describe function we call it here using the super() func because we are still indirectly accessing the Shape's constructor
        super().describe()


class Square(Shape):
    def __init__(self, width, colour, is_filled):
        self.width = width
        super().__init__(colour, is_filled)


circle = Circle(radius=5, colour = "blue", is_filled = True)                                  # ternary operator
print(f"the circle is {circle.colour}, has a {circle.radius} cm radius, and {'it is filled' if circle.is_filled else 'is is not filled'} ")
circle.describe()

