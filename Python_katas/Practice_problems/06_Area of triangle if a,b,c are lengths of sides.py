#area of triangle = sqrt(s * (s - a) * (s - b) * (s - c))

#where, s=semiperimeter=(a+b+c)/2

print("lets calculate area of triangle using sides a,b,c\n")
a=int(input("enter side a:"))
b=int(input("enter side b:"))
c=int(input("enter side c:"))

semiperimeter=(a+b+c)/2
area=(semiperimeter*(semiperimeter-a)*(semiperimeter-b)*(semiperimeter-c))**(1/2)

print(f"area of triangle having sides a:{a}, b:{b} and c:{c} is: {area}")