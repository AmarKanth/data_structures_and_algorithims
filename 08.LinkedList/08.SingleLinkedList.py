"""
TimeComplexity is O(1)
SpaceComplexity is O(1)
"""
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

"""
            TimeComplexity      SpaceComplexity
insert      O(n)                O(1)
traverse    O(n)                O(1)
search      O(n)                O(1)
delete      O(n)                O(1)
deleteAll   O(1)                O(1)
"""
class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    def insert(self, value, location):
        """
        1. Insert new node, when there is no head
        2. Replace head with new node(@index 0)
        3. Replace tail with new node(@index -1)
        4. Insert new node at specific location
        """
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == -1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
                if tempNode == self.tail:
                    self.tail = newNode

    def traverse(self):
        if self.head == None:
            print("The Singly Linked List does not exist")
        else:
            tempNode = self.head
            while tempNode != None:
                print(tempNode.value)
                tempNode = tempNode.next
    
    def search(self, value):
        if self.head == None:
           return "The ssl does not exist"
        else:
            tempNode = self.head
            while tempNode != None:
                if tempNode.value == value:
                    return tempNode.value
                tempNode = tempNode.next
            return "The value does not exist in ssl"
    
    def delete(self, location):
        """
        1. Delete node at index 0(head)
        2. Delete node at index 0(head) if head and tail is same
        3. Delete node at index -1(tail)
        4. Delete node at index -1(tail) if head and tail is same
        3. Delete node at specific location
        """
        if self.head == None:
            print("The ssl does not exist")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    tempNode = self.head
                    while tempNode != None:
                        if tempNode.next == self.tail:
                            break
                        tempNode = tempNode.next
                    tempNode.next = None
                    self.tail = tempNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next
    
    def deleteAll(self):
        if self.head is None:
            print("The ssl does not exist")
        else:
            self.head = None
            self.tail = None

ssl = SLinkedList()
ssl.insert(1, 1)
ssl.insert(2, 1)
ssl.insert(3, 1)
ssl.insert(4, 1)
ssl.insert(0, 0)
ssl.insert(0, 3)
print([node.value for node in ssl])
ssl.traverse()
search = ssl.search(10)
print(f"search value is {search}")