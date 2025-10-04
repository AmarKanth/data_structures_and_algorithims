"""
TimeComplexity is O(n^2)
SpaceComplexity is O(1)
"""
def bubble_sort(custom_list):
    for i in range(len(custom_list)-1):
        for j in range(len(custom_list)-i-1):
            if custom_list[j] > custom_list[j+1]:
                custom_list[j], custom_list[j+1] = custom_list[j+1], custom_list[j]
    return custom_list

res = bubble_sort([0,9,7,1,2,3,6,5,4,8])
print(res)

"""
406. Queue Reconstruction by Height
"""
people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
people.sort(key=lambda x: (-x[0], x[1]))

ans = []
for p in people:
    ans.insert(p[1], p)
print(ans)