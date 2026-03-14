num=int(input("Enter the number: "))
n=num
List= [i for i in range(1,n+1)]
result= []
root=int(n**(0.5))

for i in range(1,root+1):
    if num%i==0:
        result.append(i)
        if num//i != i:
            result.append(num//i)
result.sort()
print(result)