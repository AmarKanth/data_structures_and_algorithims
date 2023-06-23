"""
Basic Tree
"""
class TreeNode:
    def __init__(self, data, children=[]):
        self.data = data
        self.children = children
    
    def __str__(self, level=0):
        ret = " " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level+1)
        return ret
    
    def addChild(self, TreeNode):
        self.children.append(TreeNode)

tree = TreeNode("Drinks", [])
cold = TreeNode("Cold", [])
hot = TreeNode("Hot", [])
tree.addChild(cold)
tree.addChild(hot)
tea = TreeNode("Tea", [])
coffee = TreeNode("Coffee", [])
cola = TreeNode("Cola", [])
fanta = TreeNode("Fanta", [])
cold.addChild(cola)
cold.addChild(fanta)
hot.addChild(tea)
hot.addChild(coffee)
print(tree)


"""
Binary Tree With List
"""
class BinaryTree:
    """
    TimeComplexity is O(1)
    SpaceComplexity is O(1)
    """
    def __init__(self, size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size
    
    """
    TimeComplexity is O(1)
    SpaceComplexity is O(1)
    """
    def insertNode(self, value):
        if self.lastUsedIndex + 1 == self.maxSize:
            return "The Binary Tree is full"
        self.customList[self.lastUsedIndex+1] = value
        self.lastUsedIndex += 1
        return "The value has been successfully inserted"
    
    """
    TimeComplexity is O(n)
    SpaceComplexity is O(1)
    """
    def searchNode(self, nodeValue):
        for idx in range(self.lastUsedIndex):
            if self.customList[idx] == nodeValue:
                return "Success"
        return "Not Found"
    
    """
    TimeComplexity is O(n)
    SpaceComplexity is O(n)
    """
    def preOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        print(self.customList[index])
        self.preOrderTraversal(index*2)
        self.preOrderTraversal(index*2+1)
    
    """
    TimeComplexity is O(n)
    SpaceComplexity is O(n)
    """
    def inOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        self.inOrderTraversal(index*2)
        print(self.customList[index])
        self.inOrderTraversal(index*2+1)
    
    """
    TimeComplexity is O(n)
    SpaceComplexity is O(n)
    """
    def postOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        self.postOrderTraversal(index*2)
        self.postOrderTraversal(index*2+1)
        print(self.customList[index])
    
    """
    TimeComplexity is O(n)
    SpaceComplexity is O(1)
    """
    def levelOrderTraversal(self, index):
        for idx in range(index, self.lastUsedIndex+1):
            print(self.customList[idx])
    
    """
    TimeComplexity is O(n)
    SpaceComplexity is O(1)
    """
    def deleteNode(self, value):
        if self.lastUsedIndex == 0:
            return "There is no node to delete"
        for idx in range(1, self.lastUsedIndex+1):
            if self.customList[idx] == value:
                self.customList[idx] = self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex] = None
                self.lastUsedIndex -= 1
                return "The node has been successfully deleted"
    
    """
    TimeComplexity is O(1)
    SpaceComplexity is O(1)
    """
    def deleteBT(self):
        self.customList = None
        return "The BT has been successfully deleted"

newBT = BinaryTree(8)
newBT.insertNode("Drinks")
newBT.insertNode("Hot")
newBT.insertNode("Cold")
newBT.insertNode("Tea")
newBT.insertNode("Coffee")


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