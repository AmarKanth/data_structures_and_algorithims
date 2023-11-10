"""
1. Bubble sort is also known as sinking sort.
2. We repeatedly compare each pair of adjucent items and swap them if they are in the wrong order
"""

"""
TimeComplexity is O(n^2)
SpaceComplexity is O(1)
"""
def bubbleSort(customList):
    for i in range(len(customList)-1):
        for j in range(len(customList)-i-1):
            if customList[j] > customList[j+1]:
                customList[j], customList[j+1] = customList[j+1], customList[j]
    else:
        print(customList)

cList = [0,9,7,1,2,3,6,5,4,8]
bubbleSort(cList)