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

def swap(mylist, index1, index2):
    mylist[index1], mylist[index2] = mylist[index2], mylist[index1]

def pivot(mylist, pivot_index, end_index):
    # It will split the array into two sub arrays
    swap_index = pivot_index
    for i in range(pivot_index+1, end_index+1):
        if mylist[i] < mylist[pivot_index]:
            swap_index += 1
            swap(mylist, swap_index, i)
    swap(mylist, pivot_index, swap_index)
    return swap_index

def quickSortHelper(mylist, left, right):
    if left < right:
        pivot_index = pivot(mylist, left, right)
        quickSortHelper(mylist, left, pivot_index-1)
        quickSortHelper(mylist, pivot_index+1, right)
    return mylist

def quickSort(mylist):
    return quickSortHelper(mylist, 0, len(mylist)-1)

cList = [3,5,0,6,2,1,4]
res = quickSort(cList)
print(res)