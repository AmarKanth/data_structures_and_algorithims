"""
It is same as single linked list, last node stores the first node reference.
       10-->20-->30-->40-->None
None<--10<--20<--30<--40
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        temp_node = self.head
        while temp_node:
            yield temp_node
            temp_node = temp_node.next
    
    def insert_node(self, location, value):
        new_node = Node(value)
        if self.head == None:
            new_node.next = None
            new_node.prev = None
            self.head = new_node
            self.tail = new_node
        else:
            if location == 0:
                new_node.next = self.head
                new_node.prev = None
                self.head.prev = new_node
                self.head = new_node
            elif location == -1:
                new_node.next = None
                new_node.prev = self.tail
                self.tail.next = new_node
                self.tail = new_node
            else:
                temp_node = self.head
                index = 0
                while index < location - 1:
                    temp_node = temp_node.next
                    index += 1
                new_node.prev = temp_node
                new_node.next = temp_node.next
                temp_node.next = new_node
                if new_node.next:
                    new_node.next.prev = new_node
        
    def traverse(self):
        if self.head is None:
            return "DLL is not exist"
        temp_node = self.head
        while temp_node:
            print(temp_node.value)
            temp_node = temp_node.next
    
    def reverse_traverse(self):
        if self.head is None:
            return "DLL is not exist"
        temp_node = self.tail
        while temp_node:
            print(temp_node.value)
            temp_node = temp_node.prev
    
    def search(self, value):
        if self.head is None:
            return "DLL is not exist"
        temp_node = self.head
        while temp_node:
            if temp_node.value == value:
                return temp_node.value
            temp_node = temp_node.next
        return "value is not exist in the DLL"
    
    def delete(self, location):
        if self.head is None:
            return "DLL is not exist"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            else location not in [0,-1]:
                temp_node = self.head
                index = 0
                while index < location -1:
                    temp_node = temp_node.next
                    index += 1
                temp_node.next = temp_node.next.next
                temp_node.next.prev = temp_node
                return "Element is deleted successfully"
    
    def delete(self):
        if self.head is None:
            return "DLL is not exist"
        
        temp_node = self.head
        while temp_node:
            temp_node.prev = None
            temp_node = temp_node.next
        self.head = None
        self.tail = None
        return "DLL is successfully deleted"

def print_ddl(dll):
    res = []
    for node in dll:
        prev = node.prev.value if node.prev else None
        value = node.value
        next = node.next.value if node.next else None
        res.append((prev, value, next))
    print(res)

q = DoubleLinkedList()
print(q.create(5))
print([i.value for i in q])