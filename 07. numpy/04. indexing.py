"""
Write the values of the given indexing
si1 = a[1,1]
si2 = a[0:2,2]
si3 = a[-1, 0:2]
si4 = a[:, 1]
si5 = a[:, 1:3]
"""
import numpy as np  
a = np.array([[6,7,8], [1,2,3], [9,3,2]])
si1 = a[1,1]
si2 = a[0:2,2]
si3 = a[-1, 0:2]
si4 = a[:, 1]
si5 = a[:, 1:3]
print(a)


"""
replace elements with 0 which are > 50 in the given matrix
np1 = np.array([75.42436315, 42.48558583, 60.32924763])
"""
import numpy as np
np1 = np.array([75.42436315, 42.48558583, 60.32924763])
np1[np1 > 50.] = 0
print(np1)
  
a = np.arange(12).reshape(3,4)
b = a > 4
a[b] = -1
print(a)


"""
Swapping Columns 2 and 3 in given matrix
arr = np.arange(12).reshape(3,4)
"""
import numpy as np
arr = np.arange(12).reshape(3,4)
arr[:,[3,2]] = arr[:,[2,3]]
print(arr)