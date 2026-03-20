# =========================
# 1. Single Inheritance
# =========================

# Parent (base) class
class Animal:
    def __init__(self, name):
        # common attribute for all animals
        self.name = name

    def eat(self):
        # common behavior
        print(self.name, "is eating")

    def sound(self):
        # default sound (can be overridden)
        print(self.name, "makes some sound")


# Child (derived) class of Animal
class Dog(Animal):
    def __init__(self, name, breed):
        # call parent constructor to set name
        super().__init__(name)
        # child-specific attribute
        self.breed = breed

    # new method only for Dog
    def bark(self):
        print(self.name, "is barking")

    # overriding parent's sound() method
    def sound(self):
        print(self.name, "says: Woof Woof!")


# =========================
# 2. Multilevel Inheritance
# =========================

# Another level: Puppy inherits from Dog, which inherits from Animal
class Puppy(Dog):
    def __init__(self, name, breed, age_months):
        # call Dog's constructor (which also calls Animal's via super)
        super().__init__(name, breed)
        # attribute only for Puppy
        self.age_months = age_months

    # new method only for Puppy
    def play(self):
        print(self.name, "is playing. Age:", self.age_months, "months")


# =========================
# 3. Multiple Inheritance
# =========================

# First parent
class Walker:
    def walk(self):
        print("Walking on the road")

# Second parent
class Swimmer:
    def swim(self):
        print("Swimming in water")

# Child class inherits from two parents (Walker and Swimmer)
class Amphibian(Walker, Swimmer):
    def live(self):
        print("Can live on land and in water")

    # example of overriding a method if needed
    def walk(self):
        # extending parent behavior
        print("Amphibian is walking slowly (overridden method)")


# =========================
# 4. Using all the classes
# =========================

# Single inheritance demo
d = Dog("Tommy", "Labrador")
print("---- Dog object ----")
d.eat()          # inherited from Animal
d.sound()        # overridden in Dog
d.bark()         # defined in Dog
print("Breed:", d.breed)

# Multilevel inheritance demo
p = Puppy("Bruno", "German Shepherd", 5)
print("\n---- Puppy object ----")
p.eat()          # from Animal (grandparent)
p.sound()        # from Dog (parent)
p.play()         # from Puppy (child)
print("Breed:", p.breed)
print("Age (months):", p.age_months)

# Multiple inheritance demo
a = Amphibian()
print("\n---- Amphibian object ----")
a.walk()         # from Walker but overridden in Amphibian
a.swim()         # from Swimmer
a.live()         # from Amphibian

# =========================
# 5. Method Resolution Order (MRO)
# =========================

print("\n---- MRO Information ----")
# For multiple inheritance, Python uses MRO to decide which class method is called
print(Amphibian.mro())  # shows the order Python will search for methods
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
