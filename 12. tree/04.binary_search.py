"""
                        TimeComplexity      SpaceComplexity
pre_order_traversal     O(n)                O(n)
in_order_traversal      O(n)                O(n)
post_order_traversal    O(n)                O(n)
level_order_traversal   O(n)                O(1)
insert_node             O(logN)             O(logN)
search_node             O(logN)             O(logN)
delete_node             O(logN)             O(logN)
delete_bst              O(1)                O(1)
"""

from queue import Queue

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

def pre_order_traversal(root_node):
    if not root_node:
        return
    print(root_node.data)
    pre_order_traversal(root_node.left_child)
    pre_order_traversal(root_node.right_child)

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
            if root.left_child:
                q.put(root.left_child)
            if root.right_child:
                q.put(root.right_child)

def insert_node(root_node, node_value):
    if root_node.data == None:
        root_node.data = node_value
    elif node_value <= root_node.data:
        if root_node.left_child == None:
            root_node.left_child = BSTNode(node_value)
        else:
            insert_node(root_node.left_child, node_value)
    else:
        if node_value > root_node.data:
            if root_node.right_child == None:
                root_node.right_child = BSTNode(node_value)
            else:
                insert_node(root_node.right_child, node_value)

def search_node(root_node, node_value):
    if root_node.data == node_value:
        print("Value is found")
    elif node_value < root_node.data:
        if root_node.data == node_value:
            print("Value is found")
        else:
            search_node(root_node.left_child, node_value)
    else:
        if root_node.data == node_value:
            print("Value is found")
        else:
            search_node(root_node.right_child, node_value)

def min_value_node(bst_node):
    current = bst_node
    while (current.left_child):
        current = current.left_child
    return current

def delete_node(root_node, node_value):
    if root_node == None:
        return root_node
    if node_value < root_node.data:
        root_node.left_child = delete_node(root_node.left_child, node_value)
    elif node_value > root_node.data:
        root_node.right_child = delete_node(root_node.right_child, node_value)
    else:
        """
        The below two if conditions will be execute
        when we trying to delete leaf node
        """
        if root_node.left_child == None:
            temp = root_node.right_child
            root_node = None
            return temp
        
        if root_node.right_child == None:
            temp = root_node.left_child
            root_node = None
            return temp

        """
        1. The below code will be execute when there is a childs to the nodeValue.
        2. minValueNode fetches the successor
        3. it will replace the deleted node value with successor
        4. the last line re-arrange the all nodes
        """
        temp = min_value_node(root_node.right_child)
        root_node.data = temp.data
        root_node.right_child = delete_node(root_node.right_child, temp.data)
    return root_node

def delete_bst(root_node):
    root_node.data = None
    root_node.left_child = None
    root_node.right_child = None
    return "BST successfully deleted"