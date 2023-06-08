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


newBinaryHeap = Heap(5)