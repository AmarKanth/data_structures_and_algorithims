"""
1. Stack is a data stracture that stores items in a last-in/first-out(LIFO method) manner.
2. random access is not possible in stack
3. if data size increase, takes time to access the first element.
"""

"""
stack with list
"""
class Stack:
    def __init__(self, maxSize):
        self.list = []
        self.maxSize = maxSize
    
    def __str__(self):
        self.list.reverse()
        values = [str(i) for i in self.list]
        return "\n".join(values)
    
    def isEmpty(self):
        if self.list == []:
            return True
        return False

    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        return False
    
    def push(self, value):
        if self.isFull():
            return "Stack is full"
        self.list.append(value)
        return self.list
    
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.list.pop()
    
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.list[len(self.list)-1]
    
    def delete(self):
        self.list = None
        return self.list

"""
stack with linked list
"""
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def all(self):
        all = []
        node = self.head
        while node:
            all.append(node.value)
            node = node.next
        else:
            return all

class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()
    
    def __str__(self):
        values = [str(i) for i in self.LinkedList.all()]
        return "\n".join(values)
    
    def isEmpty(self):
        if self.LinkedList.head == None:
            return True
        return False
    
    def push(self, value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node
        return self.LinkedList.all()
    
    def pop(self):
        node = self.LinkedList.head.value
        self.LinkedList.head = self.LinkedList.head.next
        return node
    
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.LinkedList.head.value
    
    def delete(self):
        self.LinkedList.head = None
        return self.LinkedList.head