"""
2326. Spiral Matrix IV
"""
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def create_linked_list(arr):
    head = ListNode(arr[0])
    temp_node = head
    for i in range(1, len(arr)):
        new_node = ListNode(arr[i])
        temp_node.next = new_node
        temp_node = temp_node.next
    return head

m = 3
n = 3
head = create_linked_list(list(range(8)))

i = 0
j = 0
turn = 0
movement = [[0, 1], [1, 0], [0, -1], [-1, 0]]
result = [[-1 for _ in range(n)] for _ in range(m)]

while head is not None:
    result[i][j] = head.val
    x = i + movement[turn][0]
    y = j + movement[turn][1]

    if (min(x, y) < 0 or x >= m or y >= n or result[x][y] != -1):
        turn = (turn + 1) % 4
    
    i += movement[turn][0]
    j += movement[turn][1]
    head = head.next
print(result)