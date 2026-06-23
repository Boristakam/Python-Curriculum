# @property decorator = allows you to define a method that can be accessed like an attribute
#                       it adds additional logic when read, write, or delete attributes
#                        gives better getter, setter, and deleter methods for attributes

class Rectangle:
    def __init__(self, width, height):
        self._width = width    # the understore informs that the variable is protected/internal - shouldnt be accessed directly outside the class, but it doesnt prevent from doing so 
        self._height = height  # width and height are only meant to be used within the class 

    @property # property decorator allows the access the protected variables from another method (getter attribute)
    def width(self):
        return f"{self._width:.1f}cm"

    @property
    def height(self):
        return f"{self._height:.1f}cm"
    
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else: 
            print("width must be greater than 0")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else: 
            print("height must be greater than 0")

    @height.deleter
    def height(self):
        del self._height
        print("height has been deleted")


rectangle = Rectangle(2, 4)

rectangle.width = 7 # overwites the '2'

del rectangle.height

print(rectangle.width)
# print(rectangle.height) # this line will crash because height no longer exists