n=int(input("Enter a number: "))
num=n
digits=0
total=0

while num>0:
    digits=digits+1
    num= num//10

num=n

while num>0:
    ld=num%10
    total= total + (ld**digits)
    num=num//10

print(f"Your num: {n} \nTotal is {total} ")
if total==n:
    print("Yes, the number is an amstrong number.")
else:
    print("No, the number is not an amstrong number.")