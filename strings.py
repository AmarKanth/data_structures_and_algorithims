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
l = len("ab")
count = 0

for i in range(len(s)):
    if s[i:l] == "ab":
        count = count + 1
    l = l + 1

print(count)


"""
Find longest common substring between given string
str1 = "GeeksforGeeks"
str2 = "GeeksQuiz"
"""
str1 = "GeeksforGeeks"
str2 = "GeeksQuiz"

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


"""
check palindrome using recursion
"""
def palindrome(string):
    if len(string) == [1, 0]:
        return True

    if string[0] != string[len(string)-1]:
        return False

    string1 = string[1:]
    string2 = string1[:len(string1)-1]
    return palindrome(string2)

res = palindrome("amar")
print(res)


"""
s = "cdfgaa ksdjfsa bbbb"
Write a program to find longest palindrome
"""
s = "cdfgaa ksdjfsa bbbb"
l = ""

for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        sub = s[i:j]
        if sub == sub[::-1] and len(l) < len(sub):
            l = sub

print(l)


"""
Find all palindromic sub-strings of a given string
"""
string = "hellolle"
l = list()

for i in range(len(string)):
    for j in range(i+1, len(string)+1):
        sub = string[i:j]
        if sub == sub[::-1]:
            l.append(sub)

print(l)


"""
Check if a given string is a rotation of a palindrome
"""
def find_palindrome(string):
    n = len(string)

    if string == string[::-1]:
        return string
    
    for i in range(n-1):
        string1 = string[i+1:]
        string2 = string[:i+1]
        string1+=(string2)
        if string1 == string1[::-1]:
            break
    else:
        return None

    return string1

res = find_palindrome("madam")
print(res)


"""
Check if characters of a given string can be rearranged to form a palindrome

1. here "f","o","r" are odd occurances
2. if number of odd occurances are > 1 cant arrange 
string to  palindrome.
"""
from collections import Counter
string = "geeksforgeeks"

def can_be_palindrome(string):
    counter = Counter(string)
    odd_nums = [i for i in counter.values() if i%2 != 0]

    if len(odd_nums) > 1:
        return False
    return True


"""
Minimum number of deletions to make a string palindrome
"""
def num_of_appends(s):

    if len(s) == 0:
        return 0
 
    if s == s[::-1]:
        return 0

    del s[0]    
    return 1 + num_of_appends(s)

l = [i for i in "aabb"]
res = num_of_appends(l)
print(res)


"""
Minimum characters to be added at front to make string palindrome
"""
def num_of_appends(s):
    if len(s) == 0:
        return 0
 
    if s == s[::-1]:
        return 0

    del s[len(s)-1]    
    return 1 + num_of_appends(s)

l = [i for i in "AACECAAAA"]
res = num_of_appends(l)
print(res)