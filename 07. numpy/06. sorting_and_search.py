"""
where Method
find the index of 30 in given array
[10, 32, 30, 30, 50, 20, 82, 91, 45]
"""
import numpy as np

arr = np.array([10, 32, 30, 30, 50, 20, 82, 91, 45])
i = np.where(arr == 30)
print(i)


"""
searchsorted Method
"""
import numpy as np

arr = np.array([10, 32, 30, 30, 50, 20, 82, 91, 45])
left = np.searchsorted(arr, 30, side="left")
right = np.searchsorted(arr, 30, side='right')
print(right)


"""
argmax Method
"""
import numpy as np

arr = np.arange(12).reshape(3,4)
res1 = np.argmax(arr)
res2 = np.argmax(arr, axis=0)
res3 = np.argmax(arr, axis=1)
print(res3)


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
nanargmax Method
"""
import numpy as np

arr = np.array([[np.nan, 4], [1, 3]])
res1 = np.nanargmax(arr, axis=0)
res2 = np.nanargmax(arr, axis=1)
print(res2)


"""
argmin Method
"""
import numpy as np

arr = np.arange(8).reshape(4,2)
res1 = np.argmin(arr, axis=0)
res2 = np.argmin(arr, axis=1)
print(res2)


"""
sort Method
"""
import numpy as np

arr = np.array([[12, 15], [10, 1]])
sorted = np.sort(arr, axis=0)
print(sorted)

arr = np.array([[10, 15], [12, 1]])
sorted = np.sort(arr, axis=1)
print (sorted)

arr = np.array([[12, 15], [10, 1]])
sorted = np.sort(arr, axis = None)


"""
sort Function
"""
import numpy as np

arr = np.array([12, 15, 10, 1])
arr.sort()
print(arr)

mtrx = np.matrix('[4, 1; 12, 3]')
mtrx.sort()
print(mtrx)


"""
argsort Method
"""
import numpy as np

arr = np.array([9, 3, 1, 7, 4, 3, 6])
sorted_indices = np.argsort(arr)
res = np.zeros(len(sorted_indices), dtype=int)
for i in range(0, len(sorted_indices)):
    res[i] = arr[sorted_indices[i]]
print(res)


"""
lexsort Method
"""
import numpy as np

a = np.array([9, 3, 1, 3, 4, 3, 6])
b = np.array([4, 6, 9, 2, 1, 8, 7])
sorted_indices = np.lexsort((b,a))
print(sorted_indices)


"""
count_nonzero Method
"""
import numpy as np

arr = np.array([[0,1,7,0,0],[3,0,0,2,19]])
res1 = np.count_nonzero(arr, axis=0)
res2 = np.count_nonzero(arr, axis=1)
print(res2)