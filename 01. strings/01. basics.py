"""
1. strings are immutables which mean we cant replace or add element to the string.
2. indexing means fetching specific element from the string.
3. slicing means grabbing sub section from the string.
4. reverse indexing means reads the element from the last element. it starts with negative number.
"""

"""
upper - Converts to upper
isupper - checks the given string is uppercase.
"""

"""
lower - Converts to lower
islower - checks the given string is lowercase.
"""

"""
capitalize - it capitalizes first letter in the string.
"""

"""
split - it converts string into list based on delimiter.
"""

"""
count - it counts the number occurrences of specific element.
"""

"""
find - it verifies specific prase in the string. Returns –1 if it doesn’t have given element.
"""

"""
isalnum - method in Python is used to check if all the characters in a given string are alphanumeric. 
Alphanumeric characters include letters (alphabets) and numbers (digits). If all the characters in the string 
are either letters or numbers (and the string is not empty), the isalnum() method returns True; 
otherwise, it returns False.
"""
lst = ["HelloWorld", "Hello, World!", "12345", "", "Hello123"]
res = [ele for ele in lst if ele.isalnum()]
print(res)

"""
isalpha - method is used to check if all the characters in a given string are alphabetic characters (letters) 
and there are no numeric or special characters in the string. It returns True if all characters in the string 
are alphabetic, and False otherwise.
"""

"""
isdigit : This method checks if the given string contains all numbers. 
It returns False if it includes special characters or alphabetic characters.
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
without using count method
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
sort = sorted(res, key=lambda s: len(s), reverse=True)
print(sort[0])