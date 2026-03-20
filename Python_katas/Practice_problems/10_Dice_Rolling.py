import random

while True:
    inp=input("Press Enter to roll a dice or q to quit?")
    if inp=='q':
        break
    else:
        print(random.randint(1,6))
print("Thank you for playing")
