"""
1011. Capacity To Ship Packages Within D Days
"""
weights = [1,2,3,4,5,6,7,8,9,10]
days = 5

left = max(weights)
right = sum(weights)

while left < right:
    mid = (left + right) // 2
    days_needed, curr_weight = 1, 0

    for weight in weights:
        if curr_weight + weight > mid:
            days_needed += 1
            curr_weight = 0
        curr_weight += weight    
    
    if days_needed > days:
        left = mid + 1
    else:
        right = mid
print(left)


"""
889. Construct Binary Tree from Preorder and Postorder Traversal
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def construct_bt(preorder, postorder):
    n = len(preorder)
    postorder_pos = {value:idx for idx, value in enumerate(postorder)}

    def build(pre_start, pre_end, post_start, post_end):
        if pre_start > pre_end:
            return None
        
        root_value = preorder[pre_start]
        root = TreeNode(root_value)

        if pre_start == pre_end:
            return root

        left_root_value = preorder[pre_start+1]
        left_node_in_postorder_pos = postorder_pos[left_root_value]
        left_size = left_node_in_postorder_pos - post_start + 1

        root.left = build(
            pre_start+1, 
            pre_start+left_size, 
            post_start, 
            left_node_in_postorder_pos
        )
        root.right = build(
            pre_start+left_size+1, 
            pre_end, 
            left_node_in_postorder_pos+1,
            post_end-1
        )
        return root
    return build(0, n-1, 0, n-1)

preorder = [1,2,4,5,3,6,7]
postorder = [4,5,2,6,7,3,1]
root = construct_bt(preorder, postorder)


"""
1552. Magnetic Force Between Two Balls
"""
position = [1,2,3,4,7]
m = 3

position.sort()
l, r = 1, position[-1] - position[0]
ans = -1
while l <= r:
    mid = l + (r - l) // 2
    last_position, balls = position[0], 1
    for i in range(1, len(position)):
        if position[i] - last_position >= mid:
            last_position = position[i]
            balls += 1
    if balls >= m:
        ans = mid
        l = mid + 1
    else:
        r = mid - 1
print(ans)


"""
2554. Maximum Number of Integers to Choose From a Range I
"""
banned = [1,6,5]
n = 5
maxSum = 6

banned_set = set(banned)
total_sum = 0
count = 0

for i in range(1, n + 1):
    if i in banned_set:
        continue
    total_sum += i
    if total_sum > maxSum:
        break
    count += 1
print(count)


"""
786. K-th Smallest Prime Fraction
"""
from heapq import heappush, heappop

arr = [1,2,3,5]
k = 3

min_heap = []
n = len(arr)

for i in range(n):
    for j in range(i+1, n):
        fraction = (arr[i] / arr[j], (arr[i], arr[j]))
        heappush(min_heap, fraction)

for _ in range(k - 1):
    heappop(min_heap)

print(heappop(min_heap)[1])