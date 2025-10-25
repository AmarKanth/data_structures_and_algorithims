"""
2273. Find Resultant Array After Removing Anagrams
"""
def remove_anagrams(words):
    def sig(word):
        cnt = [0]*26
        for ch in word:
            cnt[ord(ch) - ord('a')] += 1
        return tuple(cnt)
    
    res = []
    res_sigs = []
    for w in words:
        s = sig(w)
        if res and res_sigs[-1] == s:
            continue
        res.append(w)
        res_sigs.append(s)
    return res

result = remove_anagrams(["abba","baba","bbaa","cd","cd"])
print(result)