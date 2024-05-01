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
SpaceComplexity is O(n+k)
"""
def bucket_sort(custom_list):
    number_of_buckets = round(math.sqrt(len(custom_list)))
    min_value = min(custom_list)
    max_value = max(custom_list)
    range_val = (max_value - min_value) / number_of_buckets
 
    buckets = [[] for _ in range(number_of_buckets)]
 
    for j in custom_list:
        if j == max_value:
            buckets[-1].append(j)
        else:
            index_b = math.floor((j - min_value) / range_val)
            buckets[index_b].append(j)
    
    sorted_array = []
    for i in range(number_of_buckets):
        buckets[i] = insertion_sort(buckets[i])
        sorted_array.extend(buckets[i])
    
    return sorted_array

c_list = [2,1,5,3,9,7,4,6,8]
res = bucket_sort(c_list)
print(res)