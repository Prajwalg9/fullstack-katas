def MoveZerosEnd(arr):
    i,j=0,1
    n=len(arr)
    while j<n:
        if arr[i]!=0:
            i+=1
            j+=1
        else:
            if arr[j]!=0:
                arr[i],arr[j]=arr[j],arr[i]
                i+=1
            j+=1
            
List=[0,0,1,0,1,2,0,32,0,2,34,00,0,0,45,0,433,5]
print(List)
MoveZerosEnd(List)
print(List)
                