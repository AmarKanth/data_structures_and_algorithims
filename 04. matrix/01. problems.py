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