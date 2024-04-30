"""
1. Create Buckets and distribute elements of array into bucket
2. Sort buckets individually
3. Merge buckets after sorting
"""

import math

def insert_sort(custom_list):
    for i in range(1, len(custom_list)):
        key = custom_list[i]
        j = i - 1 
        while j >= 0 and key < custom_list[j]:
            custom_list[j+1] = custom_list[j]
            j -= 1
        custom_list[j+1] = key
    return custom_list

"""
TimeComplexity is O(n^2)
SpaceComplexity is O(1)
"""
def bucket_sort(custom_list):
    number_of_buckets = round(math.sqrt(len(custom_list)))
    max_value = max(custom_list)
    arr = []

    for i in range(number_of_buckets):
        arr.append([])
    
    for j in custom_list:
        bucket_idx = math.ceil(j*number_of_buckets/max_value)
        arr[bucket_idx-1].append(j)
    
    for i in range(number_of_buckets):
        arr[i] = insert_sort(arr[i])
    
    k = 0
    for i in range(number_of_buckets):
        for j in range(len(arr[i])):
            custom_list[k] = arr[i][j]
            k += 1
    return custom_list


c_list = [2,1,5,3,9,7,4,6,8]
res = bucket_sort(c_list)
print(res)