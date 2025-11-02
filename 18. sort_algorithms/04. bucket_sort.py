"""
1. Create Buckets and distribute elements of array into bucket
2. Sort buckets individually
3. Merge buckets after sorting
"""

import math

def insertion_sort(arr):
    for i in range(len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

"""
TimeComplexity is O(n^2)
SpaceComplexity is O(n+k)
"""
def bucket_sort(custom_list):
    number_of_buckets = math.ceil(math.sqrt(len(custom_list)))
    min_value = min(custom_list)
    max_value = max(custom_list)
    range_val = (max_value - min_value)/number_of_buckets
    buckets = [[] for _ in range(number_of_buckets)]
    sorted_array = []

    for j in custom_list:
        idx = math.floor((j-min_value)/range_val)
        if idx == number_of_buckets:
            idx -= 1
        buckets[idx].append(j)

    for i in range(number_of_buckets):
        arr = insertion_sort(buckets[i])
        sorted_array.extend(arr)

    return sorted_array

res = bucket_sort([2,1,5,3,9,7,4,6,8])
print(res)

"""
455. Assign Cookies
"""
def find_content_children(g, s):
    g.sort()
    s.sort()
    i = 0
    j = 0
    content = 0

    while i < len(g) and j < len(s):
        if s[j] >= g[i]:
            content += 1
            i += 1
            j += 1
        else:
            j += 1
    return content

result = find_content_children([1,2], [1,2,3])
print(result)

"""
88. Merge Sorted Array
"""
def merge(nums1, m, nums2, n):
    p1 = m - 1
    p2 = n - 1
    p = m + n - 1

    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1

    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
merge(nums1, 3, nums2, 3)
print(nums1)

"""
1005. Maximize Sum Of Array After K Negations
"""
def largest_sum_after_k_negations(nums, k):
    nums.sort()
    n = len(nums)

    i = 0
    while i < n and k > 0 and nums[i] < 0:
        nums[i] = -nums[i]
        i += 1
        k -= 1

    total = sum(nums)
    min_abs = min(abs(x) for x in nums)
    if k % 2 == 1:
        total -= 2 * min_abs
    return total

result = largest_sum_after_k_negations([4,2,3], 1)
print(result)

"""
747. Largest Number At Least Twice of Others
"""
def dominant_index(nums):
    if len(nums) == 1:
        return 0

    max_num = max(nums)
    max_index = nums.index(max_num)

    second_max = max(x for x in nums if x != max_num)

    if max_num >= 2 * second_max:
        return max_index
    else:
        return -1

result = dominant_index([3,6,1,0])
print(result)

"""
645. Set Mismatch
"""
def find_error_nums(nums):
    seen = set()
    duplicate = -1

    for num in nums:
        if num in seen:
            duplicate = num
        seen.add(num)

    n = len(nums)
    missing = (set(range(1, n + 1)) - seen).pop()
    return [duplicate, missing]

result = find_error_nums([1,2,2,4])
print(result)