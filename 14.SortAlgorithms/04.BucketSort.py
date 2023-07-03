"""
1. Create Buckets and distribute elements of array into bucket
2. Sort buckets individually
3. Merge buckets after sorting
"""

import math

def insertSort(customList):
    for i in range(1, len(customList)):
        key = customList[i]
        j = i - 1 
        while j >= 0 and key < customList[j]:
            customList[j+1] = customList[j]
            j -= 1
        customList[j+1] = key
    return customList

"""
TimeComplexity is O(n^2)
SpaceComplexity is O(1)
"""
def buckerSort(customList):
    numberOfBuckets = round(math.sqrt(len(customList)))
    maxValue = max(customList)
    arr = []

    for i in range(numberOfBuckets):
        arr.append([])
    
    for j in customList:
        bucket_idx = math.ceil(j*numberOfBuckets/maxValue)
        arr[bucket_idx-1].append(j)
    
    for i in range(numberOfBuckets):
        arr[i] = insertSort(arr[i])
    
    k = 0
    for i in range(numberOfBuckets):
        for j in range(len(arr[i])):
            customList[k] = arr[i][j]
            k += 1
    return customList


cList = [2,1,5,3,9,7,4,6,8]
res = buckerSort(cList)
print(res)