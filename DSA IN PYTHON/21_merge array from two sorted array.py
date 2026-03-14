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


arr1 = [22, 33, 44, 55]
arr2 = [33, 44, 66, 77]

print(merge_array(arr1, arr2))