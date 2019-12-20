#set is datatype which allows you to store other immutable types. 
# There's no order for items stored in set so you cant access set items by index
# An item can be stored in a set only once. No duplicates allowed.p
>>> set()
set()
>>> {1}
{1}
>>> type({1})
<class 'set'>
>>> type({})
<class 'dict'>
>>> names={"Nina", "max", "Nina"}
>>> len(names)
2
>>> #proves sets cant take duplicates
... 
>>> hash("Nina")
-8675810051579874360
>>> #what happens if we take hash of a list
... 
>>> hash([])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
>>> {[]}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
>>> # cant hash immutable types
... 
>>> #how to deduplicate a list
... 
>>> names=["Nina", "Max", "Rose", "Nina"]
>>> set(names)
{'Nina', 'Rose', 'Max'}
>>> #things in set are not sorted, appear in ramdom manner
... 
>>> set1={1,2,"b", 6, "c", "e"}
>>> set1
{1, 2, 'e', 6, 'c', 'b'}
>>> 
>>> #we cant access an element from set with an index
... 
>>> set1[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'set' object is not subscriptable

>>> colors= {"red", "green", "yellow"}
>>> colors.add("pink")
>>> colors
{'green', 'yellow', 'pink', 'red'}
>>> 
>>> #remove from set
... 
>>> colors.discard("green")
>>> 
>>> colors
{'yellow', 'pink', 'red'}
>>> #with discard if we remove item from set which is not there in set; no error
... 
>>> colors.discard("p")
>>> colors
{'yellow', 'pink', 'red'}
>>> 
>>> #can also use remove to remove an element from set but gives err if we try to remove element which is not in set
... 
>>> colors.remove("red")
>>> colors
{'yellow', 'pink'}
>>> colors.remove("r")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'r'
>>> 
>>> #combine 2 sets
... 
>>> nos={1,2,3}
>>> 
>>> colors.update(nos)
>>> 
>>> colors
{1, 2, 3, 'pink', 'yellow'}
>>> 
>>> #if instead of another set we pass a string to the update method it will add individual element of string to the first set
... 
>>> colors.update("Nina")
>>> 
>>> colors
{1, 2, 3, 'N', 'n', 'pink', 'a', 'yellow', 'i'}

>>> #set operations
... 
>>> colors= {"red", "blue", "orange"}
>>> 
>>> "red" in colors
True
>>> "black" in colors
False
>>> 
>>> ranibow_colors= {"red", "green", "yellow", "blue"}
>>> 
>>> favorite={"purple", "magenta", "black"}
>>> 
>>> #assign new variable to point to set favorite
... 
>>> fav_colors= favorite
>>> 
>>> fav_colors
{'magenta', 'black', 'purple'}
>>> 
>>> #union of sets
>>> ranibow_colors | fav_colors
{'green', 'blue', 'purple', 'magenta', 'black', 'yellow', 'red'}
>>> 
>>> # union can also be done like this my_set.union(other_set)
... 
>>> #intersection
... 
>>> ranibow_colors& fav_colors
set()
>>> ranibow_colors & fav_colors
set()
>>> #returns common element; returned nothing as no common elements here
... 
>>> #Diffrence
... 
>>> ranibow_colors ^ fav_colors
{'blue', 'purple', 'magenta', 'yellow', 'green', 'black', 'red'}
>>> 