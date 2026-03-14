import random

nums = [random.randint(1,100) for i in range(10)]
print(nums)

def reverse(array,left=0,right=None):
    if right==None:
        right = len(array)-1
    if left>=right:
        return
    array[left], array[right] = array[right], array[left]
    reverse(array,left+1,right-1)

reverse(nums)
print(nums)