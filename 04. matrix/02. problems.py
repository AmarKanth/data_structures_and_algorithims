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