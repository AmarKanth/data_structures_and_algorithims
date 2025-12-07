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
"""
def spiral_matrix_III(rows, cols, rStart, cStart):
    total = rows * cols
    res = []
    
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    r, c = rStart, cStart
    step = 1

    if 0 <= r < rows and 0 <= c < cols:
        res.append([r, c])

    while len(res) < total:
        for d in range(4):
            dr, dc = dirs[d]
            steps_this_leg = step
            for _ in range(steps_this_leg):
                r += dr
                c += dc
                if 0 <= r < rows and 0 <= c < cols:
                    res.append([r, c])
                    if len(res) == total:
                        return res
            if d % 2 == 1:
                step += 1
    return res

result = spiral_matrix_III(1, 4, 0, 0)
print(result)