"""
Count the negative numbers in sorted matrix
"""
grid = [[4,3,2,-1],
        [3,2,1,-1],
        [1,1,-1,-2],
        [-1,-1,-2,-3]]

i = len(grid)-1
j = 0
count = 0
while i>=0 and j< len(grid[0]):
    if grid[i][j] < 0:
        count +=len(grid[0])-j
        i -= 1
    else:
        j +=1
print(count)