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


"""
349 Intersection of two arrays
"""
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

nums1.sort()
nums2.sort()

i = 0 
j = 0
result = set()
while i < len(nums1) and j < len(nums2):
    if nums1[i] < nums2[j]:
        i += 1
    elif nums1[i] == nums2[j]:
        result.add(nums1[i])
        i += 1
        j += 1
    else:
        j += 1
print(result)


"""
2996. Smallest Missing Integer Greater Than Sequential Prefix Sum
"""
def smallest_missing_at_least_prefix_sum(nums):
    if not nums:
        return 0
    
    k = 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1] + 1:
            k += 1
        else:
            break

    a0 = nums[0]
    s = k * (2 * a0 + (k - 1)) // 2
    present = set(nums)
    x = s
    while x in present:
        x += 1
    return x

result = smallest_missing_at_least_prefix_sum([1,2,3,2,5])
print(result)


"""
2545. Sort the Students by Their Kth Score
"""
def sort_the_students(score, k):
    return sorted(score, key=lambda row: row[k], reverse=True)

score = [[10,6,9,1],
         [7,5,11,2],
         [4,8,3,15]]
result = sort_the_students(score, 2)