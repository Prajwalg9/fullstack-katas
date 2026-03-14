def merge_array(arr1, arr2):
    result = []
    i, j = 0, 0
    n, m = len(arr1), len(arr2)

    while i < n and j < m:
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    result.extend(arr1[i:])
    result.extend(arr2[j:])

    return result



def merge_sort(arr):
    if len(arr) <= 1:
       return arr
    mid= len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    return merge_array(left_half,right_half)


arr= [22,34,33,22,336,77,85,3,6,4,26,77,555,4]
print(merge_sort(arr))