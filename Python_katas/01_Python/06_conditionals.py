#Basic if
age = 18
print("Age is:", age)
if age >= 18:
    print("You are an adult.")

#If-Else
age = 16
print("Age is:", age)
if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult.")

#If-Elif-Else
marks = 85
print("Marks are:", marks)
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
else:
    print("Grade: C")


#Nested If
num = 10
print("Number is:", num)
if num > 0:
    print("Positive number")
    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")
else:
    print("Negative number")


#if shorthand=turnary operator
age = 20
print("Age is:", age)
print("You are an adult." if age >= 18 else "You are not an adult.")

