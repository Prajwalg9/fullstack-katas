def RRotate(nums,k):
    n=len(nums)
    k%=n
    nums[:]=nums[n-k:]+nums[:n-k]
    
list=[22,33,22,44,55,667,7,77]
print(list)
RRotate(list,3)
print(list)