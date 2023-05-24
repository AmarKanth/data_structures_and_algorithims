from queue import Queue


class AVLNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1


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


"""
Insertion Conditions in AVL
1. Rotation is not Required(Insertion is same as in BT)
2. Rotation is Required(When left and right subtree depth difference is morethan one)

1. LL Condition
2. LR Condition
3. RR Condition
4. RL Condition
"""
newAVL = AVLNode(10)