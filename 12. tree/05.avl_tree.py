"""
                        TimeComplexity      SpaceComplexity
pre_order_traversal     ****                ****
in_order_traversal      ****                ****
post_order_traversal    ****                ****
level_order_traversal   ****                ****
insert_node             ****                ****
search_node             ****                ****
delete_node             ****                ****
delete_bst              O(1)                O(1)
"""

from queue import Queue

class AVLNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.height = 1

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

"""
Insertion Conditions in AVL
1. Rotation is not Required(Insertion is same as in BT)
2. Rotation is Required(When left and right subtree depth difference is morethan one)

1. LL Condition
2. LR Condition
3. RR Condition
4. RL Condition

TimeComplexity O(LogN)
SpaceComplexity O(LogN)
"""
def get_height(root_node):
    if not root_node:
        return 0
    return root_node.height

def right_rotate(disbalance_node):
    new_root = disbalance_node.left_child
    disbalance_node.left_child = disbalance_node.left_child.right_child
    new_root.right_child = disbalance_node
    disbalance_node.height = 1 + max(get_height(disbalance_node.left_child), get_height(disbalance_node.right_child))
    new_root.height = 1 + max(get_height(new_root.left_child), get_height(new_root.right_child))
    return new_root

def left_rotate(disbalance_node):
    new_root = disbalance_node.right_child
    disbalance_node.right_child = disbalance_node.right_child.left_child
    new_root.left_child = disbalance_node
    disbalance_node.height = 1 + max(get_height(disbalance_node.left_child), get_height(disbalance_node.right_child))
    new_root.height = 1 + max(get_height(new_root.left_child), get_height(new_root.right_child))
    return new_root

def get_balance(root_node):
    if not root_node:
        return 0
    return get_height(root_node.left_child) - get_height(root_node.right_child)

def insert_node(root_node, node_value):
    """
    1. It uses post order traversal
    """
    if not root_node:
        return AVLNode(node_value)
    elif node_value < root_node.data:
        root_node.left_child = insert_node(root_node.left_child, node_value)
    else:
        root_node.right_child = insert_node(root_node.right_child, node_value)
    
    root_node.height = 1 + max(get_height(root_node.left_child), get_height(root_node.right_child))
    balance = get_balance(root_node)

    if balance > 1 and node_value < root_node.left_child.data:
        return right_rotate(root_node)
    if balance > 1 and node_value > root_node.left_child.data:
        root_node.left_child = left_rotate(root_node.left_child)
        return right_rotate(root_node)
    if balance < -1 and node_value > root_node.right_child.data:
        return left_rotate(root_node)
    if balance < -1 and node_value < root_node.right_child.data:
        root_node.right_child = right_rotate(root_node.right_child)
        return left_rotate(root_node)
    return root_node

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

"""
1. Delete leaf node
2. Delete node if parent node has one sub-node
3. Delete node if parent node has two sub-nodes
4. Do rotation to make the tree balanced
"""
def get_min_value_node(root_node):
    if root_node is None or root_node.left_child is None:
        return root_node
    return get_min_value_node(root_node.left_child)

def delete_node(root_node, node_value):
    """
    1. It uses post order traversal and 
    all the updation will happen form bottom to top(including height and rotations)
    """
    if not root_node:
        return root_node
    elif node_value < root_node.data:
        root_node.left_child = delete_node(root_node.left_child, node_value)
    elif node_value > root_node.data:
        root_node.right_child = delete_node(root_node.right_child, node_value)
    else:
        if root_node.left_child is None:
            temp = root_node.right_child
            root_node = None
            return temp
        elif root_node.right_child is None:
            temp = root_node.left_child
            root_node = None
            return temp
        
        temp = get_min_value_node(root_node.right_child)
        root_node.data = temp.data
        root_node.right_child = delete_node(root_node.right_child, temp.data)

    root_node.height = 1 + max(get_height(root_node.left_child), get_height(root_node.right_child))
    balance = get_balance(root_node)
    
    if balance > 1 and get_balance(root_node.left_child) >= 0:
        return right_rotate(root_node)
    if balance < -1 and get_balance(root_node.right_child) <= 0:
        return left_rotate(root_node)
    if balance > 1 and get_balance(root_node.left_child) < 0:
        root_node.left_child = left_rotate(root_node.left_child)
        return right_rotate(root_node)
    if balance < -1 and get_balance(root_node.right_child) > 0:
        root_node.right_child = right_rotate(root_node.right_child)
        return left_rotate(root_node)
    return root_node

def delete_avl(root_node):
    root_node.data = None
    root_node.left_child = None
    root_node.right_child = None
    return "AVL has been successfully deleted"

new_avl = AVLNode(5)
new_avl = insert_node(new_avl, 10)
new_avl = insert_node(new_avl, 15)
new_avl = insert_node(new_avl, 20)
new_avl = delete_node(new_avl, 15)