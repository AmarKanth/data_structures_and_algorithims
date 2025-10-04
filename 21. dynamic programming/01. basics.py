"""
Dynamic programming is an algorthmic technique for solving an optimization problem by breaking 
it down into simpler subproblems and utilizing the fact that the optimal solution to the overall 
problem depends upon the optimal solution to its subproblems.
"""

"""
Optimal Substracture : If any problem's overall optimal solution can be constructed from the 
optimal solutions of the subproblem then this problem has optimal substracture.
ex : Fib(n) = Fib(n-1) + Fib(n-2)
"""

"""
Overlapping Subproblem : Subproblem are smaller versions of the original problem. Any Problem has 
overlapping sub problem if finding its solution involves solving the same subproblem multiple times.
"""

"""
Top Down with memoization : Solving the bigger problem by recursively finding the solution to 
smaller subproblem. Whatever we solve a sub-problem, we cache its results so that we dont end up 
solving it repeatedly if its called multiple times. 
This technique of storing the results of already solved problems is callled memoization.
"""

"""
1277 Count square submatrices with all ones
"""
matrix =[[0,1,1,1],
         [1,1,1,1],
         [0,1,1,1]]

m = len(matrix)
n = len(matrix[0])

result = 0
for i in range(m):
    for j in range(n):
        if i > 0 and j > 0 and matrix[i][j] == 1:
            matrix[i][j] = 1 + min(
                matrix[i-1][j],
                matrix[i][j-1],
                matrix[i-1][j-1]
            )
        result += matrix[i][j]
print(result)

"""
1043 Partition array for maximum sum
"""
arr = [1,15,7,9,2,5,10]
k = 3

dp = [0]*k
dp[0] = arr[0]

for i in range(1, len(arr)):
    cur_max = 0
    max_at_i = 0
    for j in range(i, i-k, -1):
        if j < 0:
            break
        cur_max = max(cur_max, arr[j])
        window_size = i-j+1
        cur_sum = cur_max*window_size
        sub_sum = dp[(j-1)%k] if j > 0 else dp[-1]
        max_at_i = max(max_at_i, cur_sum+sub_sum)
    dp[i%k] = max_at_i
print(dp[(len(arr)-1)%k])

"""
118 Pascals Triangle
"""
numRows = 5
dp = [[0]*(i+1) for i in range(numRows)]

for row in range(numRows):
    dp[row][0] = dp[row][row] = 1
    for col in range(1, row):
        dp[row][col] = dp[row-1][col-1]+dp[row-1][col]
print(dp)

"""
746. Min Cost Climbing Stairs
"""
cost = [10,15,20]
cost.append(0)
for i in range(len(cost)-3, -1, -1):
    cost[i] += min(cost[i+1], cost[i+2])
print(cost)