"""
2482. Difference Between Ones and Zeros in Row and Column
"""
def ones_minus_zeros(grid):
    m, n = len(grid), len(grid[0])

    ones_row = [sum(row) for row in grid]
    ones_col = [sum(grid[i][j] for i in range(m)) for j in range(n)]

    diff = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            diff[i][j] = ones_row[i] + ones_col[j] - (n-ones_row[i]) - (m-ones_col[j])

    return diff

grid = [[0,1,1],
        [1,0,1],
        [0,0,1]]
result = ones_minus_zeros(grid)
print(result)


"""
1572. Matrix Diagonal Sum
"""
def diagonal_sum(mat):
    n = len(mat)
    total = 0
    
    for i in range(n):
        total += mat[i][i]
        total += mat[i][n - i - 1]
    
    if n % 2 == 1:
        total -= mat[n // 2][n // 2]
    return total

mat = [[1,2,3],
       [4,5,6],
       [7,8,9]]
result = diagonal_sum(mat)
print(result)


"""
2965. Find Missing and Repeated Values
"""
def find_repeat_and_missing(grid):
    n = len(grid)
    total_vals = n * n
    expected_sum = total_vals * (total_vals + 1) // 2

    seen = set()
    repeat = None
    sum_actual = 0

    for row in grid:
        for x in row:
            sum_actual += x
            if x in seen:
                repeat = x
            else:
                seen.add(x)

    missing = expected_sum - (sum_actual - repeat)
    return [repeat, missing]

grid = [[1,3],
        [2,2]]
result = find_repeat_and_missing(grid)
print(result)


"""
1329. Sort the Matrix Diagonally
"""
from collections import defaultdict

def diagonal_sort(mat):
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

    return mat

mat = [[3,3,1,1],
       [2,2,1,2],
       [1,1,1,2]]
result = diagonal_sort(mat)
print(result)


"""
1605. Find Valid Matrix Given Row and Column Sums
"""
def restore_matrix(rowSum, colSum):
    m, n = len(rowSum), len(colSum)
    matrix = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            val = min(rowSum[i], colSum[j])
            matrix[i][j] = val
            
            rowSum[i] -= val
            colSum[j] -= val

    return matrix

rowSum1 = [3,8]
colSum1 = [4,7]
result = restore_matrix(rowSum1, colSum1)
print(result)


"""
2326. Spiral Matrix IV
"""
class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next

def spiral_matrix(m, n, head):
    matrix = [[-1] * n for _ in range(m)]
    
    top, bottom = 0, m - 1
    left, right = 0, n - 1
    node = head
    
    while node and top <= bottom and left <= right:
        # left -> right (top row)
        for c in range(left, right + 1):
            if not node: break
            matrix[top][c] = node.val
            node = node.next
        top += 1
        if not node: break
        
        # top -> bottom (right column)
        for r in range(top, bottom + 1):
            if not node: break
            matrix[r][right] = node.val
            node = node.next
        right -= 1
        if not node: break
        
        # right -> left (bottom row)
        if top <= bottom:
            for c in range(right, left - 1, -1):
                if not node: break
                matrix[bottom][c] = node.val
                node = node.next
            bottom -= 1
        if not node: break
        
        # bottom -> top (left column)
        if left <= right:
            for r in range(bottom, top - 1, -1):
                if not node: break
                matrix[r][left] = node.val
                node = node.next
            left += 1
    
    return matrix