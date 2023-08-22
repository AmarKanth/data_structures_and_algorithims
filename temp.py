"""
s = "cdfgaa ksdjfsa bbbb"
Write a program to find longest palindrome
"""
s = "cdfgaa ksdjfsa bbbb"
l = ""
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        sub = s[i:j]
        if sub == sub[::-1] and len(sub) > len(l):
            l = sub
print(l)