def fun():
  print ("Hello")

fun()

def fun1():
  return 42

fun1()

x=fun()
x

y=fun1()

>>> def add_numbers(c,d):
...     return c+d
... 
>>> add_numbers(5,6)
11

>>> def greeting(name):
...     greet= "hello"
...     return greet+" "+name
... 
>>> greeting("Mukta")
'hello Mukta'

#A function which returns nothing. A null is called None or Nonetype in python
>>> def fun2():
...     return
... 
>>> x= fun2()
>>> type(x)
<class 'NoneType'>
>>> #Function arguments
... 
>>> add_numbers(3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: add_numbers() missing 1 required positional argument: 'd'

#Default arguments
#default argument should always be last parameter of the function

>>> def greeting(greeting, name):
...     greeting= "Hello"
...     name= "Mukta"
...     return f"{greeting}, {name}"
... 
>>> def greeting(greeting, name):
...     return f"{greeting}, {name}"
... 
>>> greeting("Hello", "Mukta")
'Hello, Mukta'
>>> def greeting(name, greeting="Hello"):
...     return f"{greeting}, {name}"
... 
>>> greeting("Mukta")
'Hello, Mukta'
>>> greeting("Mukta", "Namaste")
'Namaste, Mukta'
#if we put default argument at first place we get syntax error
>>> def create_query(language="javascript", num_stars= 50, sort="desc"):
...     return(f"{language} {num_stars} {sort}")
... 
>>> create_query()
'javascript 50 desc'
>>> create_query(language="python")
'python 50 desc'
>>> create_query(language="python", num_stars=30, sort="asc")
'python 30 asc'

>>> def fun_test (a, b=6):
...     return a+b
... 
>>> fun_test(3)
9
>>> fun_test(a=3)
9
>>> fun_test(5, b=9)
14
>>> fun_test(a=2, b=11)
13

#Below proves value of default parameter is not created and initiated each time function is called; 
# its initiated only once for the first call and stores that value for subsequent calls 
>>> def fun_test(a, b=[]):
...     b.append(a)
...     return b
... 
>>> fun_test(3)
[3]
>>> fun_test(5)
[3, 5]

# we can correct above code like this

>>> def fun_test(a, b= None):
...     if b is None:
...             b=[]
...     b.append(a)
...     print b

#function scope

>>> def twitter_acc():
...     account= "Mukta"
...     return (f"The account belongs to {account}")
... 
>>> twitter_acc()
'The account belongs to Mukta'
>>> account
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'account' is not defined

#gave error because account variable is defined inside function and has no existance outside function
>>> name="Ninja"

>>> def test_name():
...     name= "Mukta"
...     return name
... 
>>> test_name()
'Mukta'
>>> name
'Ninja'

#See above how value of variable name changes if we access it inside the function or outside the function

#practice scope

>>> def calculate(a,b, action="add"):
...     if action=="add":
...             return a+b
...     elif action=="subtract":
...             return a-b
... 
>>> calculate(5,6)
11
>>> calculate(5,6, "subtract")
-1
