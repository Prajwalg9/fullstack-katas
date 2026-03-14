class largest:
    
    def largest(self, arr):
        n=len(arr)
        large=arr[0]
        for i in range(1,n):
            large=max(large,arr[i])
        return large
        
nums=[11,232,32,35,3445,22,54]

large=largest()
print(large.largest(nums))