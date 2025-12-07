"""
Convert the list into binary tree
input_list = [2,1,3,None,None,0,1]
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def convert_list_to_binary_tree(node_list, index=0):
    if index >= len(node_list) or node_list[index] is None:
        return None
    root = TreeNode(node_list[index])
    left_index = index * 2 + 1
    right_index = index * 2 + 2
    root.left = convert_list_to_binary_tree(node_list, left_index)
    root.right = convert_list_to_binary_tree(node_list, right_index)
    return root

def print_tree(root, level=0):
    if root:
        print_tree(root.right, level+1)
        print(" " * 4 * level + "->" + str(root.val))
        print_tree(root.left, level+1)

input_list = [2,1,3,None,None,0,1]
bt = convert_list_to_binary_tree(input_list)
print_tree(bt)


"""
Dutch National Flag
"""
nums = [0,1,2,0,1,2]
left = 0
mid = 0
right = len(nums)-1

while mid <= right:
    if nums[mid] == 0:
        nums[left], nums[mid] = nums[mid], nums[left]
        left += 1
        mid += 1
    elif nums[mid] == 1:
        mid += 1
    else:
        nums[mid], nums[right] = nums[right], nums[mid]
        right -= 1
print(nums)


"""
Count number of nodes
"""
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def count_nodes(root):
    if not root:
        return 0

    def get_height(node):
        height = 0
        while node.left:
            height += 1
            node = node.left
        return height

    def exists(index, height, node):
        left = 0
        right = (2 ** height) - 1
        for _ in range(height):
            mid = (left + right) // 2
            if index <= mid:
                node = node.left
                right = mid
            else:
                node = node.right
                left = mid + 1
            if not node:
                return False
        return True

    height = get_height(root)
    if height == 0:
        return 1

    left = 0
    right = (2 ** height) - 1
    while left <= right:
        mid = (left + right) // 2
        if exists(mid, height, root):
            left = mid + 1
        else:
            right = mid - 1

    return (2 ** height - 1) + left


"""
1351 Count the negative numbers in sorted matrix
"""
def count_negatives(grid):
    rows = len(grid)
    cols = len(grid[0])
    total = 0

    for row in grid:
        left, right = 0, cols - 1

        while left <= right:
            mid = (left + right) // 2
            if row[mid] < 0:
                right = mid - 1
            else:
                left = mid + 1
        total += cols - left
    
    return total

grid = [
    [4,3,2,-1],
    [3,2,1,-1],
    [1,1,-1,-2],
    [-1,-1,-2,-3]
]
result = count_negatives(grid)
print(result)
