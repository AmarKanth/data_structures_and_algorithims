"""
1. strings are immutables which mean we cant replace or add element to the string.
2. indexing means fetching specific element from the string.
3. slicing means grabbing sub section from the string.
4. reverse indexing means reads the element from the last element. it starts with negative number.
"""

"""
txt = "my name is rakesh"
replace rakesh with vijay
"""
txt = "my name is rakesh"
x = txt.replace("rakesh", "vijay")
print(x)


"""
s = "sdls ab lld ab"
Write program to count number of occurrences of substring "ab" in given string
"""
s = "sdls ab lld ab"
count = 0
for i in range(len(s)):
    sub = s[i:i+2]
    if sub == 'ab':
        count += 1
print(count)


"""
Find longest common substring between given strings
str1 = "abcaaaabbb"
str2 = "abcaabb"
"""
str1 = "abcaaaabbb"
str2 = "abcaabb"

def extract_substrings(str):
    s = set()
    for i in range(len(str)):
        for j in range(i+1, len(str)+1):
            sub = str[i:j]
            s.add(sub)
    return s

set1 = extract_substrings(str1)
set2 = extract_substrings(str2)
res = set2.intersection(set1)
sort = sorted(list(res), key=lambda s: len(s), reverse=True)
print(sort[0])