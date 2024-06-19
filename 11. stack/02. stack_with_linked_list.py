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