def isSorted(arr):
    for i in range(0,len(arr)-1):
        if arr[i]<=arr[i+1]:
            i+=1
        else:
            return False
    return True

print(isSorted([2, 11, 12, 12, 22, 22, 66, 111, 111, 334, 334]))


print(isSorted([2, 11, 12, 12, 22, 22, 66,55, 111, 111, 334, 334]))