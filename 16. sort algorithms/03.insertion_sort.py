"""
Take the first element in un-sorted array find its position in sorted array, 
do this repearedly until unsorted array gets empty.
"""

"""
TimeComplexity is O(n^2)
SpaceComplexity is O(1)
"""
def insertionSort(customList):
    for i in range(1, len(customList)):
        key = customList[i]
        j = i - 1
        # This loop will continue, until all the elements in sorted array gets sorted.
        while j>=0 and key < customList[j]:
            customList[j+1] = customList[j]
            j -= 1
        # This will decide the position of the current element in sorted array
        customList[j+1] = key
    print(customList)

clist = [2,1,5,4,9,7,6,8,3]
insertionSort(clist)