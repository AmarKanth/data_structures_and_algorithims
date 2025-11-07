"""
1. Merge Sort is a devide and conquer algorithm
2. Divide the input array in two halves and we keep halving recusrively 
until they become too small that cant not be broken further
3. Merge halves by sorting them
"""

def merge(custom_list, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0]*(n1)
    R = [0]*(n2)

    for i in range(0, n1):
        L[i] = custom_list[l+i]
    
    for j in range(0, n2):
        R[j] = custom_list[m+1+j]
    
    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            custom_list[k] = L[i]
            i += 1
        else:
            custom_list[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        custom_list[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        custom_list[k] = R[j]
        j += 1
        k += 1

"""
TimeComplexity O(NLogN)
SpaceComplexity O(n)
Note : Refer Big O Notaion for T(N/2) and O(NLogN)
"""
def merge_sort(custom_list, l, r):
    if l < r:
        m = (l+r)//2
        merge_sort(custom_list, l, m)
        merge_sort(custom_list, m+1, r)
        merge(custom_list, l, m, r)
    return custom_list

clist = [2,1,7,6,5,3,4,9,8]
res = merge_sort(clist, 0, len(clist)-1)
print(res)


"""
349 Intersection of two arrays
"""
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

nums1.sort()
nums2.sort()

i = 0 
j = 0
result = set()
while i < len(nums1) and j < len(nums2):
    if nums1[i] < nums2[j]:
        i += 1
    elif nums1[i] == nums2[j]:
        result.add(nums1[i])
        i += 1
        j += 1
    else:
        j += 1
print(result)


"""
2996. Smallest Missing Integer Greater Than Sequential Prefix Sum
"""
def smallest_missing_at_least_prefix_sum(nums):
    if not nums:
        return 0
    
    k = 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1] + 1:
            k += 1
        else:
            break

    a0 = nums[0]
    s = k * (2 * a0 + (k - 1)) // 2
    present = set(nums)
    x = s
    while x in present:
        x += 1
    return x

result = smallest_missing_at_least_prefix_sum([1,2,3,2,5])
print(result)