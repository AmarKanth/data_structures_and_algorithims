"""
Each node has two references. first reference is previous value and second reference is next value.
"""

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node.next == self.head:
                break
    
    def create(self, value):
        node = Node(value)
        node.next = node
        self.head = node
        self.tail = node
        return "CSLL created"
    
    def insert(self, value, location):
        if self.head is None:
            return "CSLL is not exist"
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            elif location == -1:
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                tempNode.next = newNode
                newNode.next = tempNode.next
                return "New node has been successfully inserted"
        
    def traversal(self):
        if self.head is None:
            print("CSLL is not exist")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    break
    
    def search(self, value):
        if self.head is None:
            print("CSLL is not exist")
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == value:
                    return tempNode.value
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    return "The node doesnt exist in the CSLL"
    
    def delete(self, location):
        if self.head is None:
            print("CSLL is not exist")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location == 1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node == self.tail:
                            break
                        node = node.next
                    node.next = self.head
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < (location -1):
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next
        
    def delete_all(self):
        self.head = None
        self.tail.next = None
        self.tail = None

csll = CircularLinkedList()
csll.create(1)
csll.insert(0,0)
# csll.insert(2,1)
# csll.insert(3,1)
# csll.insert(2,2)
print([i.value for i in csll])