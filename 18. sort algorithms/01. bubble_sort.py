"""
TimeComplexity is O(n^2)
SpaceComplexity is O(1)
"""
def bubble_sort(custom_list):
    for i in range(len(custom_list)-1):
        for j in range(len(custom_list)-i-1):
            if custom_list[j] > custom_list[j+1]:
                custom_list[j], custom_list[j+1] = custom_list[j+1], custom_list[j]
    return custom_list

res = bubble_sort([0,9,7,1,2,3,6,5,4,8])
print(res)

"""
406. Queue Reconstruction by Height
"""
people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
people.sort(key=lambda x: (-x[0], x[1]))

ans = []
for p in people:
    ans.insert(p[1], p)
print(ans)

"""
1365. How Many Numbers Are Smaller Than the Current Number
"""
nums = [8,1,2,2,3]

sorted_arr = sorted(nums)
freq = {}
for i, val in enumerate(sorted_arr):
    if val in freq:
        continue
    freq[val] = i

ans = []
for num in nums:
    ans.append(freq[num])
print(ans)

"""
1636. Sort Array by Increasing Frequency
"""
from collections import Counter

nums = [1,1,2,2,2,3]
freq = Counter(nums)
nums.sort(key=lambda x: (freq[x], -x))
return nums

"""
1356. Sort Integers by The Number of 1 Bits
"""
def custom_sort_key(num):
    bit_count = bin(num).count('1')
    return (bit_count, num)

arr = [0,1,2,3,4,5,6,7,8]
arr.sort(key=custom_sort_key)

"""
1337. The K Weakest Rows in a Matrix
"""
mat = [[1,1,0,0,0],
       [1,1,1,1,0],
       [1,0,0,0,0],
       [1,1,0,0,0],
       [1,1,1,1,1]]
m = len(mat)
k = 3

rows = sorted(range(m), key=lambda i: (mat[i], i))
del rows[k:]
print(rows)