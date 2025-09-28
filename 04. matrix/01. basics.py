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