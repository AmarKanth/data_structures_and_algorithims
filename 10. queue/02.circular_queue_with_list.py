class Queue:
    def __init__(self, max_size):
        self.items = max_size * [None]
        self.max_size = max_size
        self.top = -1
        self.start = -1
    
    def __str__(self):
        values = [str(i) for i in self.items]
        return " ".join(values)
    
    def is_full(self):
        if self.top + 1 == self.start:
            return True
        if self.start == 0 and self.top + 1 == self.max_size:
            return True
        return False
    
    def is_empty(self):
        if self.top == -1:
            return True
        return False
    
    def enqueue(self, value):
        if self.is_full():
            return "Q is full"
        else:
            if self.top + 1 == self.max_size:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.items[self.top] = value
        return self.items
    
    def dequeue(self):
        if self.is_full():
            return "Q is full"
        else:
            first_element = self.items[self.start]
            start = self.start
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start + 1 == self.top:
                self.start = 0
            else:
                self.start += 1
            self.items[start] = None
            return first_element
        
    def peek(self):
        if self.is_full():
            return "Q is empty"
        else:
            return self.items[self.start]
    
    def delete(self):
        self.items = self.max_size * [None]
        self.start = -1
        self.top = -1

q = Queue(3)
print(q.is_full())