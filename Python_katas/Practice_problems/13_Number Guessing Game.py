import random
print("welcome to the Number Guessing Game\n You have 10 chances to guess your number.")
while True:

    inp=input("Press enter to play a guessing game or q to quit: ")
    if inp=="q":
        break
    else:
        number=random.randint(1,100)
        chance=0;
        result=None
        while chance<10:
            user = int(input("Enter Number between 1 and 100: "))
            if number == user:
                result="correct!"
                print(result,'You Win')
                break
            elif number > user > 0:
                print("Incorrect! try Higher.")
            elif number < user < 100:
                print("Incorrect! try Lower.")
            else:
                print("Incorrect! Out of range.")
            chance=chance+1
        if result is None:
            print('Better Luck Next time! Try Again!')