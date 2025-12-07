"""
1314. Matrix Block Sum
"""
def matrix_block_sum(mat, k):
    m, n = len(mat), len(mat[0])
    pre = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m):
        row_sum = 0
        for j in range(n):
            row_sum += mat[i][j]
            pre[i + 1][j + 1] = pre[i][j + 1] + row_sum

    ans = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            r1 = max(0, i - k)
            c1 = max(0, j - k)
            r2 = min(m - 1, i + k)
            c2 = min(n - 1, j + k)

            R1, C1 = r1, c1
            R2, C2 = r2 + 1, c2 + 1

            total = (
                pre[R2][C2]
                - pre[R1][C2]
                - pre[R2][C1]
                + pre[R1][C1]
            )
            ans[i][j] = total
    return ans

mat = [[1,2,3],
       [4,5,6],
       [7,8,9]]
result = matrix_block_sum(mat, 1)
print(result)


"""
3242. Design Neighbor Sum Service
"""
class NeighborSum:
    def __init__(self, grid):
        self.grid = grid
        self.n = len(grid)
        self.pos = {}
        for i in range(self.n):
            for j in range(self.n):
                self.pos[grid[i][j]] = (i, j)

    def adjacent_sum(self, value):
        r, c = self.pos[value]
        n = self.n
        total = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n:
                total += self.grid[nr][nc]
        return total

    def diagonal_sum(self, value):
        r, c = self.pos[value]
        n = self.n
        total = 0
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n:
                total += self.grid[nr][nc]
        return total

grid = [[0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]]

ns = NeighborSum(grid)
print(ns.adjacent_sum(1))
print(ns.adjacent_sum(4))
print(ns.diagonal_sum(4))
print(ns.diagonal_sum(8))


"""
1992. Find All Groups of Farmland
"""
def find_farmland(land):
    m, n = len(land), len(land[0])
    res = []

    for i in range(m):
        for j in range(n):
            if land[i][j] == 1:
                r = i
                while r + 1 < m and land[r + 1][j] == 1:
                    r += 1

                c = j
                while c + 1 < n and land[i][c + 1] == 1:
                    c += 1
                
                res.append([i, j, r, c])
                
                for x in range(i, r + 1):
                    for y in range(j, c + 1):
                        land[x][y] = 0
    return res

land = [[1,0,0],[0,1,1],[0,1,1]]
result = find_farmland(land)
print(result)


"""
867. Transpose Matrix
"""
matrix = [[1,2,3],[4,5,6],[7,8,9]]
rows = len(matrix)
cols = len(matrix[0])

result = [[0] * rows for _ in range(cols)]
for r in range(rows):
    for c in range(cols):
        result[c][r] = matrix[r][c]
print(result)


"""
883. Projection Area of 3D Shapes
"""
grid = [[1,2],[3,4]]
n = len(grid)
top = sum(1 for i in range(n) for j in range(n) if grid[i][j] > 0)
front = sum(max(row) for row in grid)
side = 0

for j in range(n):
    max_col = 0
    for i in range(n):
        if grid[i][j] > max_col:
            max_col = grid[i][j]
    side += max_col
print(top + front + side)