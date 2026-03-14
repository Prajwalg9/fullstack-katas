n=int(input("Enter a number: "))
num=n
result=0

while num>0:
    last=num%10
    result = (result*10) + last
    num=num//10

print(result)