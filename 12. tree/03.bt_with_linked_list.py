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

def pre_order_traversal(root_node):
    """
    Visit the current node (the root node initially).
    Recursively traverse the left subtree.
    Recursively traverse the right subtree.
    """
    if not root_node:
        return
    print(root_node.data)
    pre_order_traversal(root_node.left_child)
    pre_order_traversal(root_node.right_child)

def in_order_traversal(root_node):
    """
    Recursively traverse the left subtree.
    Visit the current node.
    Recursively traverse the right subtree.
    """
    if not root_node:
        return
    in_order_traversal(root_node.left_child)
    print(root_node.data)
    in_order_traversal(root_node.right_child)

def post_order_traversal(root_node):
    """
    Recursively traverse the left subtree.
    Recursively traverse the right subtree.
    Visit the current node.
    """
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
        return "Node has been successfully inserted"
    else:
        q = Queue()
        q.put(root_node)
        while not q.empty():
            root = q.get()
            if root.data == value:
                return "Node value is already exist, skip the insertion"
            if root.left_child:
                q.put(root.left_child)
            else:
                root.left_child = new_node
                return "Node has been successfully inserted"
            if root.right_child:
                q.put(root.right_child)
            else:
                root.right_child = new_node
                return "Node has been successfully inserted"

def search_node(root_node, value):
    if not root_node:
        return "Binary Tree is doesnt exist"
    else:
        q = Queue()
        q.put(root_node)
        while not q.empty():
            root = q.get()
            if root.data == value:
                return "Success"
            if root.left_child:
                q.put(root.left_child)
            if root.right_child:
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
    if root_node == None:
        return "Binary Tree is doesnt exist"
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
    if not root_node:
        return "Binary Tree is doesnt exist"
    else:
        q = Queue()
        q.put(root_node)
        while not q.empty():
            root = q.get()
            if root.data == value:
                deepest_node = get_deepest_node(root_node)
                delete_deepest_node(root_node, deepest_node)
                root.data = deepest_node
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

def print_tree(root_node, level=0):
    if root_node:
        print_tree(root_node.left_child, level + 1)
        print(' ' * 4 * level + '-> ' + str(root_node.data))
        print_tree(root_node.right_child, level + 1)

tree = TreeNode(10)
insert_node(tree, 20)
insert_node(tree, 30)
insert_node(tree, 40)
insert_node(tree, 50)
insert_node(tree, 60)
insert_node(tree, 70)
insert_node(tree, 80)
delete_node(tree, 10)
delete_node(tree, 20)
delete_node(tree, 30)
delete_node(tree, 40)
delete_node(tree, 50)
print_tree(tree)