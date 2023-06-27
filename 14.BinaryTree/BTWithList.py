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
        for idx in range(1, self.lastUsedIndex+1):
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