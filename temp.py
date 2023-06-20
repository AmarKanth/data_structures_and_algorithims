class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insertSSL(self, value, location):
        """
        1. Insert new node, when there is no head
        2. Replace head with new node(@index 0)
        3. Replace tail with new node(@index -1)
        4. Insert new node at specific location
        """
        newNode = Node(value)

        if self.head is None:
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
    
    def traversalSSL(self):
        node = self.head
        index = 0
        while node is not None:
            print((index, node.value))
            index += 1
            node = node.next

ssl = SingleLinkedList()
ssl.insertSSL(3, 0)
ssl.insertSSL(1, 1)
ssl.insertSSL(4, 2)
ssl.insertSSL(0, 0)
ssl.traversalSSL()