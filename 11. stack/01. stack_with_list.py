"""
1. Stack is a data stracture that stores items in a last-in/first-out(LIFO method) manner.
2. random access is not possible in stack
3. if data size increase, takes time to access the first element.
"""

class Stack:
    def __init__(self, max_size):
        self.list = []
        self.max_size = max_size
    
    def __str__(self):
        self.list.reverse()
        values = [str(i) for i in self.list]
        return "\n".join(values)
    
    def is_empty(self):
        if self.list == []:
            return True
        return False

    def is_full(self):
        if len(self.list) == self.max_size:
            return True
        return False
    
    def push(self, value):
        if self.is_full():
            return "Stack is full"
        self.list.append(value)
        return self.list
    
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.list.pop()
    
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.list[len(self.list)-1]
    
    def delete(self):
        self.list = None
        return self.list
