#loops

# for loop
for i in range(5):
    print("Iteration:", i)

for char in "Hello":
    print("Character:", char)

# while loop
count = 0
while count < 5:
    print("Count:", count)
    count += 1

# break and continue
for i in range(10):
    if i == 5:
        break
    if i % 2 == 0:
        continue
    print("Odd number less than 5:", i)

# nested loops
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")

# loop with else
for i in range(3):
    print("Looping:", i)
else:
    print("Loop finished.")