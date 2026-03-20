# ---------- 1) Polymorphism with built-in len() ----------
print(len("Hello"))          # 5  -> string
print(len([1, 2, 3]))        # 3  -> list
print(len({"a": 1, "b": 2})) # 2  -> dict

# Same function name len(), different behavior depending on object type.


# ---------- 2) Polymorphism with different unrelated classes ----------
class Car:
    def move(self):
        print("Car is driving on the road")

class Boat:
    def move(self):
        print("Boat is sailing on the water")

class Plane:
    def move(self):
        print("Plane is flying in the sky")

# One interface: obj.move() works for all objects
vehicles = [Car(), Boat(), Plane()]

for v in vehicles:
    v.move()  # same method name, different output


# ---------- 3) Polymorphism with inheritance (overriding) ----------
class Animal:
    def sound(self):
        print("Some generic animal sound")

class Dog(Animal):
    def sound(self):
        # override parent method
        print("Dog says: Woof")

class Cat(Animal):
    def sound(self):
        # override parent method
        print("Cat says: Meow")

animals = [Animal(), Dog(), Cat()]

for a in animals:
    a.sound()  # which sound() runs depends on actual object


# ---------- 4) Polymorphism with duck typing ----------
class Duck:
    def swim(self):
        print("Duck is swimming")

class Fish:
    def swim(self):
        print("Fish is swimming")

# Function does not care about class, only that swim() exists
def let_it_swim(creature):
    creature.swim()

let_it_swim(Duck())  # calls Duck.swim()
let_it_swim(Fish())  # calls Fish.swim()
