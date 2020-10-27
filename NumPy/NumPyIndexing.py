# Python program to demonstrate
# indexing in numpy array
import numpy as np
 
# Initial Array
arr = np.array([[-1, 2, 0, 4],
                [4, -0.5, 6, 0],
                [2.6, 0, 7, 8],
                [3, -7, 4, 2.0]])
print("Initial Array: ")
print(arr)

o/p:
Initial Array:
[[-1, 2, 0, 4],
 [4, -0.5, 6, 0],
 [2.6, 0, 7, 8],
 [3, -7, 4, 2.0]]
 
# Printing a range of Array
# with the use of slicing method

sliced_arr = arr[:2, ::2]
print ("Array with first 2 rows and"
    " alternate columns(0 and 2):\n", sliced_arr)

o/p:
Array with first 2 rows and alternate columns(0 and 2):
[[-1, 2],
 [4, -0.5]]

# Printing elements at
# specific Indices
Index_arr = arr[[1, 1, 0, 3], 
                [3, 2, 1, 0]]
print ("\nElements at indices (1, 3), "
    "(1, 2), (0, 1), (3, 0):\n", Index_arr)

o/p:
Elements at indices (1, 3), (1, 2), (0, 1), (3, 0):
 [ 0. 54.  2.  3.]
