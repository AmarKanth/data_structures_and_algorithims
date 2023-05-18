class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


"""
TimeComplexity  O(logn)
SpaceComplexity O(logn)
"""
def insertNode(rootNode, nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.leftChild, nodeValue)
    else:
        if nodeValue > rootNode.data:
            if rootNode.rightChild is None:
                rootNode.rightChild = BSTNode(nodeValue)
            else:
                insertNode(rootNode.rightChild, nodeValue)


def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)


"""
It access the elements in ascending order
"""
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


"""
TimeComplexity O(logN)
SpaceComplexity O(logN)
"""
def searchNode(rootNode, nodeValue):
    if rootNode.data == nodeValue:
        print("Value is found")
    elif nodeValue < rootNode.data:
        if rootNode.data == nodeValue:
            print("Value is found")
        else:
            searchNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.data == nodeValue:
            print("Value is found")
        else:
            searchNode(rootNode.rightChild, nodeValue)

newBST = BSTNode(None)