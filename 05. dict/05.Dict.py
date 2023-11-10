"""
1. items returns list of tuples with key, value
2. keys returns list of keys
3. values returns list of values
"""

"""
Write code to sort the key, value pairs based on the values
d = {"a": 1, "c": 3, "b": 2}
"""
d = {"a": 1, "c": 3, "b": 2}
res = sorted(d.items(), key=lambda t: t[1])
print(dict(res))


"""
{"a": "1", "b":[1,2,3,5], "c": {"a":1, "b":[1,2,3,4]}} return values of given dict in flatten list.

output should like this ['1', 1, 2, 3, 5, 1, 1, 2, 3, 4]
"""
res = []

def flatten_list(obj):
    if type(obj) == dict:
        flatten_list(list(obj.values()))
    elif type(obj) == list:
        for e in obj:
            flatten_list(e)
    else:
        res.append(obj)

flatten_list({"a": "1", "b":[1,2,3,5], "c": {"a":1, "b":[1,2,3,4]}})
print(res)