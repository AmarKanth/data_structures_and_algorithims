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