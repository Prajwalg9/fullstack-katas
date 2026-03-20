# Get birth year from user (it will be a string)
birth_year_str = input("Enter your birth year: ")

# Convert the string to an integer
birth_year_int = int(birth_year_str)

# Now we can do math with it
current_year = 2025
age = current_year - birth_year_int

print("You are", age, "years old.")


# Other examples of type casting
x_str = "10.5"
y_str = "20"

# Convert string to float
x_float = float(x_str)

# Convert string to integer
y_int = int(y_str)

result = x_float + y_int

# Convert the numeric result back to a string to print it nicely
print("The result is: " + str(result))