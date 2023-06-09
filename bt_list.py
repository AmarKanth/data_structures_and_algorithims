"""
1. Trees are non-linear data stractures.
2. In binary tree each node has most two children.
"""

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
Types Of BinaryTree

1. Full Binary Tree     :-  Each node should have 2 children or zero children
2. Perfect Binary Tree  :-  All the non-leaf nodes has two children and are at the same level(depth), 
                            all leaf nodes has zero children and are the same level(depth)
3. Complete Binary Tree :-  All levels are completely filled except last level.
4. Balanced Binary Tree :-  All the leaf nodes are in same level(depth)
"""

"""
Types of Traversal Methods

preorder    :- All-LeftNodes --> All-RightNodes
inorder     :- LeftNode --> RootNode --> RightNode
postorder   :- LeftNode --> RightNode --> RootNode
levelorder  :- Depth-1 --> Depth-2 --- Till-LastNode
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
newBT.deleteBT()