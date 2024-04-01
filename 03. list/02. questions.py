"""
del keyword is use to delete objects in python.
"""
class MyClass:
  name = "John"

del MyClass
print(MyClass)

x = "hello"
del x
print(x)

x = ["apple", "banana", "cherry"]
del x[0]
print(x)


"""
[
    {"name": "vijay", "age": 20},
    {"name": "kumar", "age": 40},
    {"name": "rakesh", "age": 30}
]
sort the given list based on age
"""
obj = [
    {"name": "vijay", "age": 20},
    {"name": "kumar", "age": 40},
    {"name": "rakesh", "age": 30}
]

res = sorted(obj, key=lambda d: d["age"])
print(res)


"""
input = ["-1", "0", "2", "3", "4","-1","-2", "-1","3", "-1"] write program to return 
output ['-1', '-1', '-1', '-1', '0', '2', '3', '4', '-2', '3'] from the given list
"""
input = ["-1", "0", "2", "3", "4", "-1", "-2", "-1", "3", "-1"]
n = len(input)
last_index = 0
for i in range(n):
    if input[i] == "-1":
        input[i], input[last_index] = input[last_index], input[i]
        last_index += 1
print(input)

input = ["-1", "0", "2", "3", "4", "-1", "-2", "-1", "3", "-1"]
n = len(input)
last_index = n - 1
for i in range(n-1, -1, -1):
    if input[i] == "-1":
        input[i], input[last_index] = input[last_index], input[i]
        last_index -= 1
print(input)


"""
Write a code to return number of occurrences of elements in the list l = [1,2,3,4,4,4], 
without using counter
output = {1: 1, 2: 1, 3: 1, 4: 3}
"""
l = [1,2,3,4,4,4]
d = {k: 0 for k in set(l)}
for e in l:
    count = d[e]
    d[e] = count + 1
print(d)


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
Write a function to sort elements in the list without using sort function
"""
l = [2,1,3]
for i in range(len(l)):
    for j in range(i+1, len(l)):
        if l[i] > l[j]:
            l[i], l[j] = l[j], l[i]
print(l)


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
"""
l = [1, 2, 3, 4, 5, 6, 8, 9]
def find_missing_number(l, n):
    sum1 = n*(n+1)//2
    sum2 = sum(l)
    return sum1-sum2
res = find_missing_number(l, 9)
print(res)