class Heap:
    def __init__(self, size):
        self.customList = (size+1) * [None]
        self.heapSize = 0
        self.maxSize = size + 1
    
"""
TimeComplexity is O(1)
SpaceComplexity is O(1)
"""
def peakofHeap(rootNode):
    if not rootNode:
        return
    return rootNode.customList[1]

"""
TimeComplexity is O(1)
SpaceComplexity is O(1)
"""
def sizeofHeap(rootNode):
    if not rootNode:
        return
    return rootNode.heapSize

"""
TimeComplexity is O(n)
SpaceComplexity is O(1)
"""
def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    for idx in range(1, rootNode.heapSize+1):
        print(rootNode.customList[idx])

def heapifyTreeInsert(rootNode, index, heapType):
    parentIndex = int(index/2)
    if index <= 1:
        return
    
    # Performed element swapping for sorting.
    if heapType == "Min":
        if rootNode.customList[index] < rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
            heapifyTreeInsert(rootNode, parentIndex, heapType)
    if heapType == "Max":
        if rootNode.customList[index] > rootNode.customList[parentIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
            heapifyTreeInsert(rootNode, parentIndex, heapType)

"""
TimeComplexity is O(LogN)
SpaceComplexity is O(LogN)
"""
def insertNode(rootNode, nodeValue, heapType):
    if rootNode.heapSize + 1 == rootNode.maxSize:
        return "Binary Heap is full"
    rootNode.customList[rootNode.heapSize + 1] = nodeValue
    rootNode.heapSize += 1
    # Heapifying will be performed from last node to rootnode
    heapifyTreeInsert(rootNode, rootNode.heapSize, heapType)
    return "The value is successfully inserted"

def heapifyTreeExtract(rootNode, index, heapType):
    leftIndex = index * 2
    rightIndex = index * 2 + 1
    swapChild = 0

    if rootNode.heapSize < leftIndex:
        return 
    # If current node has only leftchild and leftchild is the last child
    elif rootNode.heapSize == leftIndex:
        if heapType == "Min":
            if rootNode.customList[index] > rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return
        else:
            if rootNode.customList[index] < rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return
    # If current node has right and left child
    else:
        if heapType == "Min":
            # Find Min value between left and right childs
            if rootNode.customList[leftIndex] < rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[swapChild]
            rootNode.customList[swapChild] = temp
        else:
            # Find Max value between left and right childs
            if rootNode.customList[leftIndex] > rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[swapChild]
            rootNode.customList[swapChild] = temp
    heapifyTreeExtract(rootNode, swapChild, heapType)

"""
TimeComplexity is O(LogN)
SpaceComplexity is O(LogN)
"""
def extractNode(rootNode, heapType):
    if rootNode.heapSize == 0:
        return
    else:
        # Binary Heap allowed to extract rootNode
        extractedNode = rootNode.customList[1]
        rootNode.customList[1] = rootNode.customList[rootNode.heapSize]
        rootNode.customList[rootNode.heapSize] = None
        rootNode.heapSize -= 1
        # Heapifying will be performed from rootNode
        heapifyTreeExtract(rootNode, 1, heapType)
        return extractedNode
    
"""
TimeComplexity is O(1)
SpaceComplexity is O(1)
"""
def deleteBH(rootNode):
    rootNode.customList = None

newBinaryHeap = Heap(5)
insertNode(newBinaryHeap, 4, "Max")
insertNode(newBinaryHeap, 5, "Max")
insertNode(newBinaryHeap, 2, "Max")
insertNode(newBinaryHeap, 1, "Max")
levelOrderTraversal(newBinaryHeap)