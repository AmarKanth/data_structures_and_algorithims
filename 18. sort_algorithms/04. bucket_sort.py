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

