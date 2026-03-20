#Sets: Non sequential collection of unique mutable items enclosed within {}

s1={22,23,'hello',88,8.99}
print(s1) #{22, 23, 8.99, 88, 'hello'}
print(len(s1))

print("\nMembership Operator:")
nums={1,2,3}
print(nums)
print(0 in nums)
print(1 in nums)
print(2 not in nums)

#Concatination repetation and indexing is not allowed

print("\nAdd and Remove and Discard:")
print("\nAdd:")
s1={1,2,3,4,5,6,7,8,9}
print(s1)
s1.add(10)
print(s1)

print("\nRemove and Discard:")#remove gives error if not found so we use discard
s1={1,2,3,4,5,6,7,8,9}
print(s1)

s1.remove(7)
print(s1)

s1.discard(6)
print(s1)

print("Intersection:")
lang={'Eng','marathi','hindi'}
lang2={'japaneese','hindi','Eng'}
print(lang)
print(lang2)
print("Common elements:")
print(lang.intersection(lang2))
print(lang & lang2)

print("\nUnion:")
lang={'Eng','marathi','hindi'}
lang2={'japaneese','hindi','Eng'}
print(lang)
print(lang2)
print(lang.union(lang2))
print(lang | lang2)

print("\nDifference of Sets:")
lang={'mon','tue','wed','thu','fri','sat','sun'}
lang2={'sat','sun'}
print(lang)
print(lang2)
print(lang.difference(lang2))
print(lang - lang2)

print("Frozen sets: in some cases we need sets which are immutable")
frozen_set=frozenset({'a','b','c','d'})
print(frozen_set)
print(type(frozen_set))
print("here we can not use add remove or discard functions")