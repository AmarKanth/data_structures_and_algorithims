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
