"""
delete first column from 
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
"""
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
new_arr = np.delete(arr, 0, axis=1)
print(new_arr)