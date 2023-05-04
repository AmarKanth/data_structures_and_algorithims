"""
Binary Tree Traversal(Linked List)
"""
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

"""
Time Complexity is O(n)
Space Complexity is O(n) becuase we are using the stack memory
"""
def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

preOrderTraversal(newBT)

"""
Time Complexity is O(n)
Space Complexity is O(n)
"""
def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

inOrderTraversal(newBT)

"""
Time Complexity is O(n)
Space Complexity is O(n)
"""
def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

postOrderTraversal(newBT)

"""
Time Complexity is O(n)
Space Complexity is O(n)
"""
from queue import Queue
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

levelOrderTraversal(newBT)

"""
Searching For Node(Linked List)
"""
"""
Searching for element in Binray Tree gives better performance with levelOrderTraversal,
because levelOrderTraversal uses Queue and other traversal methods uses stack.
"""
"""
Time Complexity O(n)
Space Complexity O(n)
"""
from queue import Queue
def searchBT(rootNode, node):
    if not rootNode:
        return "BT is not exist"
    else:
        q = Queue()
        q.put(rootNode)
        while not q.empty():
            root = q.get()
            if root.data == node:
                return "Success"
            if root.leftChild is not None:
                q.put(root.leftChild)
            if root.rightChild is not None:
                q.put(root.rightChild)
        return "Not Found"

res = searchBT(newBT, "Tea")
print(res)

"""
Insert New Node
"""
"""
Time Complexity O(n)
Space Complexity O(n)
"""
from queue import Queue
def insertBT(rootNode, newNode):
    if not rootNode:
        rootNode = newNode
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

newNode = TreeNode("Cola")
res = insertBT(newBT, newNode)
print(res)

"""
Delete Node(Linked List)
"""
"""
TimeComplexity is O(n)
SpaceComplexity is O(n)
"""
from queue import Queue

def getDeepestNode(rootNode):
    if not rootNode:
        return
    else:
        q = Queue()
        q.put(rootNode)
        while not q.empty():
            root = q.get()
            if root.leftChild is not None:
                q.put(root.leftChild)
            if root.rightChild is not None:
                q.put(root.rightChild)
        deepestNode = root.data
        return deepestNode

def deleteDeepestNode(rootNode, dNode):
    if not rootNode:
        return
    else:
        q = Queue()
        q.put(rootNode)
        while not q.empty():
            root = q.get()
            if root.data is dNode:
                root = None
                return
            if root.rightChild:
                if root.rightChild.data is dNode:
                    root.rightChild = None
                    return
                else:
                    q.put(root.rightChild)
            if root.leftChild:
                if root.leftChild.data is dNode:
                    root.leftChild = None
                    return
                else:
                    q.put(root.leftChild)

def deleteNodeBT(rootNode, node):
    if not rootNode:
        return "The BT doesnt exist"
    else:
        q = Queue()
        q.put(rootNode)
        while not q.empty():
            root = q.get()
            if root.data is node:
                dNode = getDeepestNode(rootNode)
                root.data = dNode
                deleteDeepestNode(rootNode, dNode)
                return "The node has been successfully deleted"
            if root.leftChild is not None:
                q.put(root.leftChild)
            if root.rightChild is not None:
                q.put(root.rightChild)
        return "Failed to delete the node"

deleteNodeBT(newBT, "Tea")


"""
Delete Enitre Binary Tree
"""
"""
TimeComplexity is O(1)
SpaceComplexity is O(1)
"""

def deleteBT(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "The BT has been successfully deleted"

deleteBT(newBT)