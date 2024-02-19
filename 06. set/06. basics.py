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

"""
intersection_update - it keeps the common elements and removes unmatched elements in set 1.
"""
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
s1.intersection_update(s2)
print(s1)

"""
copy - it copies the original set and changes in original won’t change the copied object.
"""

"""
difference - it compares two sets and returns unmatched elements of set1.
"""
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
s = s1.difference(s2)
print(s)

"""
difference_update - it compares two sets and updates unmatches elements of set1.
"""
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
s1.difference_update(s2)
print(s1)

"""
isdisjoint - it returns true if the sets have null intersection and vice versa.
"""

"""
issubset - it returns true if the set is subset of other set.
"""

"""
issuperset - it’s reverse process of subset (if set contains other set).
"""

"""
symetric_difference - it returns non common items.
"""

"""
union - it combines the two sets.
"""
s1 = set("123")
s2 = set("456")
s = s1.union(s2)
print(s)

"""
update - it updates set with non-existing items.
"""
s1 = set("123")
s2 = set("126")
s1.update(s2)
print(s1)