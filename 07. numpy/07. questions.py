"""
Check whether a Numpy array contains a specified row
"""
import numpy as np

array = np.array([[1, 2, 3, 4, 5],
                  [6, 7, 8, 9, 10],
                  [11, 12, 13, 14, 15],
                  [16, 17, 18, 19, 20]])

print([1, 2, 3, 4, 5] in array.tolist())

"""
How to Remove rows in Numpy array that contains non-numeric values?
Here axis 0 is the columns and axis 1 is the rows
"""
import numpy as np

array = np.array([[10.5, 22.5, 3.8], 
                  [23.45, 50, 78.7],
                  [41, np.nan, np.nan]])

print(array[~np.isnan(array).any(axis=1)])

"""
Remove single dimensional entries from the shape
"""
import numpy as np

array = np.array([[[2, 2, 2], [2, 2, 2]]])
print(np.squeeze(array))

"""
Find the number of occurrences of a sequence in a NumPy array
"""
import numpy as np
  
array = np.array([[2, 8, 9, 4], 
                  [9, 4, 9, 4],
                  [4, 5, 9, 7],
                  [2, 9, 4, 3]])

output = repr(array).count("9, 4")
print(output)

"""
Find most common pair in NumPy array
"""
import numpy as np

array = np.array([[2, 8, 9, 4], 
                  [9, 4, 9, 4],
                  [4, 5, 9, 7],
                  [2, 9, 4, 3]])

flat = array.flatten()

d  = dict()
for i in range(0, len(flat)-1):
        comb = (flat[i], flat[i+1])
        if comb in d.keys():
            d[comb] += 1
        else:
            d[comb] = 1

sorted = sorted(d.items(), key=lambda t: t[1], reverse=True)
print(sorted[0][0])

"""
Find the most frequent value in a NumPy array
"""
import numpy as np

x = np.array([1, 1, 1, 2, 3, 4, 2, 4, 3, 3])
print(np.bincount(x).argmax())

# if the array contains more than one element 
# having the maximum number of frequency
y = np.bincount(x)
maximum = max(y)
  
for i in range(len(y)):
    if y[i] == maximum:
        print(i, end=" ")


"""
How to build an array of all combinations of two NumPy arrays?
"""
import numpy as np
  
np1 = np.array([1, 2])
np2 = np.array([4, 6])

comb_array = np.array(np.meshgrid(np1, np2)).T.reshape(-1, 2)
print(comb_array)

"""
How to check whether specified values are 
present in n*n NumPy?
"""
import numpy as np
  
np1 = np.array([[2, 3, 0],
               [4, 1, 6]])
print(10 in np1)

"""
How to get the diagonal elements of
n*n matrix
"""
import numpy as np
  
np1 = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
res = np.diagonal(np1)
print(res)

"""
Count the number of non zero values in the array
"""
import numpy as np
  
np1 = np.array([[0, 2, 0], [0, 5, 0], [0, 8, 0]])
res = np.count_nonzero(np1)
print(res)

"""
How to find the size of an array
"""
import numpy as np

np1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(np.size(np1))
print(np.size(np1, 0)) 
print(np.size(np1, 1))

"""
Write a program to remove leading and trailing zeros
from an array
"""
import numpy as np 
  
np1 = np.array([0, 0, 0, 0, 1, 5, 7, 0, 6, 2, 9, 0, 10, 0, 0])
res = np.trim_zeros(np1)
print(res)

"""
How to reverse the numpy array
"""
import numpy as np
 
np1 = np.array([1, 2, 3, 6, 4, 5])
res = np.flip(np1)
print(res)

"""
How to make numpy readonly
"""
import numpy as np

a = np.zeros(11)
a.setflags(write=False)

"""
insert new column at position 2
"""
import numpy as np

twoDArray = np.array([["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]])
newTwoDArray = np.insert(twoDArray, 2, [[1,2,3]], axis=1)
print(newTwoDArray)

"""
insert new row at last
"""
import numpy as np

twoDArray = np.array([["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]])
newTwoDArray = np.append(twoDArray, [[1,2,3]], axis=0)
print(newTwoDArray)

"""
delete first column
"""
import numpy as np

twoDArray = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
newTwoDArray = np.delete(twoDArray, 0, axis=1)
print(newTwoDArray)