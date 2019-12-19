>>> []
[]
>>> list()
[]
>>> type([])
<class 'list'>
>>> names= ["Nina", "Mona", "Ruby"]
>>> type(names)
<class 'list'>

>>> print(names)
['Nina', 'Mona', 'Ruby']
>>> len(names)
3
>>> names[0]
'Nina'
>>> names[1]
'Mona'
>>> names[2]
'Ruby'

#if we try to acccess element which is not present it gives error
>>> names[3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range

#can update a list item like this
>>> names[1]= "jimmy"
>>> names
['Nina', 'jimmy', 'Ruby']

#can also define a list in parts like this
>>> names=[
... "nina",
... "jimmy",
... "ruby",
... ]
>>> names
['nina', 'jimmy', 'ruby']

#sort a list
>>> lottery_number= [10, 1500, 23000, 4300]
>>> sorted(lottery_number)
[10, 1500, 4300, 23000]

#original list remains like that
>>> lottery_number
[10, 1500, 23000, 4300]

#sort desc
>>> sorted(lottery_number, reverse= True)
[23000, 4300, 1500, 10]

#original list remains same
>>> lottery_number
[10, 1500, 23000, 4300]

#sort list in place, this changes the underlying list

>>> lottery_number
[10, 1500, 23000, 4300]
>>> lottery_number.sort()
>>> lottery_number
[10, 1500, 4300, 23000]

# desc sort

>>> lottery_number.reverse()
>>> lottery_number
[23000, 4300, 1500, 10]

#Add element to the list
>>> names= ["jimmy", "Ruby", "Mukta"]
>>> names.append("radha")
>>> names
['jimmy', 'Ruby', 'Mukta', 'radha']

#insert at perticular position in list

>>> names.insert(0, "rose")
>>> names
['rose', 'jimmy', 'Ruby', 'Mukta', 'radha']

#join 2 lists
>>> colors= ["Blue", "velvet"]
>>> names.extend(colors)
>>> names
['rose', 'jimmy', 'Ruby', 'Mukta', 'radha', 'Blue', 'velvet']

#is element in list?

>>> names=["Nina", "james", "Ruby", "Nina"]
>>> "rose" in names
False
>>> "Nina" in names
True

#find index position of item in list
>>> names.index("james")
1
>>> names.index("Nina")
0

#find count of item in list
>>> names.count("Nina")
2

# can change element at particular position in list like this

>>> pos=names.index("james")
>>> names[pos]= "Rosy"
>>> names
['Nina', 'Rosy', 'Ruby', 'Nina']

#remove item from list

>>> names= ["Nina", "Max"]
>>> names.remove("Max")
>>> names
['Nina']

#Removes only first item
>>> names= ["Nina", "Max", "Nina"]
>>> names.remove("Nina")
>>> names
['Max', 'Nina']

#pop to remove item
>>> names= ["Nina", "Max", "Joey", "Ross"]
>>> names.pop(1)
'Max'
>>> names
['Nina', 'Joey', 'Ross']
>>> names.pop(2)
'Ross'
>>> names
['Nina', 'Joey']

#when we try to pop element which is not present in list
>>> names.pop(2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: pop index out of range

