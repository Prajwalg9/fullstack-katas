from abc import ABC, abstractmethod

# Abstract class: cannot create object of this class directly
class Shape(ABC):
    def __init__(self, color):
        # common attribute for all shapes
        self.color = color

    @abstractmethod
    def area(self):
        # abstract method: only a rule (no body here)
        # every child class MUST implement this
        pass

    def show_color(self):
        # normal (concrete) method: has implementation
        print("Color of shape:", self.color)


# Concrete class 1
class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        # actual formula is hidden inside, user just calls area()
        return 3.14 * self.radius * self.radius


# Concrete class 2
class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# Using abstraction
shapes = [
    Circle("Red", 5),
    Rectangle("Blue", 4, 6)
]

for s in shapes:
    s.show_color()              # common interface
    print("Area:", s.area())    # same method name, different formulas inside
