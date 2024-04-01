"""
Find the number of pairs where nums[i] + nums[j] < 2
nums = [-1,1,2,3,1]
"""
nums = [-1,1,2,3,1]
nums.sort()
left = 0
right = len(nums)-1
target = 2
count = 0

while left < right:
    if nums[left] + nums[right] < target:
        count += right - left
        left += 1
    else:
        right -= 1
print(count)


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