def swap(custom_list, index1, index2):
    custom_list[index1], custom_list[index2] = custom_list[index2], custom_list[index1]

def pivot(custom_list, pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index+1, end_index+1):
        if custom_list[i] < custom_list[pivot_index]:
            swap_index += 1
            swap(custom_list, swap_index, i)
    swap(custom_list, pivot_index, swap_index)
    return swap_index

def quick_sort_helper(custom_list, left, right):
    if left < right:
        pivot_index = pivot(custom_list, left, right)
        quick_sort_helper(custom_list, left, pivot_index-1)
        quick_sort_helper(custom_list, pivot_index+1, right)
    return custom_list

"""
TimeComplexity O(NLogN)
SpaceComplexity O(n)
"""
def quick_sort(custom_list):
    return quick_sort_helper(custom_list, 0, len(custom_list)-1)

res = quick_sort([3,5,0,6,2,1,4])
print(res)