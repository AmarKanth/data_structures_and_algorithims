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