class Car: 
    def __init__(self, model, year, colour, for_sale): #dunder method - the constructor - behaves similar to a function - self means this object we're creating right now (the car)
        self.model = model
        self.year = year
        self.colour = colour
        self.for_sale = for_sale

    def drive(self):
        print(f"your drive the {self.colour} {self.model}")
        
    def stop(self):
        print(f"you stop the {self.colour} {self.model}")

    def describe(self):
        print(f"{self.year} {self.colour} {self.model}")
