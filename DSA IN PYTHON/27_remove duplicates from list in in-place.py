nums=[1,1,1,2,3,2,32,3,3,22,2,2,112,8,3,44,55,5,4,4,33,4,4,44,4,4]
def Remove_Dup(arr):
    i=0
    j=1
    for a in range(0,len(arr)-1):
        if nums[i]==nums[j]:
            j+=1
        else:
            i+=1
            nums[i],nums[j]=nums[j],nums[i]
            
print(nums)            
Remove_Dup(nums)
print(nums)
