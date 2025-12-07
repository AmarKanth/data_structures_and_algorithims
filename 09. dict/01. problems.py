"""
1. items returns list of tuples with key, value
2. keys returns list of keys
3. values returns list of values
4. len returns the len of the dict
"""


"""
{"a": "1", "b":[1,2,3,5], "c": {"a":1, "b":[1,2,3,4]}} return values of given dict in flatten list.

output should like this ['1', 1, 2, 3, 5, 1, 1, 2, 3, 4]
"""
def flatten_list(input, res):
    if type(input) == dict:
        for ele in list(input.values()):
            flatten_list(ele, res)
    elif type(input) == list:
        res.extend(input)
    else:
        res.append(input)
    return res

output = flatten_list({"a": "1", "b":[1,2,3,5], "c": {"a":1, "b":[1,2,3,4]}}, [])
print(output)


"""
Implement the LRUCache
"""
from collections import OrderedDict

class LRUCache:
    def __init__(self, size):
        self.max_size = size
        self.elements = OrderedDict()
    
    def get(self, key):
        if key in self.elements:
            self.elements.move_to_end(key, last=True)
            return self.elements[key]
        return -1
    
    def put(self, key, value):
        if key in self.elements:
            self.elements.move_to_end(key, last=True)
        else:
            if len(self.elements) >= self.max_size:
                self.elements.popitem(last=False)
        self.elements[key] = value
    
    def peek(self, key):
        return self.elements.get(key, -1)
    
    def clear(self):
        self.elements.clear()


"""
1329. Sort the Matrix Diagonally
"""
from collections import defaultdict

mat = [[3,3,1,1],
       [2,2,1,2],
       [1,1,1,2]]

m, n = len(mat), len(mat[0])
diagonals = defaultdict(list)

for i in range(m):
    for j in range(n):
        diagonals[i - j].append(mat[i][j])

for key in diagonals:
    diagonals[key].sort(reverse=True)

for i in range(m):
    for j in range(n):
        mat[i][j] = diagonals[i - j].pop()
print(mat)