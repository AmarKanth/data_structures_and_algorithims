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
        self.leftChild = None
        self.rightChild = None

newBT = TreeNode("Drinks")
leftChild = TreeNode("Hot")
tea = TreeNode('Tea')
coffee = TreeNode('Coffee')
leftChild.leftChild = tea
leftChild.rightChild = coffee
rightChild = TreeNode("Cold")
newBT.leftChild = leftChild
newBT.rightChild = rightChild

def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        q = Queue()
        q.put(rootNode)
        while not q.empty():
            root = q.get()
            print(root.data)
            if root.leftChild is not None:
                q.put(root.leftChild)
            if root.rightChild is not None:
                q.put(root.rightChild)

def insertNode(rootNode, value):
    newNode = TreeNode(value)

    if not rootNode:
        rootNode = newNode
        return "Node successfully inserted"
    else:
        q = Queue()
        q.put(rootNode)
        while not q.empty():
            root = q.get()
            if root.leftChild is not None:
                q.put(root.leftChild)
            else:
                root.leftChild = newNode
                return "Successfully Inserted"
            if root.rightChild is not None:
                q.put(root.rightChild)
            else:
                root.rightChild = newNode
                return "Successfully Inserted"

def searchNode(rootNode, value):
    if not rootNode:
        return "BT is not exist"
    else:
        q = Queue()
        q.put(rootNode)
        while not q.empty():
            root = q.get()
            if root.data == value:
                return "Success"
            if root.leftChild is not None:
                q.put(root.leftChild)
            if root.rightChild is not None:
                q.put(root.rightChild)
        return "Not Found"

def getDeepestNode(rootNode):
    if not rootNode:
        return
    else:
        deepestNode = None
        q = Queue()
        q.put(rootNode)
        while not q.empty():
            root = q.get()
            deepestNode = root.data
            if root.leftChild is not None:
                q.put(root.leftChild)
            if root.rightChild is not None:
                q.put(root.rightChild)
        return deepestNode

def deleteDeepestNode(rootNode, deepestNode):
    """
    1. If deepest node is root node make it None
    2. If deepest node is leftChild remove link between root and leftChild
    3. If deepest node is rightChild remove linke between root and rightChild
    """
    if not rootNode:
        return
    else:
        q = Queue()
        q.put(rootNode)
        while not q.empty():
            root = q.get()
            if root.data == deepestNode:
                root = None
                return
            if root.rightChild:
                if root.rightChild.data == deepestNode:
                    root.rightChild = None
                    return
                else:
                    q.put(root.rightChild)
            if root.leftChild:
                if root.leftChild.data == deepestNode:
                    root.leftChild = None
                    return
                else:
                    q.put(root.leftChild)

def deleteNodeBT(rootNode, value):
    """
    1. Find matched node
    2. Find Deepest node
    3. Replace matched node with deepest node
    4. Delete deepest node
    """
    if not rootNode:
        return "The BT doesnt exist"
    else:
        q = Queue()
        q.put(rootNode)
        while not q.empty():
            root = q.get()
            if root.data is value:
                deepestNode = getDeepestNode(rootNode)
                root.data = deepestNode
                deleteDeepestNode(rootNode, deepestNode)
                return "The node has been successfully deleted"
            if root.leftChild is not None:
                q.put(root.leftChild)
            if root.rightChild is not None:
                q.put(root.rightChild)
        return "Failed to delete the node"

def deleteBT(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "The BT has been successfully deleted"