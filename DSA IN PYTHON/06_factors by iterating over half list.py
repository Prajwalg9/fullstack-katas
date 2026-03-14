num=int(input("Enter the number: "))
n=num
List= [i for i in range(1,n+1)]
result= []

for i in range(1,n//2):
    if n%i==0:
        result.append(i)

result.append(n)
print(result)