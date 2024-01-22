"""
Lists are mutable which means you can assign new element to the list.
"""

"""
len - it returns length of the list
"""

"""
slicing is grabbing some part of list.
new_list = old_list[start:stop:step]
"""

"""
indexing allows to access element from the list.
my_list = [10, 20, 30, 40, 50]
my_list[1]
"""

"""
concatenation allows to add two list using + symbol
"""

"""
append - adds new element at the end of list.
"""

"""
insert - insert takes two arguments index and object. It places object in specified index.
"""

"""
extend - extend appends each element of the iterable to the target object. Target object might be list, tuple 
or string. It returns none(in place method) object. It applies the change to the original object.
"""

"""
pop - pop removes the last element of the list or it can remove element by index value as well. 
By default, index value is –1, returns the deleted element.
"""

"""
remove - removes the element by value. If there are multiple elements it removes first occurrence.
"""

"""
sort - it sorts the elements of the list and its in-place method. In place methods dont return anything.
"""
import random
lst = [{"name": f"Name {random.randrange(1, 10)}", "age": random.randrange(20, 40)} for _ in range(10)]
lst.sort(key=lambda d: -d["age"])
print(lst)

"""
reverse - its reverse elements in the list. Its in-place method.
"""

"""
count - it counts the number of occurrences of the specific element in the list.
"""

"""
index - it takes the value and returns index of the element.
"""