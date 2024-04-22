"""
LeetCode #387 First Unique Char in a String

Author: Jose Renteria
"""

def firstUniqChar(s: str) -> int:
    hash_map = {}
    for c in s:
        if c not in hash_map:
            hash_map[c] = 1
        else:
            hash_map[c] += 1

    l = []
    for val in hash_map:
        if hash_map[val] == 1:
            l.append(val)
    return s.index(l[0])

sol = firstUniqChar("leetcode")
print(sol)