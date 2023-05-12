class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
    
newBT = TreeNode("Drinks")
hot = TreeNode("Hot")
cold = TreeNode("Cold")
newBT.leftChild = hot
newBT.rightChild = cold

tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
hot.leftChild = tea
hot.rightChild = coffee

cola = TreeNode("Cola")
cold.leftChild = cola

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


def deleteDeepestNode(rootNode, node):
    if not rootNode:
        return
    else:
        q = Queue()
        q.put(rootNode)
        while not q.empty():
            root = q.get()
            if root.data == node:
                root = None
                return
            if root.leftChild:
                if root.leftChild.data == node:
                    root.leftChild = None
                    return
                else:
                    q.put(root.leftChild)
            if root.rightChild:
                if root.rightChild.data == node:
                    root.rightChild = None
                    return
                else:
                    q.put(root.rightChild)


def deleteNode(rootNode, node):
    if not rootNode:
        return "BT is not exist"
    else:
        q = Queue()
        q.put(rootNode)
        while not q.empty():
            root = q.get()
            if root.data == node:
                dNode = getDeepestNode(rootNode)
                root.data = dNode
                print(root.data)
                print("----------------")
                deleteDeepestNode(rootNode, dNode)
                return "Node is deleted successfully"
            if root.leftChild is not None:
                q.put(root.leftChild)
            if root.rightChild is not None:
                q.put(root.rightChild)

# deleteNode(newBT, "Tea")
# levelOrderTraversal(newBT)
res = getDeepestNode(newBT)
print(res)