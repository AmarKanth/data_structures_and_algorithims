"""
[
    {"name": "vijay", "age": 20},
    {"name": "kumar", "age": 40},
    {"name": "rakesh", "age": 30}
]
sort the given list based on age
"""
obj = [{"name": "vijay", "age": 20}, {"name": "kumar", "age": 40}, {"name": "rakesh", "age": 30}]
res = sorted(obj, key=lambda d: d["age"])
print(res)


"""
input = ["-1", "0", "2", "3", "4","-1","-2", "-1","3", "-1"] write program to return 
output ['-1', '-1', '-1', '-1', '0', '2', '3', '4', '-2', '3'] from the given list
"""
def reorder_list(input_list):
    minus_ones = [x for x in input_list if x == "-1"]
    others = [x for x in input_list if x != "-1"]
    return minus_ones + others

input_list = ["-1", "0", "2", "3", "4", "-1", "-2", "-1", "3", "-1"]
res = reorder_list(input_list)
print(res)


"""
Find second largest number from the given list
lst = [2, 9, 3]
"""
lst = [2, 9, 3]
largest = second_largest = 0
for num in lst:
    if num > largest:
        largest, second_largest = num, largest
    elif num > second_largest and num != largest:
        second_largest = num
print(second_largest)


"""
Write a program to reverse the list using recursion
"""
def reverse(l):
    if len(l) == 0:
        return l
    return reverse(l[1:]) + l[:1]
res = reverse([2,1,3])
print(res)


"""
how to find missing number in a list of 1 to 10
using sum of n series equation 
1+2+3+4+...+n = n*(n+1)/2
l = [1, 2, 3, 4, 5, 6, 8, 9]
n = 9
"""
l = [1, 2, 3, 4, 5, 6, 8, 9]
def find_missing_number(l, n):
    sum1 = n*(n+1)//2
    sum2 = sum(l)
    return sum1-sum2
res = find_missing_number(l, 9)
print(res)

