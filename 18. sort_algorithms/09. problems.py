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


"""
1710. Maximum Units on a Truck
"""
def maximum_units(boxTypes, truckSize):
    boxTypes.sort(key=lambda x: x[1], reverse=True)

    total_units = 0
    for numberOfBoxes, unitsPerBox in boxTypes:
        if truckSize <= 0:
            break
        boxes_to_take = min(truckSize, numberOfBoxes)
        total_units += boxes_to_take * unitsPerBox
        truckSize -= boxes_to_take

    return total_units

result = maximum_units([[1,3],[2,2],[3,1]], 4)
print(result)


"""
3010. Divide an Array Into Subarrays With Minimum Cost I
"""
def min_cost_three_sub_arrays(nums):
    n = len(nums)
    if n < 3:
        return None
    best_pair = float('inf')
    min_prev = nums[1]
    for s3 in range(2, n):
        best_pair = min(best_pair, min_prev + nums[s3])
        min_prev = min(min_prev, nums[s3])
    return nums[0] + best_pair

result = min_cost_three_sub_arrays([10,3,1,1])
print(result)


"""
2164. Sort Even and Odd Indices Independently
"""
def sort_even_odd(nums):
    even = sorted(nums[0::2])
    odd = sorted(nums[1::2], reverse=True)
    
    result = []
    e = o = 0
    for i in range(len(nums)):
        if i % 2 == 0:
            result.append(even[e])
            e += 1
        else:
            result.append(odd[o])
            o += 1
    return result

result = sort_even_odd([4,1,2,3])
print(result)


"""
2144. Minimum Cost of Buying Candies With Discount
"""
def minimum_cost(cost):
    cost.sort(reverse=True)
    total = 0
    for i, c in enumerate(cost):
        if (i + 1) % 3 != 0:
            total += c
    return total

result = minimum_cost([6,5,7,9,2,2])
print(result)


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
