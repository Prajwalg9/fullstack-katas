#tuples are sequence of immutable variables separated by comma enclosed within round brackets or no brackets:
t1=(223,34,32.33,"Hello World",True,[2,32,3],(77,88,44),'s')
print(t1)

print("\nAccesing elements of tuples")
print(t1[0])
print(t1[1])
print(t1[-1])
print(t1[-2])
print(t1[2:])
print(t1[:-1])
print(t1[-2][-1])

print("\nType casting:")
t1=1,3,23,544,3
print(t1)
l1=list(t1)
print(l1)
t2=tuple(l1)
print(t2)

print("\n Concatenation:")
t1=42,23,56,23
t2=23,34,23,23,23
print(t1)
print(t2)
print(t1+t2)

print("\n Repetation:")
t1='hello',True,'world'
print(t1*9)


print("\nMembership operations:")
student=1001,"ramsham",91.0
print("ram" in student)
print("ramsham" in student)
print(91.0 in student)

print("\nCounting elements:")
print(student.count(1001))

print("Index functions:")
t1=23,23,23,23,23,44,55,34,77,4456,755
print(t1.index(23))

print("\nMax vs Min vs Sum")
print(f"Max:{max(t1)} Min:{min(t1)} Sum:{sum(t1)}")
