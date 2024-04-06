"""
1. Bubble sort is also known as sinking sort.
2. We repeatedly compare each pair of adjucent items and swap them if they are in the wrong order
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
    else:
        print(custom_list)

clist = [0,9,7,1,2,3,6,5,4,8]
bubble_sort(clist)