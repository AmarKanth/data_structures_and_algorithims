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

"""
Dept First Search
-----------------
1. pre order traversal
    Visit the current node (the root node initially).
    Recursively traverse the left subtree.
    Recursively traverse the right subtree.
2. in order traversal
    Recursively traverse the left subtree.
    Visit the current node.
    Recursively traverse the right subtree.
3. post order traversal
    Recursively traverse the left subtree.
    Recursively traverse the right subtree.
    Visit the current node.
Breadth First Search
--------------------
1. level order traversal
"""
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
            if root.left_child is not None:
                q.put(root.left_child)
            if root.right_child is not None:
                q.put(root.right_child)

def insert_node(root_node, value):
    new_node = TreeNode(value)
    if root_node == None:
        return new_node
    else:
        q = Queue()
        q.put(root_node)
        while not q.empty():
            root = q.get()
            if root.data == value:
                break
            if root.left_child:
                q.put(root.left_child)
            else:
                root.left_child = new_node
                break
            if root.right_child:
                q.put(root.right_child)
            else:
                root.right_child = new_node
                break
        return root_node

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
    if root_node == None:
        return root_node
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
        return root_node
    else:
        q = Queue()
        q.put(root_node)
        while not q.empty():
            root = q.get()
            if root.data == deepest_node:
                root = None
                break
            if root.left_child:
                if root.left_child.data == deepest_node:
                    root.left_child = None
                    break
                else:
                    q.put(root.left_child)
            if root.right_child:
                if root.right_child.data == deepest_node:
                    root.right_child = None
                    break
                else:
                    q.put(root.right_child)
        return root_node

def delete_node(root_node, value):
    if root_node == None:
        return root_node
    else:
        q = Queue()
        q.put(root_node)
        while not q.empty():
            root = q.get()
            if root.data == value:
                deepest_node = get_deepest_node(root_node)
                delete_deepest_node(root_node, deepest_node)
                root.data = deepest_node
                break
            if root.left_child:
                q.put(root.left_child)
            if root.right_child:
                q.put(root.right_child)
        return root_node

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
tree = insert_node(tree, 20)
tree = insert_node(tree, 30)
tree = insert_node(tree, 40)
tree = insert_node(tree, 50)
tree = insert_node(tree, 60)
tree = insert_node(tree, 70)
tree = insert_node(tree, 80)
tree = delete_node(tree, 10)
tree = delete_node(tree, 20)
tree = delete_node(tree, 30)
tree = delete_node(tree, 40)
tree = delete_node(tree, 50)
print_tree(tree)
