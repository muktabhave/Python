import numpy as np
 
# First Array
arr1 = np.array([[4, 7], [2, 6]], 
                 dtype = np.float64)
                  
# Second Array
arr2 = np.array([[3, 6], [2, 8]], 
                 dtype = np.float64) 
 
# Addition of two Arrays
Sum = np.add(arr1, arr2)
print("Addition of Two Arrays: ")
print(Sum)

o/p:
Addition of Two Arrays: 
[[ 7. 13.]
 [ 4. 14.]]
 
# Addition of all Array elements
# using predefined sum method
Sum1 = np.sum(arr1)
print("\nAddition of Array elements: ")
print(Sum1)

o/p:
Addition of Array elements: 
19.0


# Square root of Array
Sqrt = np.sqrt(arr1)
print("\nSquare root of Array1 elements: ")
print(Sqrt)

o/p:
Square root of Array1 elements: 
[[2.         2.64575131]
 [1.41421356 2.44948974]]

# Transpose of Array
# using In-built function 'T'
Trans_arr = arr1.T
print("\nTranspose of Array: ")
print(Trans_arr)

o/p:

Transpose of Array: 
[[4. 2.]
 [7. 6.]]
