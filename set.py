"""
1. sets are unorder collection of unique elements.
2. We can't access specific element from set because these are un-indexed. 
For loop, iter, in  and next are the different ways to access the elements. 
"""

"""
adds the element to the set
"""
s1 = set()
s1.add("a")
print(s1)

"""
clear truncate the set
"""
s1 = set("a")
s1.clear()
print(s1)

"""
removes specific element
"""
s1 = {"a", "b"}
s1.discard("b")
print(s1)

"""
Write a program to display the common letters in both the strings
"""
s1 = set("ac")
s2 = set("ab")
res = s1.intersection(s2)
print(res)