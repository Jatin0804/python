import numpy as np

#create a 1-D numpy array
arr1d = np.array([1,2,3,4,5])

print("Arr1d is : ",arr1d)
print("Type of arr1d : ",type(arr1d))
print("Shape of arr1d : ",np.shape(arr1d))

#craeet a 2-D array
arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])

print("\narr2d is : \n",arr2d)
print("arr2d shape : ",arr2d.shape)

print("Data [1][2] : ",arr2d[1][2])

a=np.array([1,2,3,4,5])
b=np.array([6,7,8,9,10])

print("\na : ",a)
print("b : ",b)
radd = a+b
print("Resultant add a+b : ",radd)
rsqrt = np.sqrt(a)
print("\nSqrt of a : ",rsqrt)

print("\narr2d + 2 : \n",arr2d+2)

arr3d = np.array([[[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]],[[19,20,21],[22,23,24],[25,26,27]]])
print("\n arr3d : \n",arr3d)

zero_1d = np.zeros(5)
print("\nZero_1d : ",zero_1d)

zero_2d = np.zeros((3,4),dtype=int)
print("\nZero_2d : \n", zero_2d)

range_1d = np.arange(10)
print("\nrange_1d : ", range_1d)

# arr3d = np.array([[[1,2,3],[4,5,6],[7,8,9]]*3])
# print("\n",arr3d)