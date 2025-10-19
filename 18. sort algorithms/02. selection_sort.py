"""
Finds the minimum element and move it to the sorted part of array to make 
unsorted part sorted.
"""

"""
TimeComplexity is O(n^2)
SpaceComplexity is O(1)
"""
def selection_sort(custom_list):
    for i in range(len(custom_list)):
        min_index = i
        for j in range(i+1, len(custom_list)):
            if custom_list[min_index] > custom_list[j]:
                min_index = j
        custom_list[min_index], custom_list[i] = custom_list[i], custom_list[min_index]
    return custom_list

res = selection_sort([0,9,7,1,2,3,6,5,4,8])
print(res)

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

"""
1608. Special Array With X Elements Greater Than or Equal X
"""
def lower_bound(arr, target):
    low, high = 0, len(arr)
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid
    return low

def special_array(nums):
    n = len(nums)
    nums.sort()
    for x in range(0, n + 1):
        idx = lower_bound(nums, x)
        count_ge = n - idx
        if count_ge == x:
            return x
    return -1

result = special_array([3,5])
print(result)

"""
888. Fair Candy Swap
"""
def fair_candy_swap(aliceSizes, bobSizes):
    sumA, sumB = sum(aliceSizes), sum(bobSizes)
    delta = (sumB - sumA) // 2
    setB = set(bobSizes)
    
    for x in aliceSizes:
        if x + delta in setB:
            return [x, x + delta]

aliceSizes = [1,1]
bobSizes = [2,2]
result = fair_candy_swap(aliceSizes, bobSizes)
print(result)