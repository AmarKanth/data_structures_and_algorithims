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
def flatten_list(input, res):
    if type(input) == dict:
        for ele in list(input.values()):
            flatten_list(ele, res)
    elif type(input) == list:
        res.extend(input)
    else:
        res.append(input)
    return res

output = flatten_list({"a": "1", "b":[1,2,3,5], "c": {"a":1, "b":[1,2,3,4]}}, [])
print(output)