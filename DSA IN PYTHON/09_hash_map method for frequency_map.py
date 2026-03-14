from random import randint

nums = [randint(1,20) for i in range(1,31)]
print(nums)
hashmap = dict()

for i in range(0,len(nums)):
    hashmap[nums[i]] = hashmap.get(nums[i],0) + 1

print(hashmap)