def selection_sort(List):
    n = len(List)
    for i in range(0, n):
        min_index = i
        for j in range(i + 1, n):
            if List[min_index] > List[j]:
                min_index = j
        List[min_index], List[i] = List[i], List[min_index]

arr= [22,34,33,22,336,77,85,3,6,4,26,77,555,4]
print(arr)
selection_sort(arr)
print(arr)