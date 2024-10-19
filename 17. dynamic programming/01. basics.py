"""
Dynamic programming is an algorthmic technique for solving an optimization problem by breaking it down 
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

"""
Fibonacci series using Top Down
"""
def fibonacci(n, memo):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n not in memo:
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]

res = fibonacci(10, {})
print(res)


"""
Bottom Up with Tabulation : Tabulation is the opposite of the top-down approach and avoids recursion. 
In this approach, we solve the problem bottom-up (i.e by solving all the related subproblems first). 
This is done by filling up a table. Based on the result in the table, the solution to the top/original 
problem is then computed.
"""

"""
Fibonacci series using Bottom Up
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
S1 and S2 are given strings
Convert S2 to S1 using delete, insert or replace operations
Find the minimum count of edit operations
"""
def find_min_operations(s1, s2, index1, index2, temp_dict):
    if index1 == len(s1):
        return len(s2) - index2
    if index2 == len(s2):
        return len(s1) - index1
    if s1[index1] == s2[index2]:
        return find_min_operations(s1, s2, index1+1, index2+1, temp_dict)
    else:
        dict_key = str(index1)+str(index2)
        if dict_key not in temp_dict:
            delete_op = 1 + find_min_operations(s1, s2, index1, index2+1, temp_dict)
            insert_op = 1 + find_min_operations(s1, s2, index1+1, index2, temp_dict)
            replace_op = 1 + find_min_operations(s1, s2, index1+1, index2+1, temp_dict)
            temp_dict[dict_key] = min(delete_op, insert_op, replace_op)
        return temp_dict[dict_key]

res = find_min_operations("catch", "carch", 0, 0, {})
print(res)


"""
Given the weights and profits of N items
Find the maximum profit within given capacity of C
items can not be broken
"""
class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight
 
def zo_knapsack(items, capacity, current_index, temp_dict):
    dict_key = str(current_index) + str(capacity)
    if capacity <=0 or current_index < 0 or current_index >= len(items):
        return 0
    elif dict_key in temp_dict:
        return temp_dict[current_index]
    elif items[current_index].weight <= capacity:
        profit1 = items[current_index].profit + zo_knapsack(items, capacity-items[current_index].weight, current_index+1, temp_dict)
        profit2 = zo_knapsack(items, capacity, current_index+1, temp_dict)
        temp_dict[dict_key] = max(profit1, profit2)
        return temp_dict[dict_key]
    else:
        return 0


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


"""
S1 and S2 are given strings
Convert S2 to S1 using delete, insert or replace operations
Find the minimum count of edit operations
"""
def find_min_operations(s1, s2, temp_dict):
    for i1 in range(len(s1)+1):
        dict_key = str(i1)+'0'
        temp_dict[dict_key] = i1
    
    for i2 in range(len(s2)+1):
        dict_key = '0'+str(i2)
        temp_dict[dict_key] = i2
    
    for i1 in range(1,len(s1)+1):
        for i2 in range(1,len(s2)+1):
            if s1[i1-1] == s2[i2-1]:
                dict_key = str(i1)+str(i2)
                dict_key1 = str(i1-1)+str(i2-1)
                temp_dict[dict_key] = temp_dict[dict_key1]
            else:
                dict_key = str(i1)+str(i2)
                dict_keyd = str(i1-1)+str(i2)
                dict_keyi = str(i1)+str(i2-1)
                dict_Keyr = str(i1-1)+str(i2-1)
                temp_dict[dict_key] = 1 + min(temp_dict[dict_keyd], min(temp_dict[dict_keyi], temp_dict[dict_Keyr]))
    dict_key = str(len(s1))+str(len(s2))
    return temp_dict[dict_key]

res = find_min_operations("catch", "carch", {})
print(res)


"""
Given the weights and profits of N items
Find the maximum profit within given capacity of C
items can not be broken
"""
def zo_knapsack(profits, weights, capacity):
    if capacity <= 0 or len(profits) == 0 or len(weights) != len(profits):
        return 0
    number_of_rows = len(profits) + 1
    dp = [[None for i in range(capacity+2)] for j in range(number_of_rows)]
    for i in range(number_of_rows):
        dp[i][0] = 0
    for i in range(capacity+1):
        dp[number_of_rows-1][i] = 0
    for row in range(number_of_rows-2, -1, -1):
        for column in range(1,capacity+1):
            profit1 = 0
            profit2 = 0
            if weights[row] <= column:
                profit1 = profits[row] + dp[row + 1][column - weights[row]]
            profit2 = dp[row + 1][column]
            dp[row][column] = max(profit1, profit2)
    return dp[0][capacity]
