class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

def preOrder(root):
    if root == None:
        return
    print (root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)

from queue import Queue

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def insert(self, val):
        newNode = Node(val)

        if self.root == None:
            self.root = newNode
            return "Successfully inserted"
        else:
            q = Queue()
            q.put(self.root)
            while not q.empty():
                rootNode = q.get()
                if val < rootNode.info:
                    if rootNode.left == None:
                        rootNode.left = newNode
                        return "Successfully inserted"
                    else:
                        q.put(rootNode.left)
                
                if val > rootNode.info:
                    if rootNode.right == None:
                        rootNode.right = newNode
                        return "Successfully inserted"
                    else:
                        q.put(rootNode.right)

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])

preOrder(tree.root)
