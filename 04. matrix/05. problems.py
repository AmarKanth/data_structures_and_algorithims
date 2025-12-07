"""
3239. Minimum Number of Flips to Make Binary Grid Palindromic I
"""
grid = [[1,0,0],
        [0,0,0],
        [0,0,1]]
m = len(grid)
n = len(grid[0])

row_cost = 0
for i in range(m):
    for j in range(n // 2):
        if grid[i][j] != grid[i][n - 1 - j]:
            row_cost += 1

col_cost = 0
for j in range(n):
    for i in range(m // 2):
        if grid[i][j] != grid[m - 1 - i][j]:
            col_cost += 1

print(min(row_cost, col_cost))


"""
2643. Row With Maximum Ones
"""
mat = [[0,1],[1,0]]
max_ones = -1
row_index = -1

for i, row in enumerate(mat):
    ones = sum(row)
    if ones > max_ones:
        max_ones = ones
        row_index = i

print([row_index, max_ones])


"""
1337. The K Weakest Rows in a Matrix
"""
def count_ones_binary(row):
    lo, hi = 0, len(row)
    while lo < hi:
        mid = (lo + hi) // 2
        if row[mid] == 1:
            lo = mid + 1
        else:
            hi = mid
    return lo

def k_weakest_rows(mat, k):
    counts = [(count_ones_binary(row), i) for i, row in enumerate(mat)]
    counts.sort()
    return [idx for _, idx in counts[:k]]

mat1 = [[1,1,0,0,0],
        [1,1,1,1,0],
        [1,0,0,0,0],
        [1,1,0,0,0],
        [1,1,1,1,1]]
result = k_weakest_rows(mat1, 3)
print(result)