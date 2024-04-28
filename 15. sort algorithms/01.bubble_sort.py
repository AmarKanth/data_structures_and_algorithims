"""
1. Bubble sort is also known as sinking sort.
2. We repeatedly compare each pair of adjucent items and swap them if they are in the wrong order.
3. Bubble sort keeps the sorted elements at end of the list.
"""

"""
TimeComplexity is O(n^2)
SpaceComplexity is O(1)
"""
def bubble_sort(custom_list):
    for i in range(len(custom_list)-1):
        for j in range(len(custom_list)-i-1):
            if custom_list[j] > custom_list[j+1]:
                custom_list[j], custom_list[j+1] = custom_list[j+1], custom_list[j]
    return custom_list

res = bubble_sort([0,9,7,1,2,3,6,5,4,8])
print(res)