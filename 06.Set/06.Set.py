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
copy - it copies the original set and changes in original won’t change the copied object.
"""

"""
difference - it returns the difference of the two sets.
"""

"""
difference_update - it removes the items that exists in both the sets.
"""

"""
intersection_update - it removes the non-common items between the sets.
"""

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

"""
update - it updates set with non-existing items.
"""