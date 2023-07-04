"""
QuickSort Algorithm
-------------------
1. Take First element consider it as pivot number.
2. Separate the list with elements less than pivot number.
3. Separate the list with elements greater than pivot number.
4. Now place pivot number after last element of 1st list(elements which are less than pivot number).
5. The pivot number is in right sort order.
6. Repeat the entire process with first element again.
7. Once all the elements in first half of the list sorted then move on to second half of the elements.
"""

def swap(my_list, index1, index2):
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]

def pivot(my_list, pivot_index, end_index):
    # It will split the array into two sub arrays
    swap_index = pivot_index
    for i in range(pivot_index+1, end_index+1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
    swap(my_list, pivot_index, swap_index)
    return swap_index

def quickSort(mylist):
    pass