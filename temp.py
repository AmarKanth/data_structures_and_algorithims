class AVLNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1


def preOrdertreversal(rootNode):
    if not rootNode:
        return 
    balance = getBalance(rootNode)
    print(f"{rootNode.data}--{rootNode.height}--{balance}")
    preOrdertreversal(rootNode.leftChild)
    preOrdertreversal(rootNode.rightChild)


def getHeight(rootNode):
    if not rootNode:
        return 0
    return rootNode.height


def getBalance(rootNode):
    if not rootNode:
        return 0
    return getHeight(rootNode.leftChild) - getHeight(rootNode.rightChild)


def insertNode(rootNode, nodeValue):
    if not rootNode:
        return AVLNode(nodeValue)
    if nodeValue < rootNode.data:
        rootNode.leftChild = insertNode(rootNode.leftChild, nodeValue)
    else:
        rootNode.rightChild = insertNode(rootNode.rightChild, nodeValue)
    
    rootNode.height = 1 + max(getHeight(rootNode.leftChild), getHeight(rootNode.rightChild))
    balance = getBalance(rootNode)
    return rootNode


newAVL = AVLNode(30)
newAVL = insertNode(newAVL, 25)
newAVL = insertNode(newAVL, 35)
newAVL = insertNode(newAVL, 20)
newAVL = insertNode(newAVL, 15)
preOrdertreversal(newAVL)