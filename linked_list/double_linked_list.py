class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    def create(self, value):
        node = Node(value)
        node.next = None
        node.prev = None
        self.head = node
        self.tail = node
        return 'DLL created'
    
    def insert(self, value, location):
        if self.head is None:
            return "DLL is not exist"
        
        newNode = Node(value)

        if location == 0:
            newNode.prev = None
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        
        if location == -1:
            newNode.next = None
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
        
        if location not in [0,-1]:
            tempNode = self.head
            index = 0
            while index < location - 1:
                tempNode = tempNode.next
                index += 1
            newNode.next = tempNode.next
            newNode.prev = tempNode
            newNode.next.prev = newNode
            tempNode.next = newNode
        
    def traverse(self):
        if self.head is None:
            return "DLL is not exist"
        tempNode = self.head
        while tempNode:
            print(tempNode.value)
            tempNode = tempNode.next
    
    def reverseTraverse(self):
        if self.head is None:
            return "DLL is not exist"
        tempNode = self.tail
        while tempNode:
            print(tempNode.value)
            tempNode = tempNode.prev
    
    def search(self, value):
        if self.head is None:
            return "DLL is nto exist"
        tempNode = self.tail
        while tempNode:
            if tempNode.value == value:
                return tempNode.value
            tempNode = tempNode.next
        return "value is not exist in the DLL"
    
    def delete(self, location):
        if self.head is None:
            return "DLL is not exist"
        
        if location == 0:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
        
        if location == -1:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None
        
        if location not in [0,-1]:
            currentNode = self.head
            index = 0
            while index < location -1:
                currentNode = currentNode.next
                index += 1
            currentNode.next = currentNode.next.next
            currentNode.next.prev = currentNode
            return "Element is deleted successfully"
    
    def delete(self):
        if self.head is None:
            return "DLL is not exist"
        
        tempNode = self.head
        while tempNode:
            tempNode.prev = None
            tempNode = tempNode.next
        self.head = None
        self.tail = None
        return "DLL is successfully deleted"

q = DoubleLinkedList()
print(q.create(5))
print([i.value for i in q])