>>> a=()
>>> type(a)
<class 'tuple'>

#Tuple is not just item but item and , defines a tuple with 1 element
>>> b=(1)
>>> type(b)
<class 'int'>
>>> b=(1,)
>>> type(b)
<class 'tuple'>

>>> c=(1,2,3,4,"roni")
>>> c[1]
2
>>> c[3]
4

#Tuple is immutable object i.e. we cant change its items hence extend, pop etc dont work
>>> c[0]= "raj"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment

#unpacking tuples

>>> student= (10, "Rosy", 20, "Maths")
>>> id,name,age,subject= student
>>> id
10
>>> name
'Rosy'
>>> age
20
>>> subject
'Maths'

#if we give worng no of arguments while unpacking it throws error

>>> id, name,age=student
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: too many values to unpack (expected 3)


#give _ for missing value
... 
>>> id,name,age,_=student
>>> id
10
>>> name
'Rosy'
>>> age
20

>>> x= 1,2,3
>>> type(x)
<class 'tuple'>

>>> def status_code():
...     return 20, "ok"
... 
>>> x= status_code()
>>> type(x)
<class 'tuple'>


>>> code,name= status_code()
>>> code
20
>>> name
'ok'