class Car:
    # class attribute: shared by all Car objects
    wheels = 4

    def __init__(self, brand, color):
        # instance attributes: unique for each object
        self.brand = brand
        self.color = color

    def description(self):
        # method reading data (like a getter)
        return f"{self.color} {self.brand} with {self.wheels} wheels"

car1 = Car("Tesla", "Red")
car2 = Car("BMW", "Blue")

print(car1.description())
print(car2.description())
print(Car.wheels)   # access class attribute via class
