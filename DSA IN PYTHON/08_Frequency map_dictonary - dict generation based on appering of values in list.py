from random import randint

nums = [randint(1,20) for i in range(1,31)]
print(nums)
frequency_map={}

#goal is to count number of occurrence of each number in given list and store it in dict={ num : no. of occurences }

for i in range(0,len(nums)):
    if nums[i] not in frequency_map:
        frequency_map[nums[i]]=1
    else:
        frequency_map[nums[i]]+=1

print(frequency_map)