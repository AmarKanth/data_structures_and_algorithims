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
search      O(n)                O(1)
delete      O(n)                O(1)
delete_all  O(1)                O(1)
"""
class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    def insert(self, location, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            return "Node successfully inserted"

        if location == 0:
            new_node.next = self.head
            self.head = new_node
            return "Node successfully inserted"
        
        if location != 0:
            temp_node = self.head
            index = 0
            while index < location - 1:
                temp_node = temp_node.next
                index += 1
            if self.tail == temp_node:
                self.tail.next = new_node
                self.tail = new_node
            else:
                next_node = temp_node.next
                temp_node.next = new_node
                new_node.next = next_node
            return "Node successfully inserted"
    
    def search(self, value):
        if self.head == None:
           return "SLL does not exist"
        temp_node = self.head
        while temp_node:
            if temp_node.value == value:
                return temp_node.value
            temp_node = temp_node.next
        return "The value does not exist in ssl"
    
    def delete(self, location):
        if self.head == None:
            return "SLL is doesnt exist"

        if self.head == self.tail:
            self.head = None
            self.tail = None
            return "Node successfully deleted from sll"
        
        if location == 0:
            self.head = self.head.next
            return "Node successfully deleted from sll"
        
        if location != 0:
            temp_node = self.head
            index = 0
            while index < location - 1:
                temp_node = temp_node.next
                index += 1
            if self.tail == temp_node.next:
                temp_node.next = None
                self.tail = temp_node
            else:
                next_node = temp_node.next
                temp_node.next = next_node.next
            return "Node successfully deleted from sll"
    
    def delete_all(self):
        if self.head == None:
            return "SLL does not exist"
        self.head = None
        self.tail = None
        return "SLL is successfully deleted"

def print_sll(sll):
    res = []
    for node in sll:
        value = node.value if node else None
        next = node.next.value if node.next else None
        res.append((value, next))
    return res

ssl = SingleLinkedList()
ssl.insert(1, 1)
ssl.insert(2, 1)
ssl.insert(3, 1)
ssl.insert(4, 1)
ssl.insert(0, 0)
ssl.insert(0, 3)
search = ssl.search(10)
print(f"search value is {search}")


"""
create linked list for courses
courses = [('d','a'), ('a','b'), ('b','c')]
"""
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def create_linked_list(courses):
    if not courses:
        return None
    head = ListNode(courses[0][0])
    current = head
    for pair in courses:
        new_node = ListNode(pair[1])
        current.next = new_node
        current = new_node
    return head

courses = [
    ('d', 'a'),
    ('a', 'b'),
    ('b', 'c'),
]

linked_list = create_linked_list(courses)

current = linked_list
while current:
    print(f'"{current.data}" -> ', end="")
    current = current.next
print("None")


"""
Find the middle of the linked list
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def create_linked_list(lst):
    head = Node(lst[0])
    temp_node = head
    index = 1
    while index < len(lst):
        new_node = Node(lst[index])
        temp_node.next = new_node
        temp_node = new_node
        index += 1
    return head

def middle_node(head):
    fast_pointer = head
    slow_pointer = head
    while fast_pointer and fast_pointer.next:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next
    return slow_pointer

head = create_linked_list([1,2,3,4,5,6])
middle = middle_node(head)
print(middle)