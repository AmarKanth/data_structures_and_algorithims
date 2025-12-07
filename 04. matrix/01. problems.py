"""
2373. Largest Local Values in a Matrix
"""
grid = [[9,9,8,1],
        [5,6,2,6],
        [8,2,6,4],
        [6,2,2,2]]

n = len(grid)
max_local = [[0]*(n-2) for _ in range(n-2)]

for i in range(n-2):
    for j in range(n-2):
        max_val = float("-inf")
        for di in range(i, i+3):
            for dj in range(j, j+3):
                max_val = max(grid[di][dj], max_val)
        max_local[i][j] = max_val
print(max_local)


"""
885. Spiral Matrix III

7   8   9
6   1   2
5   4   3
"""
def spiral_matrix_III(rows, cols, rStart, cStart):
    res = []
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    r, c = rStart, cStart
    step = 1

    if 0 <= r < rows and 0 <= c < cols:
        res.append([r, c])

    while len(res) < (rows*cols):
        for direction in range(4):
            dr, dc = directions[direction]
            for _ in range(steps):
                r += dr
                c += dc
                if 0 <= r < rows and 0 <= c < cols:
                    res.append([r, c])
            if direction % 2 == 1:
                step += 1
    return res

result = spiral_matrix_III(3, 3, 1, 1)
print(result)


"""
2482. Difference Between Ones and Zeros in Row and Column
"""
grid = [[0,1,1],
        [1,0,1],
        [0,0,1]]

m, n = len(grid), len(grid[0])
ones_row = [sum(row) for row in grid]
ones_col = [sum(grid[i][j] for i in range(m)) for j in range(n)]

diff = [[0] * n for _ in range(m)]
for i in range(m):
    for j in range(n):
        diff[i][j] = ones_row[i] + ones_col[j] - (n-ones_row[i]) - (m-ones_col[j])
print(diff)


"""
1572. Matrix Diagonal Sum
"""
mat = [[1,2,3],
       [4,5,6],
       [7,8,9]]

n = len(mat)
total = 0
for i in range(n):
    total += mat[i][i]
    total += mat[i][n - i - 1]

if n % 2 == 1:
    total -= mat[n // 2][n // 2]
print(total)


"""
1605. Find Valid Matrix Given Row and Column Sums
"""
rowSum1 = [3,8]
colSum1 = [4,7]

m, n = len(rowSum), len(colSum)
matrix = [[0] * n for _ in range(m)]

for i in range(m):
    for j in range(n):
        val = min(rowSum[i], colSum[j])
        matrix[i][j] = val
        
        rowSum[i] -= val
        colSum[j] -= val
print(matrix)