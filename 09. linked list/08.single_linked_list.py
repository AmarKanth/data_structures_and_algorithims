"""
TimeComplexity is O(1)
SpaceComplexity is O(1)
"""
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

"""
            TimeComplexity      SpaceComplexity
insert      O(n)                O(1)
traverse    O(n)                O(1)
search      O(n)                O(1)
delete      O(n)                O(1)
deleteAll   O(1)                O(1)
"""
class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    def insert(self, value, location):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            if location == 0:
                new_node.next = self.head
                self.head = new_node
            elif location == -1:
                new_node.next = None
                self.tail.next = new_node
                self.tail = new_node
            else:
                temp_node = self.head
                index = 0
                while index < location - 1:
                    if temp_node.next:
                        temp_node = temp_node.next
                    index += 1
                next_node = temp_node.next
                temp_node.next = new_node
                new_node.next = next_node
                if temp_node == self.tail:
                    self.tail = new_node

    def traverse(self):
        if self.head == None:
            print("The Singly Linked List does not exist")
        else:
            temp_node = self.head
            while temp_node != None:
                print(temp_node.value)
                temp_node = temp_node.next
    
    def search(self, value):
        if self.head == None:
           return "The ssl does not exist"
        else:
            temp_node = self.head
            while temp_node != None:
                if temp_node.value == value:
                    return temp_node.value
                temp_node = temp_node.next
            return "The value does not exist in ssl"
    
    def delete(self, location):
        if self.head == None:
            print("The ssl does not exist")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    temp_node = self.head
                    while temp_node != None:
                        if temp_node.next == self.tail:
                            break
                        temp_node = temp_node.next
                    temp_node.next = None
                    self.tail = temp_node
            else:
                temp_node = self.head
                index = 0
                while index < location - 1:
                    temp_node = temp_node.next
                    index += 1
                next_node = temp_node.next
                temp_node.next = next_node.next
    
    def delete_all(self):
        if self.head is None:
            print("The ssl does not exist")
        else:
            self.head = None
            self.tail = None

ssl = SLinkedList()
ssl.insert(1, 1)
ssl.insert(2, 1)
ssl.insert(3, 1)
ssl.insert(4, 1)
ssl.insert(0, 0)
ssl.insert(0, 3)
print([node.value for node in ssl])
ssl.traverse()
search = ssl.search(10)
print(f"search value is {search}")