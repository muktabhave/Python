# Python program to demonstrate basic array characteristics

import numpy as np
 
# Creating array object
arr = np.array( [[ 1, 2, 3],
                 [ 4, 2, 5]] )
 

# Printing type of arr object
print("Array is of type: ", type(arr))
 
Array is of type:  <class 'numpy.ndarray'>

# Printing array dimensions (axes)
print("No. of dimensions: ", arr.ndim)
 
No. of dimensions:  2

# Printing shape of array
print("Shape of array: ", arr.shape)
 
Shape of array:  (2, 3)

# Printing size (total number of elements) of array
print("Size of array: ", arr.size)
 
Size of array:  6

# Printing type of elements in array
print("Array stores elements of type: ", arr.dtype)

Output :

Array stores elements of type:  int64



Array Creation

There are various ways to create arrays in NumPy.

For example, you can create an array from a regular Python list or tuple using the array function. The type of the resulting array is deduced from the type of the elements in the sequences.
Often, the elements of an array are originally unknown, but its size is known. Hence, NumPy offers several functions to create arrays with initial placeholder content. These minimize the necessity of growing arrays, an expensive operation.
For example: np.zeros, np.ones, np.full, np.empty, etc.
To create sequences of numbers, NumPy provides a function analogous to range that returns arrays instead of lists.
arange: returns evenly spaced values within a given interval. step size is specified.
linspace: returns evenly spaced values within a given interval. num no. of elements are returned.
Reshaping array: We can use reshape method to reshape an array. Consider an array with shape (a1, a2, a3, …, aN). We can reshape and convert it into another array with shape (b1, b2, b3, …, bM). The only required condition is:
a1 x a2 x a3 … x aN = b1 x b2 x b3 … x bM . (i.e original size of array remains unchanged.)
Flatten array: We can use flatten method to get a copy of array collapsed into one dimension. It accepts order argument. Default value is ‘C’ (for row-major order). Use ‘F’ for column major order.
Note: Type of array can be explicitly defined while creating array.

# Python program to demonstrate array creation techniques

import numpy as np
 
# Creating array from list with type float
a = np.array([[1, 2, 4], [5, 8, 7]], dtype = 'float')
print ("Array created using passed list:\n", a)
 
Array created using passed list:
 [[ 1.  2.  4.]
 [ 5.  8.  7.]] 
 
# Creating array from tuple
b = np.array((1 , 3, 2))
print ("\nArray created using passed tuple:\n", b)
 
 Array created using passed tuple:
 [1 3 2]
 
# Creating a 3X4 array with all zeros
c = np.zeros((3, 4))
print ("\nAn array initialized with all zeros:\n", c)


An array initialized with all zeros:
 [[ 0.  0.  0.  0.]
 [ 0.  0.  0.  0.]
 [ 0.  0.  0.  0.]]

# Create a constant value array of complex type
d = np.full((3, 3), 6, dtype = 'complex')
print ("\nAn array initialized with all 6s."
            "Array type is complex:\n", d)
Output :

An array initialized with all 6s. Array type is complex:
 [[ 6.+0.j  6.+0.j  6.+0.j]
 [ 6.+0.j  6.+0.j  6.+0.j]
 [ 6.+0.j  6.+0.j  6.+0.j]]



Array Indexing

Knowing the basics of array indexing is important for analysing and manipulating the array object. NumPy offers many ways to do array indexing.

Slicing: Just like lists in python, NumPy arrays can be sliced. As arrays can be multidimensional, you need to specify a slice for each dimension of the array.
Integer array indexing: In this method, lists are passed for indexing for each dimension. One to one mapping of corresponding elements is done to construct a new arbitrary array.
Boolean array indexing: This method is used when we want to pick elements from array which satisfy some condition.
# Python program to demonstrate
# indexing in numpy
import numpy as np
 
# An exemplar array
arr = np.array([[-1, 2, 0, 4],
                [4, -0.5, 6, 0],
                [2.6, 0, 7, 8],
                [3, -7, 4, 2.0]])

# Slicing array
temp = arr[:2, ::2]
print ("Array with first 2 rows and alternate"
                    "columns(0 and 2):\n", temp)
 
 
Array with first 2 rows and alternatecolumns(0 and 2):
 [[-1.  0.]
 [ 4.  6.]]
 
 
# Integer array indexing example
temp = arr[[0, 1, 2, 3], [3, 2, 1, 0]]
print ("\nElements at indices (0, 3), (1, 2), (2, 1),"
                                    "(3, 0):\n", temp)

Elements at indices (0, 3), (1, 2), (2, 1),(3, 0):
 [ 4.  6.  0.  3.]


# boolean array indexing example
cond = arr > 0 # cond is a boolean array
temp = arr[cond]
print ("\nElements greater than 0:\n", temp)

Output :

Elements greater than 0:
 [ 2.   4.   4.   6.   2.6  7.   8.   3.   4.   2. ]
 
 
Basic operations
Plethora of built-in arithmetic functions are provided in NumPy.

Operations on single array: We can use overloaded arithmetic operators to do element-wise operation on array to create a new array. In case of +=, -=, *= operators, the exsisting array is modified.

# Python program to demonstrate basic operations on single array

import numpy as np
 
a = np.array([1, 2, 5, 3])
 
# add 1 to every element
print ("Adding 1 to every element:", a+1)

Adding 1 to every element: [2 3 6 4]

# subtract 3 from each element
print ("Subtracting 3 from each element:", a-3)
 
Subtracting 3 from each element: [-2 -1  2  0] 
 
# multiply each element by 10
print ("Multiplying each element by 10:", a*10)
 
Multiplying each element by 10: [10 20 50 30] 
 
# square each element
print ("Squaring each element:", a**2)
 
Squaring each element: [ 1  4 25  9] 
 
# modify existing array
a *= 2
print ("Doubled each element of original array:", a)
 
Doubled each element of original array: [ 2  4 10  6]
 
# transpose of array
a = np.array([[1, 2, 3], [3, 4, 5], [9, 6, 0]])
 
print ("\nOriginal array:\n", a)
print ("Transpose of array:\n", a.T)

Output :

Original array:
 [[1 2 3]
 [3 4 5]
 [9 6 0]]
Transpose of array:
 [[1 3 9]
 [2 4 6]
 [3 5 0]]
 
Unary operators: Many unary operations are provided as a method of ndarray class. This includes sum, min, max, etc. These functions can also be applied row-wise or column-wise by setting an axis parameter.
# Python program to demonstrate unary operators in numpy
import numpy as np
 
arr = np.array([[1, 5, 6],
                [4, 7, 2],
                [3, 1, 9]])
 
# maximum element of array
print ("Largest element is:", arr.max())

Largest element is: 9

print ("Row-wise maximum elements:",
                    arr.max(axis = 1))

Row-wise maximum elements: [6 7 9]
 
# minimum element of array
print ("Column-wise minimum elements:",
                        arr.min(axis = 0))
 
Column-wise minimum elements: [1 1 2]

# sum of array elements
print ("Sum of all array elements:",
                            arr.sum())

Sum of all array elements: 38 
 
# cumulative sum along each row
print ("Cumulative sum along each row:\n",
                        arr.cumsum(axis = 1))

Output :

Cumulative sum along each row:
[[ 1  6 12]
 [ 4 11 13]
 [ 3  4 13]]


Binary operators: These operations apply on array elementwise and a new array is created. You can use all basic arithmetic operators like +, -, /, , etc. In case of +=, -=, = operators, the exsisting array is modified.
# Python program to demonstrate
# binary operators in Numpy
import numpy as np
 
a = np.array([[1, 2],
            [3, 4]])
b = np.array([[4, 3],
            [2, 1]])
 
# add arrays
print ("Array sum:\n", a + b)

Array sum:
[[5 5]
 [5 5]]
 
# multiply arrays (elementwise multiplication)
print ("Array multiplication:\n", a*b)

Array multiplication:
[[4 6]
 [6 4]]
 
# matrix multiplication
print ("Matrix multiplication:\n", a.dot(b))
Output:

Matrix multiplication:
[[ 8  5]
 [20 13]]
 
Universal functions (ufunc): NumPy provides familiar mathematical functions such as sin, cos, exp, etc. These functions also operate elementwise on an array, producing an array as output.
Note: All the operations we did above using overloaded operators can be done using ufuncs like np.add, np.subtract, np.multiply, np.divide, np.sum, etc.

# Python program to demonstrate universal functions in numpy
import numpy as np
 
# create an array of sine values
a = np.array([0, np.pi/2, np.pi])
print ("Sine values of array elements:", np.sin(a))
 
# exponential values
a = np.array([0, 1, 2, 3])
print ("Exponent of array elements:", np.exp(a))
 
# square root of array values
print ("Square root of array elements:", np.sqrt(a))
Run on IDE
Output:

Sine values of array elements: [  0.00000000e+00   1.00000000e+00   1.22464680e-16]
Exponent of array elements: [  1.           2.71828183   7.3890561   20.08553692]
Square root of array elements: [ 0.          1.          1.41421356  1.73205081]
