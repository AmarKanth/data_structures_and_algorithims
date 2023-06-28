"""
In case of selection sort we repeatedly find the minimum element and 
move it to the sorted part of array to make unsorted part sorted.
"""

"""
TimeComplexity is O(n^2)
SpaceComplexity is O(1)
"""
def selectionSort(customList):
    for i in range(len(customList)):
        min_index = i
        # this is to find the min value in the unorted part of array
        for j in range(i+1, len(customList)):
            if customList[min_index] > customList[j]:
                min_index = j
        customList[min_index], customList[i] = customList[i], customList[min_index]
    else:
        print(customList)

cList = [0,9,7,1,2,3,6,5,4,8]
selectionSort(cList)