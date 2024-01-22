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