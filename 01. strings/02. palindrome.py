"""
check palindrome using recursion
"""
def palindrome(string):
    if len(string) in [1, 0]:
        return True
    if string[0] != string[len(string)-1]:
        return False
    string1 = string[1:]
    string2 = string1[:len(string1)-1]
    return palindrome(string2)

res = palindrome("amar")
print(res)


"""
Check if a given string is a rotation of a palindrome
"""
def find_palindrome(string):
    if string == string[::-1]:
        return string
    
    n = len(string)
    for i in range(n-1):
        string1 = string[i+1:]
        string2 = string[:i+1]
        string3 = string2 + string1
        if string3 == string3[::-1]:
            break
    else:
        return None
    return string3

res = find_palindrome("madam")
print(res)


"""
Check if characters of a given string can be rearranged to 
form a palindrome
"""
from collections import Counter
string = "geeksforgeeks"

def can_be_palindrome(string):
    counter = Counter(string)
    odd_nums = [i for i in counter.values() if i%2 != 0]

    if len(odd_nums) > 1:
        return False
    return True