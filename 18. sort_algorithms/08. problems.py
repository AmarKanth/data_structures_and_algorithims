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


"""
1403. Minimum Subsequence in Non-Increasing Order
"""
def min_subsequence(nums):
    nums.sort(reverse=True)
    total = sum(nums)
    taken_sum = 0
    result = []
    for x in nums:
        taken_sum += x
        result.append(x)
        if taken_sum > total - taken_sum:
            return result
    return result

result = min_subsequence([4,3,10,9,8])
print(result)


"""
2389. Longest Subsequence With Limited Sum
"""
def answer_queries(nums, queries):
    nums.sort()
    n = len(nums)
    prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix[i] = prefix[i-1] + nums[i-1]

    def largest_k_leq_q(q):
        low, high = 0, n
        while low < high:
            mid = (low + high + 1) // 2
            if prefix[mid] <= q:
                low = mid
            else:
                high = mid - 1
        return low
    
    return [largest_k_leq_q(q) for q in queries]

result = answer_queries([4,5,2,1], [3,10,21])
print(result)


"""
1385. Find the Distance Value Between Two Arrays
"""
def lower_bound(arr, x):
    low, high = 0, len(arr)
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        else:
            high = mid
    return low

def find_the_distance_value(arr1, arr2, d):
    arr2.sort()
    count = 0
    for x in arr1:
        i = lower_bound(arr2, x)
        ok = True
        if i < len(arr2) and abs(arr2[i] - x) <= d:
            ok = False
        if i - 1 >= 0 and abs(arr2[i-1] - x) <= d:
            ok = False
        if ok:
            count += 1
    return count

arr1=[4,5,8]
arr2=[10,9,1,8] 
d=2
result = find_the_distance_value(arr1, arr2, d)
print(result)
