#numpy:-NumPy is a fundamental library for scientific computing in Python.
# It provides support for arrays and matrices, along with a collection of mathematical functions to operate on these data structures.
# In this lesson, we will cover the basics of NumPy, focusing on arrays and vectorized operations.

import numpy as np
arr1=np.array([1,2,3,4,5])
print(arr1)
print(type(arr1))
print(arr1.shape)

arr2=np.array([1,2,3,4,5])
arr2.reshape(1,5) #1row and 5 columns
print(arr2)

arr2=np.array([[1,2,3,4,5]])
arr2.shape
print(arr2.shape)

#2d array
import numpy as np
arr2=np.array([[1,2,3,4,5],[2,3,4,5,6]])
print(arr2)
print(arr2.shape)

arr3=np.arange(0,10,2).reshape(5,1)
print(arr3)

#create arrays
arr4=np.ones((3,4))
print(arr4)

#identity matrix
arr5=np.eye(3)
print(arr5)

import numpy as np

arr = np.array([[1, 2, 3],[4, 5, 6]])
#attributes of numpy array
print("Array:\n", arr)
print("Shape:", arr.shape)          # Output: (2, 3)
print("Number of dimensions:", arr.ndim)   # Output: 2
print("Size (number of elements):", arr.size)  # Output: 6
print("Data type:", arr.dtype)      # Output: int64 (may vary based on platform)
print("Item size (in bytes):", arr.itemsize)  # Output: 8 (may vary based on platform)

#numpy vactorized operation
arr1=np.array([1,2,3,4,5])
arr2=np.array([10,20,30,40,50])

#element wise addition
print("addition:",arr1+arr2)

#element wise substraction
print("substaction:",arr1-arr2)

#element wise multiplication
print("multiplication:",arr1*arr2)

#element wise division
print("division:",arr1/arr2)

#universal function
import numpy as np
arr=np.array([2,3,4,5,6])
#square root
print(np.sqrt(arr))

#exponential
print(np.exp(arr))

#sine
print(np.sin(arr))

#natural log
print(np.log(arr))

 #array slicing and indexing
arr7=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print("array:\n",arr7)

print(arr7[1][1])
print(arr7[1:])
print(arr7[1:,2:])
print(arr7[0:2,2:])

arr7=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print("array:\n",arr7)

print(arr7[1:,1:3])

#modify array element
arr7[0,0]=100
print(arr7)

arr7[1:]=100
print(arr7)

#statistical concepts--normalization
#to have a mean of 0 and standard deviation of 1
data=np.array([1,2,3,4,5])

#calculate the mean and standard deviation
mean = np.mean(data)
std_dev=np.std(data)

#normalization of data
normalized_data=(data-mean)/std_dev
print("normalized data:",normalized_data)
###
data=np.array([1,2,3,4,5,6,7,8,9,10])
#mean
mean=np.mean(data)
print("mean:",mean)

#median
median=np.median(data)
print("median:",median)

#standard deviation
std_dev=np.std(data)
print("standard deviation:",std_dev)

#variance
variance=np.var(data)
print("variance:",variance)

#logical data
import numpy as np

data=np.array([1,2,3,4,5,6,7,8,9])
Data=data[(data>=5)&(data<=8)]
print(Data)




