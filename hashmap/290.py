"""
LeetCode #290

Author: Jose Renteria

"""

def wordPattern(pattern: str, s: str) -> bool:
    s = s.split()
    hash_map = {}
    l = []
    for i, c in enumerate(pattern):
        if c in hash_map:
            l.append(hash_map[c] == s[i])
        hash_map[c] = s[i]
    print(l)
    for el in l:
        if el == False:
            return el
    return True


sol = wordPattern("abba", "dog dog dog dog")
print(sol)