from queue import Queue


class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


def preOrderTraversal(rootNode):
    if rootNode != None:
        return 
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)


def inOrderTraversal(rootNode):
    if rootNode != None:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)


def postOrderTraversal(rootNode):
    if rootNode != None:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

    
def levelOrderTraversal(rootNode):
    if rootNode == None:
        return
    q = Queue()
    q.put(rootNode)

    while not q.empty():
        root = q.get()
        print(root.data)

        if root.leftChild != None:
            q.put(root.leftChild)
        
        if root.rightChild != None:
            q.put(root.rightChild)


def insertNode(rootNode, value):
    newNode = BinaryTree(value)

    if rootNode == None:
        rootNode = newNode
        return "Node successfully inserted"
    else:
        q = Queue()
        q.put(rootNode)
        while not q.empty():
            root = q.get()

            if root.leftChild != None:
                q.put(root.leftChild)
            else:
                root.leftChild = newNode
                return "Node successfully inserted"
            
            if root.rightChild != None:
                q.put(root.rightChild)
            else:
                root.rightChild = newNode
                return "Node successfully inserted"


def searchNode(rootNode, value):
    if rootNode == None:
        return "Binary Tree is not exist"
    else:
        q = Queue()
        q.put(rootNode)
        while not q.empty():
            root = q.get()
            if root.data == value:
                return "Success"
            if root.leftChild != None:
                q.put(root.leftChild)
            if root.rightChild != None:
                q.put(root.rightChild)
    return "Not Found"


newBT = BinaryTree("Drinks")
hot = BinaryTree("Hot")
cold = BinaryTree("Cold")
newBT.leftChild = hot
newBT.rightChild = cold

levelOrderTraversal(newBT)