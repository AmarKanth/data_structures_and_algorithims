"""
Repeat all the elements of a NumPy array of strings
"""
import numpy as np

np1 = np.array(['Akash', 'Rohit', 'Ayush'], dtype = str)
res = np.char.multiply(np1, 2)
print(res)


"""
How to split the element of a given NumPy array with spaces?
"""
import numpy as np

np1 = np.array(['PHP C# Python C Java C++'], dtype=str)
res = np.char.split(np1)
print(res[0])


"""
How to insert a space between characters 
of all the elements of a given NumPy array?
"""
import numpy as np  
  
np1 = np.array(["geeks", "for", "geeks"])
res = np.char.join(" ", np1)
print(res)


"""
Find the length of each string element in the Numpy array
"""
import numpy as np

np1 = np.array(['New York', 'Lisbon', 'Beijing', 'Quebec'])
length_checker = np.vectorize(len)  
res = length_checker(np1)
print(res)


"""
Swap the case of an array of string
"""
import numpy as np

np1 = np.array(['P4Q R', '4q Rp', 'Q Rp4', 'rp4q'])
res = np.char.swapcase(np1)
print(res)


"""
Change the case to uppercase of elements of an array
"""
import numpy as np

np1 = np.array(['p4q r', '4q rp', 'q rp4', 'rp4q'])
res = np.char.upper(np1)
print(res)


"""
Change the case to lowercase of elements of an array
"""
import numpy as np

np1 = np.array(['P4Q R', '4Q RP', 'Q RP4', 'RP4Q'])
res = np.char.lower(np1)
print(res)


"""
Join String by a separator
"""
import numpy as np

np1 = np.array(['Python', 'Numpy', 'Pandas'])
sep = np.array(['-', '+', '*'])
res = np.core.defchararray.join(sep, np1)
print(res)


"""
Check if two same shaped string arrays one by one
"""
import numpy as np

np1 = np.array('numpy-1')
np2 = np.array('numpy-0')
res = np.char.not_equal(np1, np2)
print(res)


"""
Count the number of substrings in array elements
"""
import numpy as np

np1 = np.array(['Sayantan', '  Sayan  ', 'Sayansubhra'])
res = np.char.count(np1, sub ='an')
print(res)


"""
Find the lowest index of the substring in an array
"""
import numpy as np

np1 = np.array(['aAaAaA', 'baA', 'abBABba'])
res = np.char.find(np1, sub ='A')
print (res)


"""
Get the boolean array when values end with a particular character
"""
import numpy as np
  
np1 = np.array(['geeks', 'for', 'geeks'])
res = np.char.endswith(np1, 'ks')
print(res)