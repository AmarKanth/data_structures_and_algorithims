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
            if root.left_child:
                q.put(root.left_child)
            if root.right_child:
                q.put(root.right_child)

def get_height(root_node):
    if not root_node:
        return 0
    return root_node.height

def get_balance(root_node):
    if not root_node:
        return 0
    return get_height(root_node.left_child) - get_height(root_node.right_child)

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

def insert_node(root_node, node_value):
    if not root_node:
        return AVLNode(node_value)
    elif node_value < root_node.data:
        root_node.left_child = insert_node(root_node.left_child, node_value)
    else:
        root_node.right_child = insert_node(root_node.right_child, node_value)
    
    root_node.height = 1 + max(get_height(root_node.left_child), get_height(root_node.right_child))
    balance = get_balance(root_node)
    if balance > 1 and get_balance(root_node.left_child) >= 0:
        return right_rotate(root_node)
    if balance > 1 and get_balance(root_node.left_child) < 0:
        root_node.left_child = left_rotate(root_node.left_child)
        return right_rotate(root_node)
    if balance < -1 and get_balance(root_node.right_child) <= 0:
        return left_rotate(root_node)
    if balance < -1 and get_balance(root_node.right_child) > 0:
        root_node.right_child = right_rotate(root_node.right_child)
        return left_rotate(root_node)
    return root_node

def search_node(root_node, value):
    if root_node.data == value:
        print("value is found")
    elif value < root_node.data:
        search_node(root_node.left_child)
    else:
        search_node(root_node.right_child)

def get_min_value_node(root_node):
    if root_node is None or root_node.left_child is None:
        return root_node
    return get_min_value_node(root_node.left_child)

def delete_node(root_node, value):
    if not root_node:
        return root_node
    elif value < root_node.data:
        root_node.left_child = delete_node(root_node.left_child, value)
    elif value > root_node.data:
        root_node.right_child = delete_node(root_node.right_child, value)
    else:
        if root_node.left_child == None:
            temp = root_node.right_child
            root_node = None
            return temp
        if root_node.right_child == None:
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
    if balance > 1 and get_balance(root_node.left_child) < 0:
        root_node.left_child = left_rotate(root_node.left_child)
        return right_rotate(root_node)
    if balance < -1 and get_balance(root_node.right_child) <= 0:
        return left_rotate(root_node)
    if balance < -1 and get_balance(root_node.right_child) > 0:
        root_node.right_child = right_rotate(root_node.right_child)
        return left_rotate(root_node)
    return root_node

def delete_avl(root_node):
    root_node.data = None
    root_node.left_child = None
    root_node.right_child = None
    return "AVL Tree is successfully deleted"

def print_tree(root_node, level=0):
    if root_node:
        print_tree(root_node.left_child, level+1)
        print(" " * 4 * level + "->" + str(root_node.data))
        print_tree(root_node.right_child, level+1)

avl = AVLNode(30)
insert_node(avl, 40)
insert_node(avl, 20)
insert_node(avl, 50)
insert_node(avl, 45)
print_tree(avl)