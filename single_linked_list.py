"""
Linked list is a form of a sequential collection and it does not have to be in order.
A linked list made up of independent nodes that may contain any type of data and 
each node has a reference to the next in the link.
"""

"""
1. Elements in linked list are independent. 
Elements in list will be replaced with next element if delete the element.
2. in case of delete element in list elements will be rearrange the indicies and memory slots.
In linked list need to update the references. which is effiecient than the list.
3. we cant randomly fetch the element in linked list, need to itarate all the elements.
"""

"""
1. Singular Linked List :- each node contains value and reference, 
head and tail nodes stores only reference to the next node.

2. Circular Singly Linked List :- it is same as single linked list, 
last node stores the first node reference.

3. Doubly Linked List :- each node has two references. 
first reference is previous value and second reference is next value.

4. Circular Doubly Linked List :- it is same as doubly linked list,
last node stores the reference of previous node and first node.
"""


"""
Time to create single linked list is 0(1)
"""
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    def insertSLL(self, value, location):
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
        
    def traverseSLL(self):
        if self.head is None:
            print("The Singly Linked List does not exist")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next
    
    def searchSLL(self, nodeValue):
        if self.head is None:
           return "The list does not exist"
        else:
            node = self.head
            while node is not None:
                if node.value == nodeValue:
                    return node.value
                node = node.next
            return "The value does not exist in this list"
    
    def deleteNode(self, location):
        if self.head is None:
            print("The SLL does not exist")
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
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next
    
    def deleteEntireSLL(self):
        if self.head is None:
            print("The SLL does not exist")
        else:
            self.head = None
            self.tail = None

singleLinkedList = SLinkedList()
singleLinkedList.insertSLL(1, 1)
singleLinkedList.insertSLL(2, 1)
singleLinkedList.insertSLL(3, 1)
singleLinkedList.insertSLL(4, 1)
singleLinkedList.insertSLL(0, 0)
singleLinkedList.insertSLL(0, 3)
print([node.value for node in singleLinkedList])
singleLinkedList.traverseSLL()
search = singleLinkedList.searchSLL(10)
print(f"search value is {search}")