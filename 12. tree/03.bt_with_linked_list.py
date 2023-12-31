"""
                        TimeComplexity      SpaceComplexity
pre_order_traversal     O(n)                O(n)
in_order_traversal      O(n)                O(n)
post_order_traversal    O(n)                O(n)
level_order_traversal   O(n)                O(1)
insert_node             O(n)                O(n)
search_node             O(n)                O(n)
get_deepest_node        O(n)                O(n)
delete_deepest_node     ****                ****
delete_node             ****                ****
delete_bt               O(1)                O(1)
"""
from queue import Queue


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

new_bt = TreeNode("Drinks")
hot = TreeNode("Hot")
cold = TreeNode("Cold")
new_bt.left_child = hot
new_bt.right_child = cold

tea = TreeNode('Tea')
coffee = TreeNode('Coffee')
hot.left_child = tea
hot.right_child = coffee

coke = TreeNode('Coke')
cold.left_child = coke

def pre_order_traversal(root_node):
    if not root_node:
        return
    print(root_node.data)
    preOrderTraversal(root_node.left_child)
    preOrderTraversal(root_node.right_child)

def in_order_traversal(root_node):
    if not root_node:
        return
    in_order_traversal(root_node.left_child)
    print(root_node.data)
    in_order_traversal(root_node.right_child)

def post_order_traversal(root_node):
    if not root_node:
        return
    post_order_traversal(root_node.left_child)
    post_order_traversal(root_node.right_child)
    print(root_node.data)

def level_order_traversal(root_node):
    if not root_node:
        return
    else:
        q = Queue()
        q.put(root_node)
        while not q.empty():
            root = q.get()
            print(root.data)
            if root.left_child is not None:
                q.put(root.left_child)
            if root.right_child is not None:
                q.put(root.right_child)

def insert_node(root_node, value):
    new_node = TreeNode(value)

    if not root_node:
        root_node = new_node
        return "Node successfully inserted"
    else:
        q = Queue()
        q.put(root_node)
        while not q.empty():
            root = q.get()
            if root.data == value:
                return "Node value is already exist, skip the insertion"
            if root.left_child is not None:
                q.put(root.left_child)
            else:
                root.left_child = new_node
                return "Successfully Inserted"
            if root.right_child is not None:
                q.put(root.right_child)
            else:
                root.right_child = new_node
                return "Successfully Inserted"

def search_node(root_node, value):
    if not root_node:
        return "BT is not exist"
    else:
        q = Queue()
        q.put(root_node)
        while not q.empty():
            root = q.get()
            if root.data == value:
                return "Success"
            if root.left_child is not None:
                q.put(root.left_child)
            if root.right_child is not None:
                q.put(root.right_child)
        return "Not Found"

def get_deepest_node(root_node):
    if not root_node:
        return
    else:
        deepest_node = None
        q = Queue()
        q.put(root_node)
        while not q.empty():
            root = q.get()
            deepest_node = root.data
            if root.left_child:
                q.put(root.left_child)
            if root.right_child:
                q.put(root.right_child)
        return deepest_node

def delete_deepest_node(root_node, deepest_node):
    """
    1. If deepest node is root node make it None
    2. If deepest node is leftChild remove link between root and leftChild
    3. If deepest node is rightChild remove linke between root and rightChild
    """
    if not root_node:
        return
    else:
        q = Queue()
        q.put(root_node)
        while not q.empty():
            root = q.get()
            if root.data == deepest_node:
                root = None
                return
            if root.right_child:
                if root.right_child.data == deepest_node:
                    root.right_child = None
                    return
                else:
                    q.put(root.right_child)
            if root.left_child:
                if root.left_child.data == deepest_node:
                    root.left_child = None
                    return
                else:
                    q.put(root.left_child)

def delete_node(root_node, value):
    """
    1. Find matched node
    2. Find Deepest node
    3. Replace matched node with deepest node
    4. Delete deepest node
    """
    if not root_node:
        return "The BT doesnt exist"
    else:
        q = Queue()
        q.put(root_node)
        while not q.empty():
            root = q.get()
            if root.data == value:
                deepest_node = get_deepest_node(root_node)
                root.data = deepest_node
                delete_deepest_node(root_node, deepest_node)
                return "The node has been successfully deleted"
            if root.left_child:
                q.put(root.left_child)
            if root.right_child:
                q.put(root.right_child)
        return "Failed to delete the node"

def delete_bt(root_node):
    root_node.data = None
    root_node.left_child = None
    root_node.right_child = None
    return "The BT has been successfully deleted"