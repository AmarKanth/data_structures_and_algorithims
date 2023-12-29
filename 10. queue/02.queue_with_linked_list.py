class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __str__(self):
        return self.value

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

class Queue:
    def __init__(self):
        self.linkedlist = LinkedList()
    
    def __str__(self):
        values = [str(i) for i in self.items]
        return " ".join(values)
    
    def is_empty(self):
        if self.linkedlist.head == None:
            return True
        return False
    
    def enqueue(self, value):
        node = Node(value)
        if self.linkedlist.head == None:
            self.linkedlist.head = node
            self.linkedlist.tail = node
        else:
            self.linkedlist.tail.next = node
            self.linkedlist.tail = node
    
    def dequeue(self):
        if self.is_empty():
            return "Q is empty"
        else:
            temp_node = self.linkedlist.head
            if self.linkedlist.head == self.linkedlist.tail:
                self.linkedlist.head = None
                self.linkedlist.tail = None
            else:
                self.linkedlist.head = self.linkedlist.head.next
        return temp_node
        
    def peek(self):
        if self.linkedlist.head == None:
            return "Q is empty"
        else:
            return self.linkedlist.head
    
    def delete(self):
        self.linkedlist.head = None
        self.linkedlist.tail = None