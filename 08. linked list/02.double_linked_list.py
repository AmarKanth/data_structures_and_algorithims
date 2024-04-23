"""
TimeComplexity is O(1)
SpaceComplexity is O(1)
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

"""
                    TimeComplexity      SpaceComplexity
insert              O(n)                O(1)
reverse_traverse    O(n)                O(1)
search              O(n)                O(1)
delete              O(n)                O(1)
delete_all          O(n)                O(1)
"""
class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        temp_node = self.head
        while temp_node:
            yield temp_node
            temp_node = temp_node.next
    
    def insert(self, location, value):
        new_node = Node(value)
        if self.head == None:
            new_node.prev = None
            new_node.next = None
            self.head = new_node
            self.tail = new_node
            return "Node has been successfully inserted"
        
        if location == 0:
            new_node.prev = None
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            return "Node has been successfully inserted"
        
        if location != 0:
            temp_node = self.head
            index = 0
            while index < location - 1:
                temp_node = temp_node.next
                index += 1
            if self.tail == temp_node:
                new_node.prev = self.tail
                new_node.next = None
                self.tail.next = new_node
                self.tail = new_node
            else:
                new_node.prev = temp_node
                new_node.next = temp_node.next
                temp_node.next = new_node
                new_node.next.prev = new_node
            return "Node has been successfully inserted"
    
    def reverse_traverse(self):
        if self.head == None:
            return "DLL is doesnt exist"
        temp_node = self.tail
        while temp_node:
            yield temp_node.value
            temp_node = temp_node.prev
    
    def search(self, value):
        if self.head == None:
            return "DLL is doesnt exist"
        temp_node = self.head
        while temp_node:
            if temp_node.value == value:
                return temp_node.value
            temp_node = temp_node.next
        return "value is not exist in the DLL"
    
    def delete(self, location):
        if self.head == None:
            return "DLL is doesnt exist"

        if location == 0:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
            return "Node has been successfully deleted"
        
        if location != 0:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                temp_node = self.head
                index = 0
                while index < location - 1:
                    temp_node = temp_node.next
                    index += 1
                if self.tail == temp_node.next:
                    self.tail = self.tail.prev
                    self.tail.next = None
                else:
                    temp_node.next = temp_node.next.next
                    temp_node.next.prev = temp_node
            return "Node has been successfully deleted"
    
    def delete_all(self):
        if self.head == None:
            return "DLL is doesnt exist"
        temp_node = self.head
        while temp_node:
            temp_node.prev = None
            temp_node = temp_node.next
        self.head = None
        self.tail = None
        return "DLL is successfully deleted"

def print_dll(dll):
    res = []
    for node in dll:
        prev = node.prev.value if node.prev else None
        value = node.value
        next = node.next.value if node.next else None
        res.append((prev, value, next))
    return res

dll = DoubleLinkedList()
dll.insert(0,0)
dll.insert(1,1)
dll.insert(2,2)
dll.insert(3,3)
dll.delete(2)
res = print_dll(dll)
print(res)
