"""
Take the first element in un-sorted array find its position in sorted array, 
do this repearedly until unsorted array gets empty.
"""

"""
TimeComplexity is O(n^2)
SpaceComplexity is O(1)
"""
def insertion_sort(custom_list):
    for i in range(1, len(custom_list)):
        key = custom_list[i]
        j = i - 1
        # This loop will continue, until all the elements in sorted array gets sorted.
        while j>=0 and key < custom_list[j]:
            custom_list[j+1] = custom_list[j]
            j -= 1
        # This will decide the position of the current element in sorted array
        custom_list[j+1] = key
    return custom_list

res = insertion_sort([2,1,5,4,9,7,6,8,3])
print(res)