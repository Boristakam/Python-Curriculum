#object = a bundle of related attributes(variable) and methods(functions) to represent real world items 
#         eg. phone, cup, book,..
#         you need a "class" to create many objects

# class = blueprint used to desing the structure and layout of an object

from car import Car

car1 = Car("ford", 2014, "red", False)
car2 = Car("nissan", 2024, "blue", True)

print(car1.model, car1.year, car1.colour, car1.for_sale)
car1.drive()
car1.stop()
car1.describe()

print()
print(car2.model, car2.year, car2.colour, car2.for_sale)
car2.drive()
car2.stop()
car2.describe()