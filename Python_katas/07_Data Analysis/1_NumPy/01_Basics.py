import numpy as np

#Creating Arrays:
arr= np.array([1,2,3,4,5,6,7,8,9])
print(arr)

#Types of arrays
#1D Arrays:
Arr_1d = np.array([1,2,3,4,5,6,7,8,9])
print(Arr_1d)

#2D Array:
Arr_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(Arr_2d)

#Multidimensional Array
Arr_3d = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(Arr_3d)



#Methodes of filling arrays:
#fIlling hole array with zeros:
Arr_Zeros = np.zeros((3,3))
print(Arr_Zeros)

#fIlling hole array with one:
Arr_Ones = np.ones((3,3))
print(Arr_Ones)

#Filling with range:
Arr_Range = np.arange(1, 10, 2)
print(Arr_Range)

#Linespace:
linspace = np.linspace(0, 5, 5)
print(linspace)

#Identity Matrix:
Identity = np.identity(5)
print(Identity)
Identity= np.eye(5)
print(Identity)

# Attributes with arrays
a = np.array([[1, 2, 3],
              [4, 5, 6]])

# a.ndim
# Returns the number of dimensions of the array
# 1D -> 1, 2D -> 2, 3D -> 3
print(a.ndim)   # Output: 2

# a.shape
# Returns a tuple showing (rows, columns)
print(a.shape)  # Output: (2, 3)

# a.size
# Returns total number of elements in the array
print(a.size)   # Output: 6

# a.dtype
# Returns the data type of elements stored in the array
print(a.dtype)  # Output: int64

# a.astype(datatype
arr=np.array([1,2,3,4,5,6,7,8,9])
print(arr,arr.dtype)
Float_arr=arr.astype(np.float64)
print(Float_arr,Float_arr.dtype)



## Array Indexing & Slicing
#1D :
a = np.array([10, 20, 30, 40])
a[0]        # 10
a[1:3]      # [20 30]

#2D :
b = np.array([[1,2,3],[4,5,6]])
b[0, 1]     # 2