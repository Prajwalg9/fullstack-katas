class Car:  # define a blueprint called Car
    def __init__(self, brand, color):  # runs when you create a Car
        self.brand = brand  # attribute: brand of this specific car
        self.color = color  # attribute: color of this specific car

    def drive(self):  # method: behavior of the car
        print(f"{self.color} {self.brand} is driving")

my_car = Car("Toyota", "Red")  # object (instance) of Car
my_car.drive()                 # call method on that object
