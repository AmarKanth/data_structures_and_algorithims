"""
1. items returns list of tuples with key, value
2. keys returns list of keys
3. values returns list of values
4. len returns the len of the dict
"""

"""
{"a": "1", "b":[1,2,3,5], "c": {"a":1, "b":[1,2,3,4]}} return values of given dict in flatten list.

output should like this ['1', 1, 2, 3, 5, 1, 1, 2, 3, 4]
"""
input = {"a": "1", "b":[1,2,3,5], "c": {"a":1, "b":[1,2,3,4]}}

def flatten_list(input):
    res = []
    if type(input) == dict:
        for ele in list(input.values()):
            res.extend(flatten_list(ele))
    elif type(input) == list:
        for ele in input:
            res.extend(flatten_list(ele))
    else:
        res.append(input)
    return res

res = flatten_list(input)
print(res)