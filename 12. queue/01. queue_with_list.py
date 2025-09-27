"""
queue is datastracure that store items in FIFO(first in first out) manner.
"""

class Queue:
    def __init__(self):
        self.elements = []
    
    def __str__(self):
        values = [str(i) for i in self.elements]
        return " ".join(values)
    
    def is_empty(self):
        if self.elements == []:
            return True
        return False
    
    def enqueue(self, value):
        self.elements.append(value)
        return self.elements
    
    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.elements.pop(0)
    
    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        return self.elements[0]
    
    def delete(self):
        self.elements = None

q = Queue()
print(q.is_empty())
print(q.enqueue(1))
print(q.dequeue())
print(q.peek())
print(q.delete())
