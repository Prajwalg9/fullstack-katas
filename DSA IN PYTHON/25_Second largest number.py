import math 

def Slargest(arr):
    largest=-math.inf
    Slargest=-math.inf
    for i in range(0,len(arr)-1):
        if arr[i]>largest:
            Slargest=largest
            largest=arr[i]
        elif arr[i]>Slargest and arr[i] != largest:
            Slargest=arr[i]
    return Slargest

List=[22,33,11,7,6,8,4,443,5,5]
print(Slargest(List))