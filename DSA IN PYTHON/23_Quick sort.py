def Qsort(arr,low,high):
     if low<high:
         p_index=partition(arr,low,high)
         Qsort(arr,low,p_index-1)
         Qsort(arr,p_index+1,high)

def partition(arr,low,high):
     i,j=low,high
     pivot=arr[low]
     while i<j:
         while arr[i]<=pivot and i<=high-1:
             i+=1
         while arr[j]>=pivot and j>=low+1:
             j-=1
         if i<j:
             arr[i],arr[j]=arr[j],arr[i]
     arr[j],arr[low]=arr[low],arr[j]
     return j
 
 
nums=[22,22,11,3,4,5,33,3,33,55,43,3,4,6777,5,343,3]
Qsort(nums,0,len(nums)-1)
print(nums)
