"""
Finds the minimum element and move it to the sorted part of array to make unsorted part sorted.
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
    return customList

res = selectionSort([0,9,7,1,2,3,6,5,4,8])
print(res)
