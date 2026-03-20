import random

print("Random() - Returns Random float from 0.0 to 1.0")
print(random.random())

print("Randint() - Returns Random numbers between a, b including a,b")
print(random.randint(1,100))

print("Choice() - Returns random value from array")
fruits = ["apple", "banana", "orange"]
print(random.choice(fruits))

print("Shuffle() - Shuffles list or tupples")
l1=[1,2,3,4,5]
print(l1)
random.shuffle(l1)
print(l1)