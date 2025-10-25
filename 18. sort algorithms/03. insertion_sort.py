"""
Take the first element in un-sorted array find its position in sorted array, 
do this repeatedly until unsorted array gets empty.
"""

"""
TimeComplexity is O(n^2)
SpaceComplexity is O(1)
"""
def insertion_sort(custom_list):
    for i in range(1, len(custom_list)):
        key = custom_list[i]
        j = i - 1
        while j >= 0 and key < custom_list[j]:
            custom_list[j+1] = custom_list[j]
            j -= 1
        custom_list[j+1] = key
    return custom_list

res = insertion_sort([2,1,5,4,9,7,6,8,3])
print(res)

"""
1710. Maximum Units on a Truck
"""
def maximum_units(boxTypes, truckSize):
    boxTypes.sort(key=lambda x: x[1], reverse=True)

    total_units = 0
    for numberOfBoxes, unitsPerBox in boxTypes:
        if truckSize <= 0:
            break
        boxes_to_take = min(truckSize, numberOfBoxes)
        total_units += boxes_to_take * unitsPerBox
        truckSize -= boxes_to_take

    return total_units

result = maximum_units([[1,3],[2,2],[3,1]], 4)
print(result)