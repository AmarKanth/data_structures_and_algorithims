"""
Dynamic programming is an algotthmic technique for solving an optimization problem by breaking it down 
into simpler subproblems and utilizing the fact that the optimal solution to the overall problem depends 
upon the optimal solution to its subproblems.
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
solving it repeatedly if its called multiple times. This technique of storing the results of 
already solved problems is callled memoization.
"""
def fibonacci(n, memo):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if not n in memo:
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]

res = fibonacci(10, {})
print(res)


"""
Given N, find the number of ways to express N as a sum of 1, 3 and 4
"""
def number_factor(n, tempdict):
    if n in [0,1,2]:
        return 1
    if n == 3:
        return 2 
    if n not in tempdict:
        p1 = number_factor(n-1, tempdict)
        p2 = number_factor(n-3, tempdict)
        p3 = number_factor(n-4, tempdict)
        tempdict[n] = p1 + p2 + p3
    return tempdict[n]

res = number_factor(5, {})
print(res)


"""
Given N number of houses along the street with some amount of money 
Adjacent houses can not be stolen
Find the maximum amount that can be stolen
"""
def house_robber(houses, current_index, temp_dict):
    if current_index >= len(houses):
        return 0
    if current_index not in temp_dict:
        steal_first_house = houses[current_index] + house_robber(houses, current_index+2, temp_dict)
        skip_house = house_robber(houses, current_index+1, temp_dict)
        temp_dict[current_index] = max(steal_first_house, skip_house)
    return temp_dict[current_index]

res = house_robber([6,7,1,30,8,2,4], 0, {})
print(res)


"""
Bottom Up with Tabulation : Tabulation is the opposite of the top-down approach and avoids recursion. 
In this approach, we solve the problem bottom-up (i.e by solving all the related subproblems first). 
This is done by filling up a table. Based on the result in the table, the solution to the top/original 
problem is then computed.
"""
def fibonacci(n):
    tb = [0,1]
    for i in range(2, n+1):
        tb.append(tb[i-1]+tb[i-2])
    return tb[n-1]

res = fibonacci(10)
print(res)


"""
Given N, find the number of ways to express N as a sum of 1, 3 and 4
"""
def number_factor(n):
    temp_arr = [1,1,1,2]
    for i in range(4, n+1):
        temp_arr.append(temp_arr[i-1]+temp_arr[i-3]+temp_arr[i-4])
    return temp_arr[n]

res = number_factor(5)
print(res)


"""
Given N number of houses along the street with some amount of money 
Adjacent houses can not be stolen
Find the maximum amount that can be stolen
"""
def house_robber(houses):
    temp_arr = [0] * (len(houses) + 2)
    for i in range(len(houses)-1, -1, -1):
        temp_arr[i] = max(houses[i]+temp_arr[i+2], temp_arr[i+1])
    return temp_arr[0]

res = house_robber([6,7,1,30,8,2,4])
print(res)