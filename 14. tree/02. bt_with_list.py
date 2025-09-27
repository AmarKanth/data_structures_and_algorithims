"""
                        TimeComplexity      SpaceComplexity
init                    O(1)                O(1)
insert_node             O(1)                O(1)
search_node             O(n)                O(1)
pre_order_traversal     O(n)                O(n)
in_order_traversal      O(n)                O(n)
post_order_traversal    O(n)                O(n)
level_order_traversal   O(n)                O(1)
delete                  O(n)                O(1)
delete_bt               O(1)                O(1)
"""

class BinaryTree:
    def __init__(self, size):
        self.custom_list = size * [None]
        self.last_used_index = 0
        self.max_size = size
    
    def insert_node(self, value):
        if self.last_used_index + 1 == self.max_size:
            return "The Binary Tree is full"
        self.custom_list[self.last_used_index+1] = value
        self.last_used_index += 1
        return "The value has been successfully inserted"
    
    def search_node(self, node_value):
        for idx in range(1, self.last_used_index+1):
            if self.custom_list[idx] == node_value:
                return "Success"
        return "Not Found"
    
    def pre_order_traversal(self, index):
        """
        1.Visit the root node.
        2.Recursively traverse the left subtree.
        3.Recursively traverse the right subtree.
        """
        if index > self.last_used_index:
            return
        print(self.custom_list[index])
        self.pre_order_traversal(index*2)
        self.pre_order_traversal(index*2+1)
    
    def in_order_traversal(self, index):
        """
        1.Recursively traverse the left subtree.
        2.Visit the root node.
        3.Recursively traverse the right subtree.
        """
        if index > self.last_used_index:
            return
        self.in_order_traversal(index*2)
        print(self.custom_list[index])
        self.in_order_traversal(index*2+1)
    
    def post_order_traversal(self, index):
        """
        1.Recursively traverse the left subtree.
        2.Recursively traverse the right subtree.
        3.Visit the root node.
        """
        if index > self.last_used_index:
            return
        self.post_order_traversal(index*2)
        self.post_order_traversal(index*2+1)
        print(self.customList[index])
    
    def level_order_traversal(self, index):
        """
        1.Visit all the nodes at each level
        """
        for idx in range(index, self.last_used_index+1):
            print(self.custom_list[idx])
    
    def delete_node(self, value):
        if self.last_used_index == 0:
            return "There is no node to delete"
        for idx in range(1, self.last_used_index+1):
            if self.custom_list[idx] == value:
                self.custom_list[idx] = self.custom_list[self.last_used_index]
                self.custom_list[self.last_used_index] = None
                self.last_used_index -= 1
                return "The node has been successfully deleted"
    
    def delete_bt(self):
        self.custom_list = None
        return "The BT has been successfully deleted"

newBT = BinaryTree(8)
newBT.insert_node("Drinks")
newBT.insert_node("Hot")
newBT.insert_node("Cold")
newBT.insert_node("Tea")
newBT.insert_node("Coffee")


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
