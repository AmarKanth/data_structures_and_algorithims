"""
queue is datastracure that store items in FIFO(first in first out) manner.
"""

class Queue:
    def __init__(self):
        self.items = []
    
    def __str__(self):
        values = [str(i) for i in self.items]
        return " ".join(values)
    
    def is_empty(self):
        if self.items == []:
            return True
        return False
    
    def enqueue(self, value):
        self.items.append(value)
        return self.items
    
    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.items.pop(0)
    
    def peek(self):
        if self.is_empty():
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