# Integer datatype
# guessed by Numpy
x = np.array([1, 2]) 
print("Integer Datatype: ")
print(x.dtype)     	
 
o/p: INT64
 
# Float datatype
# guessed by Numpy
x = np.array([1.0, 2.0])
print("\nFloat Datatype: ")
print(x.dtype) 
 
o/p:float64
 
# Forced Datatype
x = np.array([1, 2], dtype = np.int64)  
print("\nForcing a Datatype: ")
print(x.dtype)
 
o/p INT64
