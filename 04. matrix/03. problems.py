"""
861. Score After Flipping Matrix
"""
def matrix_score(grid):
    m = len(grid)
    n = len(grid[0])
    
    for i in range(m):
        if grid[i][0] == 0:
            for j in range(n):
                grid[i][j] ^= 1

    total = 0
    for j in range(n):
        ones = 0
        for i in range(m):
            ones += grid[i][j]
        max_ones = max(ones, m - ones)
        total += max_ones * (1 << (n - 1 - j))

    return total

result = matrix_score([[0,0,1,1],[1,0,1,0],[1,1,0,0]])
print(result)


"""
1380. Lucky Numbers in a Matrix
"""
def lucky_numbers(matrix):
    if not matrix or not matrix[0]:
        return []

    m, n = len(matrix), len(matrix[0])
    row_mins = [min(row) for row in matrix]
    col_maxs = [max(matrix[i][j] for i in range(m)) for j in range(n)]

    result = []
    for i in range(m):
        for j in range(n):
            val = matrix[i][j]
            if val == row_mins[i] and val == col_maxs[j]:
                result.append(val)

    return result

result = lucky_numbers([[3,7,8],[9,11,13],[15,16,17]])
print(result)


"""
2500. Delete Greatest Value in Each Row
"""
def delete_greatest_value(grid):
    if not grid or not grid[0]:
        return 0

    m, n = len(grid), len(grid[0])
    for row in grid:
        row.sort()

    ans = 0
    for j in range(n - 1, -1, -1):
        col_max = max(grid[i][j] for i in range(m))
        ans += col_max
    return ans

result = delete_greatest_value([[1,2,4],[3,3,1]])
print(result)