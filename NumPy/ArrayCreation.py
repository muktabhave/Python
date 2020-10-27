arr = [1, 2, 3, 4, 5]
arr1 = ["geeks", "for", "geeks"]
# Python program to create an array
 
1) Creating an array using list
    arr=[1, 2, 3, 4, 5]
    for i in arr:
        print(i)

Output:

1
2
3
4
5
 
2) Array creation using array functions :
array(data type, value list) function is used to create an array with data type and value list specified in its arguments.


# Python code to demonstrate the working of array()

import array
  
# initializing array with array values
# initializes array with signed integers
arr = array.array('i', [1, 2, 3]) 
 
# printing original array

print ("The new created array is : )
for i in range (0,3):
    print (arr[i], end=" ")
 

Output:

The new created array is : 1 2 3 1 5
 
3) Array creation using numpy methods :
NumPy offers several functions to create arrays with initial placeholder content. These minimize the necessity of growing arrays, an expensive operation. 
For example: np.zeros,np.empty etc.

numpy.empty(shape, dtype = float, order = ‘C’) : Return a new array of given shape and type, with random values.

# Python Programming illustrating numpy.empty method
 
import numpy as np
 
b = np.empty(2, dtype = int)
print("Matrix b : \n", b)

Output :

Matrix b : 
 [         0 1079574528]
 
 
a = np.empty([2, 2], dtype = int)
print("\nMatrix a : \n", a)

Matrix a : 
 [[0 0]
 [0 0]]


c = np.empty([3, 3])
print("\nMatrix c : \n", c)

Matrix a : 
 [[ 0.  0.  0.]
 [ 0.  0.  0.]
 [ 0.  0.  0.]]
 
 
numpy.zeros(shape, dtype = None, order = ‘C’) : Return a new array of given shape and type, with zeros.

# Python Program illustrating numpy.zeros method
 
import numpy as np
 
b = np.zeros(2, dtype = int)
print("Matrix b : \n", b)
 
a = np.zeros([2, 2], dtype = int)
print("\nMatrix a : \n", a)
 
c = np.zeros([3, 3])
print("\nMatrix c : \n", c)
Run on IDE
Output :

Matrix b : 
 [0 0]

Matrix a : 
 [[0 0]
 [0 0]]

Matrix c : 
 [[ 0.  0.  0.]
 [ 0.  0.  0.]
 [ 0.  0.  0.]]
 
Reshaping array: We can use reshape method to reshape an array. Consider an array with shape (a1, a2, a3, …, aN). We can reshape and convert it into another array with shape (b1, b2, b3, …, bM).
The only required condition is: a1 x a2 x a3 … x aN = b1 x b2 x b3 … x bM . (i.e original size of array remains unchanged.)

numpy.reshape(array, shape, order = ‘C’) : Shapes an array without changing data of array.

# Python Program illustrating numpy.reshape() method
 
import numpy as geek
 
array = geek.arange(8)
print("Original array : \n", array)

Output :

Original array : 
 [0 1 2 3 4 5 6 7]
 
# shape array with 2 rows and 4 columns
array = geek.arange(8).reshape(2, 4)
print("\narray reshaped with 2 rows and 4 columns : \n", array)

Output :

array reshaped with 2 rows and 4 columns : 
 [[0 1 2 3]
 [4 5 6 7]]

 
# shape array with 2 rows and 4 columns
array = geek.arange(8).reshape(4 ,2)
print("\narray reshaped with 2 rows and 4 columns : \n", array)

Output :
array reshaped with 2 rows and 4 columns : 
 [[0 1]
 [2 3]
 [4 5]
 [6 7]]

# Constructs 3D array
array = geek.arange(8).reshape(2, 2, 2)
print("\nOriginal array reshaped to 3D : \n", array)

Output :
Original array reshaped to 3D : 
 [[[0 1]
  [2 3]]

 [[4 5]
  [6 7]]]
  

arange([start,] stop[, step,][, dtype]) : Returns an array with evenly spaced elements as per the interval. The interval mentioned is half opened i.e. [Start, Stop)

# Python Programming illustrating numpy.arange method
 
import numpy as np
 
print("A\n", np.arange(4).reshape(2, 2), "\n")

Output :

A
 [[0 1]
 [2 3]]

 
print("A\n", np.arange(4, 10), "\n")

A
 [4 5 6 7 8 9]

 
print("A\n", np.arange(4, 20, 3), "\n")

A
 [ 4  7 10 13 16 19]

numpy.linspace(start, stop, num = 50, endpoint = True, retstep = False, dtype = None) : Returns number spaces evenly w.r.t interval. Similiar to arange but 
instead of step it uses sample number.

# Python Programming illustrating numpy.linspace method
 
import numpy as np
 
# restep set to True
print("B\n", np.linspace(2.0, 3.0, num=5, retstep=True), "\n")

Output :

B
 (array([ 2.  ,  2.25,  2.5 ,  2.75,  3.  ]), 0.25)
 
# To evaluate sin() in long range 
x = np.linspace(0, 2, 10)
print("A\n", geek.sin(x))

A
 [ 0.          0.22039774  0.42995636  0.6183698   0.77637192  0.8961922
  0.9719379   0.99988386  0.9786557   0.90929743]
 
Flatten array: We can use flatten method to get a copy of array collapsed into one dimension. It accepts order argument. Default value is ‘C’ (for row-major order). Use ‘F’ for column major order.

numpy.ndarray.flatten(order = ‘C’) : Return a copy of the array collapsed into one dimension.

# Python Program illustrating numpy.flatten() method
 
import numpy as np
 
array = np.array([[1, 2], [3, 4]])
 
# using flatten method
array.flatten()
print(array)

Output :

[1, 2, 3, 4]

#using fatten method 
array.flatten('F')
print(array)

[1, 3, 2, 4]
