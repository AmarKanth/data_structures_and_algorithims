"""
1351 Count the negative numbers in sorted matrix
"""
grid = [[4,3,2,-1],
        [3,2,1,-1],
        [1,1,-1,-2],
        [-1,-1,-2,-3]]

rows = len(grid)
cols = len(grid[0])

i = rows-1
j = 0
counter = 0

while i >= 0 and j < cols:
    if grid[i][j] < 0:
        counter += cols-j
        i -= 1
    else:
        j += 1
print(counter)


"""
2373. Largest Local Values in a Matrix
"""
def largest_local(grid):
    n = len(grid)
    if n < 3:
        return []

    res = [[0] * (n - 2) for _ in range(n - 2)]

    for i in range(n - 2):
        for j in range(n - 2):
            m = grid[i][j]
            for di in range(3):
                for dj in range(3):
                    val = grid[i + di][j + dj]
                    if val > m:
                        m = val            
            res[i][j] = m
    return res

grid = [[9,9,8,1],
        [5,6,2,6],
        [8,2,6,4],
        [6,2,2,2]]

result = largest_local(grid)
print(result)


"""
2125. Number of Laser Beams in a Bank
"""
def number_of_beams(bank):
    prev_count = 0
    total = 0

    for row in bank:
        cnt = row.count('1')
        if cnt > 0:
            total += prev_count * cnt
            prev_count = cnt
    return total

bank = ["011001","000000","010100","001000"]
result = number_of_beams(bank)
print(result)


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