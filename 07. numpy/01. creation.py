"""
1. Python does not have built-in support for Arrays, but Python lists can be used instead.
2. We cannot perform all the operations on python list. For example multiplication of 2 lists
can be done easy with numpy.
"""

"""
Create New Numpy Array
"""
import numpy as np
arr = np.array([[1,2],[3,4], [5,6]], dtype=float)
print(arr)
print(arr.size)
print(arr.shape)
print(arr.reshape(2,3))


"""
arange Method
"""
import numpy as np
arr1 = np.arange(5)
arr2 = np.arange(6).reshape(3,2)
print(arr2)


"""
zeros Method
"""
import numpy as np
arr = np.zeros([3, 3], dtype=int) 
print(arr) 


"""
empty Method
"""
import numpy as np
arr = np.empty((3, 4), dtype=int)
print(arr)


"""
full Method
"""
arr = np.full((3, 3), 55, dtype=int)
print(arr)


"""
ones Method
"""
import numpy as np
arr = np.ones([3, 3], dtype=int)
print(arr)


"""
flatten the n*n matrix
The main difference between ravel and flatten is flatten used copy of original object, 
so change in flatten array will not change the main array. In case ravel its vice versa.
"""
import numpy as np
arr = np.array([[2, 3], [4, 5]])
f = arr.flatten()
r = arr.ravel()
print(r)


"""
linspace Method
"""
import numpy as np
arr = np.linspace(2, 3, num=5)
print(arr)


"""
eye Method
Eye method fills diagnal elements with ones, zeros with remaining elements.
"""
import numpy as np
arr = np.eye(4, 5, k=1)
print(arr)


"""
fromiter Method
Here dtype is U2 is 16-bit unsigned integer
"""
import numpy as np
str = "geeksforgeeks"
arr = np.fromiter(str, dtype="U2")
print(arr)


"""
fromrecords Method
"""
import numpy as np
columns = "Rollno, Name, Age"
rows = [(101, 'Jitender', 21), (102, 'Deepak', 20)]
arr = np.core.records.fromrecords(rows, names=columns)
print(arr)
print(arr.Rollno)


"""
How to build an array of all combinations of two NumPy arrays?
"""
import numpy as np
  
np1 = np.array([1, 2])
np2 = np.array([4, 6])

comb_array = np.array(np.meshgrid(np1, np2)).T.reshape(-1, 2)
print(comb_array)


"""
How to find the size of an array
np1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
"""
import numpy as np
np1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(np.size(np1))
print(np.size(np1, 0)) 
print(np.size(np1, 1))