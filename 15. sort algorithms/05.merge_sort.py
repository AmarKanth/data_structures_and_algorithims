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
        m = (l+(r-1))//2
        merge_sort(custom_list, l, m)
        merge_sort(custom_list, m+1, r)
        merge(custom_list, l, m, r)
    return custom_list

clist = [2,1,7,6,5,3,4,9,8]
res = merge_sort(clist, 0, 8)
print(res)