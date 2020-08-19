>>> type(True)
<class 'bool'>
>>> type(False)
<class 'bool'>
>>> 
>>> bool(0)
False
>>> bool(1)
True
>>> bool(-1)
True
>>> 
>>> #All numbers return true except 0
... 
>>> bool([])
False
>>> bool(())
False
>>> bool(set())
False
>>> bool({})
False
>>> 
>>> # Empty list, tuples, set, dictionary return false
... 
>>> #but all of these with any data in it return true
... 
>>> bool("")
False
>>> bool(" ")
True
>>> # string with no chars false but with 1 or more char true
... 
>>> #number comparisions
... 
>>> 3<4
True
>>> 9>2
True
>>> #strings are compared based on ASCII values
... 
>>> #capital letters have lower ASCII than small letters
... 
>>> "t"< "T"
False
>>> "cat"== "bat"
False
>>> "abc"== "abc"
True
>>> 
>>> 

>>> [1,2,3]== [0,2,3]
False
>>> [1,2,3]== [1,2,3]
True
>>> a= [1,2,3]
>>> b=[1,2,3]
>>> 
>>> a==b
True
>>> a!=b
False
>>> 
>>> 
>>> #Equality ==, !=
... 
>>> #Identity is keyword
... 
>>> a is b
False
>>> #we get false because they are not stored at same memory location
... 
>>> a==b
True
>>> #values are equal
... 
>>> a= None
>>> a is None
True
>>> a is not None
False
>>> 
>>> 
>>> 
>>> ## And or and not operators
... 
>>> 
>>> #And operator--> if a is true returns b else returns a
... 
>>> a=True 
>>> b=True
>>> a and b
True
>>> b=False
>>> a and b
False
>>> a=False
>>> a and b
False
>>> [] and {}
[]
>>> [] and {1}
[]
>>> # or operator
... 
>>> a=False
>>> b=True
>>> a or b
True
>>> b=False
>>> a or b
False
>>> not False
True
>>> not True
False
>>> bool(1)
True
>>> not 1
False
>>> bool(0)
False
>>> not 0
True
>>> # if we and 2 true values it will return second value
... 
>>> #if we or 2 true values it will return first
