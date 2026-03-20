print("lists are comma separated values enclosed within Square brackets:")
student=['jhon','ram','Kritika','pritika']
print(student)
print(type(student))
print(type(student[0]))

print("Accesing lists elements:")
days=["Mon","Tue","Wed","Thur","Fri","Sat","Sun"]
print(days)
print(days[0])
print(days[2])
print(days[3])
print(days[-1])
print(days[:3]) #['Mon', 'Tue', 'Wed']
print(days[-3:]) #['Fri', 'Sat', 'Sun']

print("Operations on Lists:")

print('Slicing:')

nums=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(nums[0:21:1])
print(nums[3:18:3])
print(nums[0:21:3])
print(nums[0:21:2])

print("Concatination:")
l1=[1,2,3,4,5]
l2=[6,7,8,9,10]
print(f"{l1} + {l2}")
print(l1+l2)

print("Repetition:")
l1=[1,2,3,4,5]
print(l1*3)

print("Append vs Insert vs Extend:")
print("Append: Adds at the end")
fruits=["apple","banana","orange","mango"]
fruits.append("grape")
print(fruits)
fruits.append("banana")
print(fruits)

print("Insert: Adds at the specified index")
fruits.insert(2,"pineapple")
print(fruits)

print("Extend: Adds at the end but can add list")
l2=["jackfruit","Kivy"]
fruits.extend(l2)
print(fruits)


print("Remove vs Pop:")
print("Remove: can remove last element and specified value")
fruits.remove("apple")
print(fruits)

print("pop: can remove last element and specified value with index")
fruits.pop(3)
print(fruits)
fruits.pop(6)
print(fruits)

print("Reverse:")
l1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(l1)
l1.reverse()
print(l1)

days=["Mon","Tue","Wed","Thur","Fri","Sat","Sun"]
print(days)
days.reverse()
print(days)

print("Sort:")
l1=[16,15,11,12,13,14,9,8,7,6,5,1,2,3,4,17,18,19,20]
print(l1)
l1.sort()
print(l1)
l1.sort(reverse=True)
print(l1)

days=["Mon","Wed","Tue","Sat","Thur","Fri","Sun"]
print(days)
days.sort()
print(days)
days.sort(reverse=True)
print(days)

print("Count:")
numbers=[1,2,4,6,3,5,3,56,2,4,7,443,5553,44,56,7,544,3,4,5]
print(numbers.count(5))
print(numbers.index(6))


print("Membership Operator:")
lang=["Python","java","C++"]
print("Python" in lang)
print("java" not in lang)
print("PHP" in lang)

print("Numerical Operations:")
nums=[10,23.3,23,45,66,44.55,33,44.55]
print(f"Minimum: {min(nums)}\n Maximum: {max(nums)} \n Average: {sum(nums)/len(nums)} \n Addition: {sum(nums)}")

print("Nested Lists:")
list=[1,23,45,43,[344,554,334,33,[333,443,34],33,44]]
print(list)
print(list[1])
print(list[-1])
print(list[2:4])
print(list[-1][1])
print(list[-1][-3])
print(list[-1][-3][2])


