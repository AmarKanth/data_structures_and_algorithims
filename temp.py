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
    heapifyTreeInsert(rootNode, rootNode.heapSize, heapType)
    return "The value is successfully inserted"


newBinaryHeap = Heap(5)
insertNode(newBinaryHeap, 20, "Max")
insertNode(newBinaryHeap, 10, "Max")
insertNode(newBinaryHeap, 5, "Max")
levelOrderTraversal(newBinaryHeap)