n=int(input("Enter the number: "))
List= [i for i in range(1,n+1)]
result = []
for i in List:
    if n%i==0:
        result.append(i)
print(result)