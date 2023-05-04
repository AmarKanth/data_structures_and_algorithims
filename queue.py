"""
1. queue is datastracure that store items in FIFO(first in first out) manner.
"""

"""
Queue with list
"""
class Queue:
    def __init__(self):
        self.items = []
    
    def __str__(self):
        values = [str(i) for i in self.items]
        return " ".join(values)
    
    def isEmpty(self):
        if self.items == []:
            return True
        return False
    
    def enqueue(self, value):
        self.items.append(value)
        return self.items
    
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.items.pop(0)
    
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.items[0]
    
    def delete(self):
        self.items = None

q = Queue()
print(q.isEmpty())
print(q.enqueue(1))
print(q.dequeue())
print(q.peek())
print(q.delete())

"""
Circular Queue with list
"""
class Queue:
    def __init__(self, maxSize):
        self.items = maxSize * [None]
        self.maxSize = maxSize
        self.top = -1
        self.start = -1
    
    def __str__(self):
        values = [str(i) for i in self.items]
        return " ".join(values)
    
    def isFull(self):
        if self.top + 1 == self.start:
            return True
        
        if self.start == 0 and self.top + 1 == self.maxSize:
            return True

        return False
    
    def isEmpty(self):
        if self.top == -1:
            return True
        return False
    
    def enqueue(self, value):
        if self.isFull():
            return "Q is full"
        else:
            if self.top + 1 == self.maxSize:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.items[self.top] = value
        return self.items
    
    def dequeue(self):
        if self.isFull():
            return "Q is full"
        else:
            firstElement = self.items[self.start]
            start = self.start
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start + 1 == self.top:
                self.start = 0
            else:
                self.start += 1
            self.items[start] = None
            return firstElement
        
    def peek(self):
        if self.isFull():
            return "Q is empty"
        else:
            return self.items[self.start]
    
    def delete(self):
        self.items = self.maxSize * [None]
        self.start = -1
        self.top = -1

q = Queue(3)
print(q.isFull())

"""
Q with linked list
"""
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
    
    def isEmpty(self):
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
        if self.isEmpty():
            return "Q is empty"
        else:
            tempNode = self.linkedlist.head
            if self.linkedlist.head == self.linkedlist.tail:
                self.linkedlist.head = None
                self.linkedlist.tail = None
            else:
                self.linkedlist.head = self.linkedlist.head.next
        return tempNode
        
    def peek(self):
        if self.linkedlist.head == None:
            return "Q is empty"
        else:
            return self.linkedlist.head
    
    def delete(self):
        self.linkedlist.head = None
        self.linkedlist.tail = None

"""
Queue in collection module

1. deque
2. append
3. popleft
4. clear
"""
from collections import deque
q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q)
q.append(4)
print(q)
q.popleft()
print(q)
q.clear()
print(q)

"""
Queue module
"""
from queue import Queue
q = Queue(maxsize=3)
q.put(1)
q.put(2)
q.put(3)
print(q.qsize())
print(q.empty())
print(q.full())
print(q.get())

"""
Queue in Multiporocessing Module
"""
from multiprocessing import Queue

q = Queue(maxsize=3)
print(q.put(1))
print(q.get())
print(q.qsize())